import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.7)

def Draw(img):
    for i in buttonList:
        img = i.draw(img)
    return img

class Button():
    def __init__(self, pos, text, size=[100, 100]):
        self.pos = pos
        self.text = text
        self.endPos = [size[0] + pos[0], size[1] + pos[1]]

    def draw(self, img):
        cv2.rectangle(img, self.pos, self.endPos, (255, 0, 255))
        cv2.putText(img, self.text, (self.pos[0] + 20, self.pos[1] + 80), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

        return img


val = list('QWERTY')
buttonQ = Button([100, 100], "Q")

buttonList = []

for j, i in enumerate(val):
    cl = Button([(j + 1) * 100, 100], i)
    buttonList += [cl]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist, bboxInfo = detector.findPosition(img)
    img = Draw(img)


    if lmlist:
        for button in buttonList:
            x,y = button.pos
            w,h = button.endPos

            if x<=lmlist[8][0]<=w and y<=lmlist[8][1]<=h:
                cv2.rectangle(img, button.pos, button.endPos, (0, 0, 255), cv2.FILLED)
                cv2.putText(img, button.text, (button.pos[0] + 20, button.pos[1] + 80), cv2.FONT_HERSHEY_PLAIN, 5,
                            (255, 255, 255), 5)


    cv2.imshow('Image', img)

    cv2.waitKey(1)

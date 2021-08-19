import cv2
import mediapipe as mp

img = cv2.imread('test.png')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edge = cv2.Canny(img_gray, 90, 10)
nimg = img.copy()
ret, thresh = cv2.threshold(edge, 150, 255, cv2.THRESH_BINARY)


contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(contours)
# cv2.drawContours(image=img, contours=contours,contourIdx=-1, color=(0,255,0), thickness=8,lineType=cv2.LINE_AA)
import random


for i, contour in enumerate(contours):  # loop over one contour area
    for j, contour_point in enumerate(contour):  # loop over the points
        b,g,r = random.randint(1,255),random.randint(1,255),random.randint(1,255)
        # draw a circle on the current contour coordinate
        cv2.circle(img, (contour_point[0][0], contour_point[0][1]), 2, (b,g,r), 2, cv2.LINE_AA)

cv2.imshow('Test', img)

cv2.waitKey()
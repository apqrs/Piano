import cv2
import numpy as np
import time

blank = np.zeros((500,500,3),dtype="uint8")


blank[100:300]=0,255,0

cv2.rectangle(blank, (10,10), (300,100), (0,0,255), 2)

cv2.line(blank, (0,0), (250,250), (255,0,255), 2)

# img = cv2.imread("piano.jpg")
# img = cv2.resize(img, (int(img.shape[1]*0.5),int(img.shape[0]*0.5)))
cv2.imshow("Image", blank)

cv2.waitKey()

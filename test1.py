import kociemba
import numpy as np
#print(kociemba.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD'))
import cv2
import imutils

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    blur = cv2.GaussianBlur(frame,(5, 5), 0)
    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 100, 100])
    upper_red = np.array([5, 255, 255])

    lower_orange = np.array([9, 85, 100])
    upper_orange = np.array([12, 255, 255])

    lower_blue = np.array([90,60,50],np.uint8)
    upper_blue = np.array([121,255,255],np.uint8)

    maskblue = cv2.inRange(hsv, lower_blue, upper_blue)
    maskred = cv2.inRange(hsv,lower_red,upper_red)
    maskorange = cv2.inRange(hsv, lower_orange, upper_orange)


    contours_blue= cv2.findContours(maskblue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_blue = imutils.grab_contours(contours_blue)
    for contour in contours_blue:
        area = cv2.contourArea(contour)
        cv2.drawContours(frame, contour, -1, (0, 255, 0), 2)

    contours_red = cv2.findContours(maskred, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_red = imutils.grab_contours(contours_red)
    for contourz in contours_red:
        area = cv2.contourArea(contourz)
        cv2.drawContours(frame, contourz, -1, (0, 255, 0), 2)

    contours_orange = cv2.findContours(maskorange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_orange = imutils.grab_contours(contours_orange)
    for contourf in contours_orange:
        area = cv2.contourArea(contourf)
        cv2.drawContours(frame, contourf, -1, (0, 255, 0), 2)

    cv2.imshow("maskblue", maskblue)
    cv2.imshow("maskred", maskred)
    cv2.imshow("maskorange", maskorange)

    cv2.imshow('img', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
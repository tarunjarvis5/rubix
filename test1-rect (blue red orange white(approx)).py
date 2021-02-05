import kociemba
import numpy as np
import requests
#print(kociemba.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD'))
import cv2
import imutils

#cap = cv2.VideoCapture(0)
URL = "http://192.168.29.190:8080/shot.jpg"

while True:
    img_res = requests.get(URL)
    img_array = np.array(bytearray(img_res.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)

    img = imutils.resize(img, width=800)


    #_,frame = cap.read()
    blur = cv2.GaussianBlur(img,(5, 5), 0)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower_white = np.array([0, 0, 100],np.uint8)
    upper_white = np.array([0, 0, 255],np.uint8)

    lower_red = np.array([0, 100, 50], np.uint8)
    upper_red = np.array([5, 255, 255],np.uint8)

    lower_orange = np.array([10, 100, 50], np.uint8)
    upper_orange = np.array([25, 255, 255], np.uint8)


    lower_blue = np.array([90,60,50],np.uint8)
    upper_blue = np.array([121,255,255],np.uint8)

    maskblue = cv2.inRange(hsv, lower_blue, upper_blue)
    maskred = cv2.inRange(hsv,lower_red,upper_red)
    maskorange = cv2.inRange(hsv, lower_orange, upper_orange)
    maskwhite = cv2.inRange(hsv, lower_white, upper_white)

    contours_blue= cv2.findContours(maskblue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_blue = imutils.grab_contours(contours_blue)
    for contour in contours_blue:
        area = cv2.contourArea(contour)
        if area > 6000:
            cv2.drawContours(img, contour, -1, (0, 255, 0), 2)
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    contours_red = cv2.findContours(maskred, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_red = imutils.grab_contours(contours_red)
    for contour in contours_red:
        area = cv2.contourArea(contour)
        if area > 6000:
            cv2.drawContours(img, contour, -1, (0, 255, 0), 2)
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    contours_orange = cv2.findContours(maskorange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_orange = imutils.grab_contours(contours_orange)
    for contour in contours_orange:
        area = cv2.contourArea(contour)
        if area > 6000:
            cv2.drawContours(img, contour, -1, (0, 255, 0), 2)
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


    contours_white = cv2.findContours(maskwhite, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_white = imutils.grab_contours(contours_white)
    for contour in contours_white:
        area = cv2.contourArea(contour)
        if area > 5000:
            cv2.drawContours(img, contour, -1, (0, 255, 0), 2)
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


    cv2.imshow("maskblue", maskblue)
    cv2.imshow("maskred", maskred)
    cv2.imshow("maskorange", maskorange)
    cv2.imshow("maskwhite", maskwhite)
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
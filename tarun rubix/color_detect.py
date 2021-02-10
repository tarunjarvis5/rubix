
import numpy as np
import cv2
import imutils
###################
# cx is column and cy is row
###################
def detect_color(img,hsv):

    lst = []

    lower_white = np.array([0, 0, 60],np.uint8)
    upper_white = np.array([0, 0, 255],np.uint8)

    lower_red = np.array([0, 100, 50], np.uint8)
    upper_red = np.array([5, 255, 255],np.uint8)

    lower_orange = np.array([10, 100, 100], np.uint8)
    upper_orange = np.array([25, 255, 255], np.uint8)

    lower_blue = np.array([90,60,100],np.uint8)
    upper_blue = np.array([121,255,255],np.uint8)

    maskblue = cv2.inRange(hsv, lower_blue, upper_blue)
    maskred = cv2.inRange(hsv,lower_red,upper_red)
    maskorange = cv2.inRange(hsv, lower_orange, upper_orange)
    maskwhite = cv2.inRange(hsv, lower_white, upper_white)

    contours_blue= cv2.findContours(maskblue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_blue = imutils.grab_contours(contours_blue)
    for contour in contours_blue:
        area = cv2.contourArea(contour)
        if area > 5000 :
            f = cv2.drawContours(img, contour, -1, (0, 255, 0), 2)
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            center = (x, y)
            x1 = w / 2
            y1 = h / 2
            cx = x + x1
            cy = y + y1
            cv2.circle(img, (int(cx), int(cy)), 2, (0, 0, 255), -1)
            text = str(int(cx))+","+str(int(cy))
            cv2.putText(img, text, (int(cx), int(cy)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
            cv2.putText(img, "BLUE", (int(cx), int(y) + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 29, 206), 2)
            if len(lst) != 9 :
                if cx not in lst :
                    if cy not in lst :
                        lst.append(["Blue",cx,cy])

    contours_red = cv2.findContours(maskred, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_red = imutils.grab_contours(contours_red)
    for contour in contours_red:
        area = cv2.contourArea(contour)
        if area > 5000:
            cv2.drawContours(img, contour, -1, (0, 255, 0), 2)
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            x1 = w / 2
            y1 = h / 2
            cx = x + x1
            cy = y + y1
            cv2.circle(img, (int(cx), int(cy)), 2, (0, 0, 255), -1)
            text = str(int(cx))+","+str(int(cy))
            cv2.putText(img, text, (int(cx), int(cy)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
            cv2.putText(img, "RED", (int(cx), int(y) + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 29, 206), 2)
            if len(lst) != 9:
                if cx not in lst:
                    if cy not in lst:
                        lst.append(["Red", cx, cy])

    contours_orange = cv2.findContours(maskorange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_orange = imutils.grab_contours(contours_orange)
    for contour in contours_orange:
        area = cv2.contourArea(contour)
        if area > 5000:
            cv2.drawContours(img, contour, -1, (0, 255, 0), 2)
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            x1 = w / 2
            y1 = h / 2
            cx = x + x1
            cy = y + y1
            cv2.circle(img, (int(cx), int(cy)), 2, (0, 0, 255), -1)
            text = str(int(cx))+","+str(int(cy))
            cv2.putText(img, text, (int(cx), int(cy)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
            cv2.putText(img, "ORANGE", (int(cx), int(y)+h-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 29, 206), 2)
            if len(lst) != 9:
                if cx not in lst:
                    if cy not in lst:
                        lst.append(["Orange", cx, cy])

    contours_white = cv2.findContours(maskwhite, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_white = imutils.grab_contours(contours_white)
    for contour in contours_white:
        area = cv2.contourArea(contour)
        if area > 5000:
            cv2.drawContours(img, contour, -1, (0, 255, 0), 2)
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            x1 = w / 2
            y1 = h / 2
            cx = x + x1
            cy = y + y1
            cv2.circle(img, (int(cx), int(cy)), 2, (0, 0, 255), -1)
            text = str(int(cx)) + "," + str(int(cy))
            cv2.putText(img, text, (int(cx), int(cy)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
            cv2.putText(img, "WHITE", (int(cx), int(y) + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 29, 206), 2)
            if len(lst) != 9:
                if cx not in lst:
                    if cy not in lst:
                        lst.append(["White", cx, cy])

    lst.sort(key=lambda x: x[2])  # sorting accoring to row i.e y-axis
    #print(lst)
    return lst

    #cv2.imshow("maskblue", maskblue)
    #cv2.imshow("maskred", maskred)
    #cv2.imshow("maskorange", maskorange)
    #cv2.imshow("maskwhite", maskwhite)
    #cv2.imshow('img', img)

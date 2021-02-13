import numpy as np
import requests
import cv2
import imutils



def beta(inst):

    URL = "http://192.168.29.190:8080/shot.jpg"

    lower_black = np.array([0, 0, 0], np.uint8)
    upper_black = np.array([255, 90, 75], np.uint8)

    while True:

        img_res = requests.get(URL)
        img_array = np.array(bytearray(img_res.content), dtype=np.uint8)
        img = cv2.imdecode(img_array, -1)

        img = imutils.resize(img, width=800)

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        maskblack = cv2.inRange(hsv, lower_black, upper_black)

        cv2.putText(img, inst, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

        contours_black = cv2.findContours(maskblack, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours_black = imutils.grab_contours(contours_black)
        for contour in contours_black:
            area = cv2.contourArea(contour)
            if area > 12000:
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                x1 = w / 2
                y1 = h / 2
                cx = x + x1
                cy = y + y1
                cv2.circle(img, (int(cx), int(cy)), 2, (0, 0, 255), -1)
                text = str(int(cx)) + "," + str(int(cy))
                cv2.putText(img, text, (int(cx), int(cy)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

                # To display arrows

                if inst == "R" :
                    cv2.arrowedLine(img, ((x + w) - 50, (y + h) - 50), ((x + w) - 50, (y) + 50), (255, 0, 247), 4, tipLength=0.1)
                elif inst == "R2" :
                    cv2.arrowedLine(img, ((x + w) - 50, (y + h) - 50), ((x + w) - 50, (y) + 50), (255, 0, 247), 4, tipLength=0.1)
                    cv2.putText(img, "2", (int(x+w)-40,int(cy)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 247), 4)
                elif inst == "R'" :
                    cv2.arrowedLine(img, ((x + w) - 50, (y) + 50), ((x + w) - 50, (y + h) - 50), (255, 0, 247), 4, tipLength=0.1)
                elif inst == "U" :
                    cv2.arrowedLine(img, ((x + w) - 50, (y) + 50), ((x) + 50, (y) + 50), (255, 0, 247), 4, tipLength=0.1)
                elif inst == "U2" :
                    cv2.arrowedLine(img, ((x + w) - 50, (y) + 50), ((x) + 50, (y) + 50), (255, 0, 247), 4, tipLength=0.1)
                    cv2.putText(img, "2", (int(cx), int(y)+40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 247), 4)
                elif inst == "U'" :
                    cv2.arrowedLine(img, ((x) + 50, (y) + 50), ((x + w) - 50, (y) + 50), (255, 0, 247), 4,tipLength=0.1)
                elif inst == "L" :
                    cv2.arrowedLine(img, ((x) + 50, (y) + 50), ((x) + 50, (y + h) - 50), (255, 0, 247), 4,tipLength=0.1)
                elif inst == "L2" :
                    cv2.arrowedLine(img, ((x) + 50, (y) + 50), ((x) + 50, (y + h) - 50), (255, 0, 247), 4,tipLength=0.1)
                    cv2.putText(img, "2", (int(x)+ 20, int(cy)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 247), 4)
                elif inst == "L'" :
                    cv2.arrowedLine(img, ((x) + 50, (y + h) - 50), ((x) + 50, (y) + 50), (255, 0, 247), 4,tipLength=0.1)
                elif inst == "D" :
                    cv2.arrowedLine(img, ((x) + 50, (y+h) - 50) , ((x + w) - 50, (y+h) -50 ), (255, 0, 247), 4, tipLength=0.1)
                elif inst == "D2" :
                    cv2.arrowedLine(img, ((x) + 50, (y+h) - 50) , ((x + w) - 50, (y+h) -50 ), (255, 0, 247), 4, tipLength=0.1)
                    cv2.putText(img, "2", (int(cx), int(y+h) - 70 ), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 247), 4)
                elif inst == "D'" :
                    cv2.arrowedLine(img, ((x + w) - 50, (y+h) -50 ) , ((x) + 50, (y+h) - 50), (255, 0, 247), 4, tipLength=0.1)
                elif  inst == "F'" :
                    cv2.arrowedLine(img, (int(x+w) - 50, int(cy) ) , (int(cx), (y) + 50 ), (255, 0, 247), 4, tipLength=0.1)
                    cv2.arrowedLine(img, (int(cx), (y) + 50 ) , (int(x) + 50 , int(cy)  ), (255, 0, 247), 4, tipLength=0.1)
                    cv2.arrowedLine(img, (int(x) + 50 , int(cy)) , (int(cx) , int(y+h) -50 ), (255, 0, 247), 4, tipLength=0.1)
                    cv2.arrowedLine(img, (int(cx) , int(y+h) -50 ) ,(int(x+w) - 50, int(cy) ), (255, 0, 247), 4, tipLength=0.1)
                elif  inst == "F2" :
                    cv2.arrowedLine(img, (int(cx), (y) + 50 ), (int(x+w) - 50, int(cy) ), (255, 0, 247), 4,tipLength=0.1)
                    cv2.arrowedLine(img, (int(x) + 50 , int(cy)), (int(cx), (y) + 50 ), (255, 0, 247), 4, tipLength=0.1)
                    cv2.arrowedLine(img, (int(cx) , int(y+h) -50 ), (int(x) + 50 , int(cy)), (255, 0, 247), 4,tipLength=0.1)
                    cv2.arrowedLine(img, (int(x+w) - 50, int(cy) ), (int(cx) , int(y+h) - 50 ), (255, 0, 247), 4,tipLength=0.1)
                    cv2.putText(img, "2", (int(cx)+20, (y) + 40 ), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 247), 4)
                elif inst == "F" :
                    cv2.arrowedLine(img, (int(cx), (y) + 50 ), (int(x+w) - 50, int(cy) ), (255, 0, 247), 4,tipLength=0.1)
                    cv2.arrowedLine(img, (int(x) + 50 , int(cy)), (int(cx), (y) + 50 ), (255, 0, 247), 4, tipLength=0.1)
                    cv2.arrowedLine(img, (int(cx) , int(y+h) -50 ), (int(x) + 50 , int(cy)), (255, 0, 247), 4,tipLength=0.1)
                    cv2.arrowedLine(img, (int(x+w) - 50, int(cy) ), (int(cx) , int(y+h) - 50 ), (255, 0, 247), 4,tipLength=0.1)
                elif  inst == "B" :
                    cv2.arrowedLine(img, (int(x+w) - 50, int(cy) ) , (int(cx), (y) + 50 ), (255, 0, 247), 4, tipLength=0.1)
                    cv2.arrowedLine(img, (int(cx), (y) + 50 ) , (int(x) + 50 , int(cy)  ), (255, 0, 247), 4, tipLength=0.1)
                    cv2.arrowedLine(img, (int(x) + 50 , int(cy)) , (int(cx) , int(y+h) -50 ), (255, 0, 247), 4, tipLength=0.1)
                    cv2.arrowedLine(img, (int(cx) , int(y+h) -50 ) ,(int(x+w) - 50, int(cy) ), (255, 0, 247), 4, tipLength=0.1)
                    cv2.putText(img, "BACK", (int(cx)-70, int(cy)), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 247), 4)
                elif  inst == "B2" :
                    cv2.arrowedLine(img, (int(x+w) - 50, int(cy) ) , (int(cx), (y) + 50 ), (255, 0, 247), 4, tipLength=0.1)
                    cv2.arrowedLine(img, (int(cx), (y) + 50 ) , (int(x) + 50 , int(cy)  ), (255, 0, 247), 4, tipLength=0.1)
                    cv2.arrowedLine(img, (int(x) + 50 , int(cy)) , (int(cx) , int(y+h) -50 ), (255, 0, 247), 4, tipLength=0.1)
                    cv2.arrowedLine(img, (int(cx) , int(y+h) -50 ) ,(int(x+w) - 50, int(cy) ), (255, 0, 247), 4, tipLength=0.1)
                    cv2.putText(img, "BACK", (int(cx)-70, int(cy)), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 247), 4)
                    cv2.putText(img, "2", (int(cx)+20, (y) + 40 ), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 247), 4)
                elif inst == "B'" :
                    cv2.arrowedLine(img, (int(cx), (y) + 50 ), (int(x+w) - 50, int(cy) ), (255, 0, 247), 4,tipLength=0.1)
                    cv2.arrowedLine(img, (int(x) + 50 , int(cy)), (int(cx), (y) + 50 ), (255, 0, 247), 4, tipLength=0.1)
                    cv2.arrowedLine(img, (int(cx) , int(y+h) -50 ), (int(x) + 50 , int(cy)), (255, 0, 247), 4,tipLength=0.1)
                    cv2.arrowedLine(img, (int(x+w) - 50, int(cy) ), (int(cx) , int(y+h) - 50 ), (255, 0, 247), 4,tipLength=0.1)
                    cv2.putText(img, "BACK", (int(cx)-70, int(cy)), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 247), 4)


        cv2.putText(img, "Press \"n\" for next", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('img',img)

        k = cv2.waitKey(1) & 0xff
        if k == 27:
            return None

def alpha(instruction):

    for inst in instruction:
        beta(inst)



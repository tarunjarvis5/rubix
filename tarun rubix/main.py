import kociemba
import numpy as np
import requests
#print(kociemba.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD'))
import cv2
import imutils
import color_detect
import rubix_engine

def main():

    # cap = cv2.VideoCapture(0)  # To use computer-webcam
    URL = "http://192.168.29.190:8080/shot.jpg"

    while True:
        img_res = requests.get(URL)
        img_array = np.array(bytearray(img_res.content), dtype=np.uint8)
        img = cv2.imdecode(img_array, -1)

        img = imutils.resize(img, width=800)

        # _,frame = cap.read() # we dont use this because i am using IPCAMERA which uses numpyarray

        blur = cv2.GaussianBlur(img, (5, 5), 0)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        #color_detect.detect_color(img, hsv)
        cv2.putText(img, "This is Rubix", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(img, "Press \"s\" to start", (100,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('img', img)

        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
        elif k == 115:
            rubix_engine.main()
            break


    cv2.destroyAllWindows()

main()
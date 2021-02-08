import kociemba
import numpy as np
import requests
#print(kociemba.solve('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD'))
import cv2
import imutils
import color_detect

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

        color_detect.detect_color(img, hsv)

        cv2.imshow('img', img)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cv2.destroyAllWindows()

main()
import numpy as np
import requests
import cv2
import imutils
import color_detect


def engine(side):
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
        if side == "front":
            cv2.putText(img, "Detecting Front Face", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(img, "\"n\" for next face", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            color_detect.detect_color(img, hsv)

        elif side == "right":
            cv2.putText(img, "Detecting Right Face", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(img, "\"n\" for next face", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            color_detect.detect_color(img, hsv)

        elif side == "back":
            cv2.putText(img, "Detecting Back Face", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(img, "\"n\" for next face", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            color_detect.detect_color(img, hsv)

        elif side == "left":
            cv2.putText(img, "Detecting Left Face", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(img, "\"n\" for next face", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            color_detect.detect_color(img, hsv)

        elif side == "upper":
            cv2.putText(img, "Detecting Upper Face", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(img, "\"n\" for next face", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            color_detect.detect_color(img, hsv)

        elif side == "bottom":
            cv2.putText(img, "Detecting Bottom Face", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(img, "\"n\" for next face", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            color_detect.detect_color(img, hsv)

        cv2.imshow('img', img)

        k = cv2.waitKey(1) & 0xff
        if k == 110 :
            break

    cv2.destroyAllWindows()

def main():

    lstfront = []
    lstback = []
    lstright = []
    lstleft = []
    lstup = []
    lstbot = []

    if len(lstfront) == 0 :
        side = "front"
        lstfront = engine(side)

    if len(lstright) == 0 :
        side = "right"
        lstfront = engine(side)

    if len(lstback) == 0:
        side = "back"
        lstfront = engine(side)

    if len(lstleft) == 0:
        side = "left"
        lstfront = engine(side)

    if len(lstup) == 0:
        side = "upper"
        lstfront = engine(side)

    if len(lstbot) == 0:
        side = "bottom"
        lstfront = engine(side)

import numpy as np
import requests
import cv2
import imutils
import color_detect


def engine(side):

    URL = "http://your-ipcamera-address/shot.jpg"


    while True:
        img_res = requests.get(URL)
        img_array = np.array(bytearray(img_res.content), dtype=np.uint8)
        img = cv2.imdecode(img_array, -1)

        img = imutils.resize(img, width=800)

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lst = []

        if side == "front":
            cv2.putText(img, "Detecting Front Face", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(img, "\"n\" for next face", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            lst = color_detect.detect_color(img, hsv)

        elif side == "right":
            cv2.putText(img, "Detecting Right Face", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(img, "\"n\" for next face", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            lst = color_detect.detect_color(img, hsv)

        elif side == "back":
            cv2.putText(img, "Detecting Back Face", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(img, "\"n\" for next face", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            lst = color_detect.detect_color(img, hsv)

        elif side == "left":
            cv2.putText(img, "Detecting Left Face", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(img, "\"n\" for next face", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            lst = color_detect.detect_color(img, hsv)

        elif side == "upper":
            cv2.putText(img, "Detecting Upper Face", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(img, "\"n\" for next face", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            lst = color_detect.detect_color(img, hsv)

        elif side == "bottom":
            cv2.putText(img, "Detecting Bottom Face", (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(img, "\"n\" for next face", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            lst = color_detect.detect_color(img, hsv)

        cv2.imshow('img', img)

        k = cv2.waitKey(1) & 0xff
        if k == 110 :
            return lst


def main():

    lstfront = []
    lstback = []
    lstright = []
    lstleft = []
    lstup = []
    lstbot = []
    stfront = ""
    stright = ""
    stleft = ""
    stbot = ""
    stup = ""
    stback = ""

    if len(lstfront) == 0 :
        side = "front"
        lstfront = engine(side)
        lstrow = lstfront[:3]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stfront+=(i[0][0])
        lstrow = lstfront[3:6]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stfront+=(i[0][0])
        lstrow = lstfront[6:9]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stfront+=(i[0][0])


    if len(lstright) == 0 :
        side = "right"
        lstright = engine(side)
        lstrow = lstright[:3]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stright += (i[0][0])
        lstrow = lstright[3:6]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stright += (i[0][0])
        lstrow = lstright[6:9]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stright += (i[0][0])


    if len(lstback) == 0:
        side = "back"
        lstback = engine(side)
        lstrow = lstback[:3]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stback += (i[0][0])
        lstrow = lstback[3:6]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stback += (i[0][0])
        lstrow = lstback[6:9]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stback += (i[0][0])


    if len(lstleft) == 0:
        side = "left"
        lstleft = engine(side)
        lstrow = lstleft[:3]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stleft += (i[0][0])
        lstrow = lstleft[3:6]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stleft += (i[0][0])
        lstrow = lstleft[6:9]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stleft += (i[0][0])


    if len(lstup) == 0:
        side = "upper"
        lstup = engine(side)
        lstrow = lstup[:3]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stup += (i[0][0])
        lstrow = lstup[3:6]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stup += (i[0][0])
        lstrow = lstup[6:9]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stup += (i[0][0])


    if len(lstbot) == 0:
        side = "bottom"
        lstbot = engine(side)
        lstrow = lstbot[:3]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stbot += (i[0][0])
        lstrow = lstbot[3:6]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stbot += (i[0][0])
        lstrow = lstbot[6:9]
        lstrow.sort(key=lambda x: x[1])
        for i in lstrow:
            stbot += (i[0][0])

    # U = WHITE
    # R = RED
    # F = GREEN
    # D = YELLOW
    # L = ORANGE
    # B = BLUE
    #print(stup)
    #print(stright)
    #print(stfront)
    #print(stbot)
    #print(stleft)
    #print(stback)
    stfinal = stup+stright+stfront+stbot+stleft+stback

    stfinal = stfinal.replace("W", "U")
    stfinal = stfinal.replace("R", "R")
    stfinal = stfinal.replace("G", "F")
    stfinal = stfinal.replace("O", "L")
    stfinal = stfinal.replace("Y", "D")
    stfinal = stfinal.replace("B", "B")
    #print(stfinal)

    return stfinal


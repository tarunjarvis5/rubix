import kociemba
import numpy as np
import requests
import cv2
import imutils
import rubix_engine
import rubix_output

# point white center towards you and red center at top with green center to right face fo white

def main():

    # cap = cv2.VideoCapture(0)  # To use computer-webcam
    URL = "http://your-ipcamera-address/shot.jpg"

    while True:
        img_res = requests.get(URL)
        img_array = np.array(bytearray(img_res.content), dtype=np.uint8)
        img = cv2.imdecode(img_array, -1)

        img = imutils.resize(img, width=800)

        # _,frame = cap.read() # we dont use this because i am using IPCAMERA which uses numpyarray

        cv2.putText(img, "This is Rubix", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(img, "Press \"s\" to start", (100,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(img, "Press \"esc\" to stop", (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('img', img)
        instruction = []
        k = cv2.waitKey(1) & 0xff
        if k == 27:    # ascii value for "esc"
            break
        elif k == 115: # ascii value for "s"
            instrucst = rubix_engine.main()
            instruction = (kociemba.solve(instrucst)).split()
            rubix_output.alpha(instruction)

    cv2.destroyAllWindows()

main()
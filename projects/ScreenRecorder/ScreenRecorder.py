import time

import cv2
import numpy as np
import pyautogui

SCREEN_SIZE = (1920, 1080)  # screen size

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))  # format of video

fps = 144  # input your monitor fps
prev = 0

while True:
    time_elapsed = time.time_ns() - prev
    img = pyautogui.screenshot()
    if time_elapsed > 1.0 / fps:
        prev = time.time()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
    cv2.waitKey(10)  # increase this value makes video record faster, 10 is good for me

cv2.destroyAllWindows()
out.release()

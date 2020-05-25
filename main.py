import sys
import cv2
import numpy as np
import stream

def showVideo():
    url = stream.getMallStream("https://www.mall.tv/stavby-a-technologie/stavba-marianskeho-sloupu-na-staromestskem-namesti")

    c = cv2.VideoCapture(url)
    _,f = c.read()
 
    avg = np.float32(f)

    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

    while(1):
        _,f = c.read()
        
        cv2.accumulateWeighted(f,avg,0.002)
        res = cv2.convertScaleAbs(avg)

        k = cv2.waitKey(20)
        if k == 27: # ESC
            sys.exit()
        if k == 105: # i
            cv2.imshow('window',f)
        else:
            cv2.imshow('window',res)

while True:
    try:
        showVideo()
    except Exception as e:
        print(e)

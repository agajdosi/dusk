import sys, random
import cv2
import numpy as np
import stream

places = (
    ("http://213.157.112.2/ipcam/mjpeg.cgi", 0.01, "mall in Hungaria"),
    ("http://213.157.112.2:8081/video2.mjpg", 0.01, "mall in Hungaria another view"),
    (stream.getMallStream("https://www.mall.tv/stavby-a-technologie/stavba-marianskeho-sloupu-na-staromestskem-namesti"), 0.002, "mariansky sloup v Praze"),
    (stream.getMallStream("https://www.mall.tv/slowtv-spolecnost-a-kultura/volny-pohyb-v-centru-prahy"), 0.002, "ulice v Praze"),
    ("https://videos-3.earthcam.com/fecnetwork/9974.flv/chunklist_w1936389804.m3u8", 0.002, "times square z ulice")
)

url = places[0][0]
speed = places[0][1]

def showVideo():
    global url, speed
    c = cv2.VideoCapture(url)
    _,f = c.read()
 
    avg = np.float32(f)

    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

    while(1):
        k = cv2.waitKey(20)
        if k == 27: # ESC
            sys.exit()

        _,f = c.read()
        
        cv2.accumulateWeighted(f, avg, speed)
        res = cv2.convertScaleAbs(avg)

        if k == 105: # i
            cv2.imshow('window',f)

        # this is so ugly, please forgive me
        elif k == 49:
            url = places[0][0]
            speed = places[0][1]
            c = cv2.VideoCapture(url)
        elif k == 50:
            url = places[1][0]
            speed = places[1][1]
            c = cv2.VideoCapture(url)
        elif k == 51:
            url = places[2][0]
            speed = places[2][1]
            c = cv2.VideoCapture(url)
        elif k == 52:
            url = places[3][0]
            speed = places[3][1]
            c = cv2.VideoCapture(url)
        elif k == 53:
            url = places[4][0]
            speed = places[4][1]
            c = cv2.VideoCapture(url)
        # will fix it soon, my eyes can't handle it

        else:
            cv2.imshow('window',res)

while True:
    try:
        showVideo()
    except Exception as e:
        print(e)

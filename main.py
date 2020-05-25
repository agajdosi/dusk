import sys, random
import cv2
import numpy as np
import stream, places

places = [
    "http://213.157.112.2/ipcam/mjpeg.cgi", # mall in Hungarie
    "http://213.157.112.2:8081/video2.mjpg", # mall in Hungaria another view
    stream.getMallStream("https://www.mall.tv/stavby-a-technologie/stavba-marianskeho-sloupu-na-staromestskem-namesti"), # mariansky sloup v Praze
    stream.getMallStream("https://www.mall.tv/slowtv-spolecnost-a-kultura/volny-pohyb-v-centru-prahy"), # ulice v Praze
    "https://videos-3.earthcam.com/fecnetwork/9974.flv/chunklist_w1936389804.m3u8", # times square z ulice 
]

url = places[0]
avg = None

def showVideo():
    global url
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
        elif k == 105: # i
            cv2.imshow('window',f)

        # this is so ugly, please forgive me
        elif k == 49:
            url = places[0]
            c = cv2.VideoCapture(url)
        elif k == 50:
            url = places[1]
            c = cv2.VideoCapture(url)
        elif k == 51:
            url = places[2]
            c = cv2.VideoCapture(url)
        elif k == 52:
            url = places[3]
            c = cv2.VideoCapture(url)
        elif k == 53:
            url = places[4]
            c = cv2.VideoCapture(url)
        # will fix it soon, my eyes can't handle it

        else:
            cv2.imshow('window',res)

while True:
    try:
        showVideo()
    except Exception as e:
        print(e)

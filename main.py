import sys, random, argparse
import cv2
import numpy as np
import stream

places = (
    ("1.m4v", 0.01, "Palladium 1"),
    ("2.m4v", 0.01, "Palladium 2"),
    #("http://93.90.222.23:7547/", 0.01, "something"),
    #("http://213.157.112.2/ipcam/mjpeg.cgi", 0.01, "mall in Hungaria"),
    #("http://213.157.112.2:8081/video2.mjpg", 0.01, "mall in Hungaria another view"),
    #(stream.getMallStream("https://www.mall.tv/slowtv-spolecnost-a-kultura/volny-pohyb-v-centru-prahy"), 0.002, "ulice v Praze"),
    #("https://videos-3.earthcam.com/fecnetwork/9974.flv/chunklist_w1936389804.m3u8", 0.002, "times square z ulice")
)

url = places[0][0]
speed = places[0][1]

parser = argparse.ArgumentParser()
parser.add_argument("--original", "-o", help="Select whether original image should be shown. Default false: only edited image will be shown. If true: edited and original images will be shown.", type=bool, default=False)
parser.add_argument("--xmove", "-x", help="Horizontal offset for edited image. Positive numbers move it to the right.", type=int, default=0)
parser.add_argument("--ymove", "-y", help="Vertical offset for edited image. Positive numbers move it down.", type=int, default=0)
parser.add_argument("--xmove2", "-x2", help="Horizontal offset for original image. Positive numbers move it to the right. Default: 2600.", type=int, default=2600)
parser.add_argument("--ymove2", "-y2", help="Vertical offset for original image. Positive numbers move it down.", type=int, default=0)

args = parser.parse_args()

def showVideo():
    global url, speed
    c = cv2.VideoCapture(url)
    _,f = c.read()
 
    avg = np.float32(f)

    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.moveWindow("window", args.xmove, args.ymove)

    if args.original == True:
        cv2.namedWindow("window2", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window2",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.moveWindow("window2", args.xmove2, args.ymove2)

    while(1):
        k = cv2.waitKey(20)
        if k == 27: # ESC
            sys.exit()

        _, f = c.read()
        
        cv2.accumulateWeighted(f, avg, speed)
        res = cv2.convertScaleAbs(avg)

        if k == 105: # i
            cv2.imshow('window', f)

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
            cv2.imshow('window', res)

        if args.original == True:
            cv2.imshow('window2', f)

while True:
    try:
        showVideo()
    except Exception as e:
        print(e)

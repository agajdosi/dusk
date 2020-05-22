import cv2
import numpy as np
import pafy



#url = 'https://www.youtube.com/watch?v=yoLlXu0AmxA' # BRNO
url = 'https://www.youtube.com/watch?v=mRe-514tGMg' # time square
#url = 'https://www.youtube.com/watch?v=0uA1tv6MFB0' #bryant park
vPafy = pafy.new(url)
play = vPafy.getbest(preftype="webm",ftypestrict=False)
url = play.url

url = "https://kadare.gjirafa.com/live/dCynrjRK8sEsrYu0zDtDg8l4KaXbFpXl/tkx00z1080/index.m3u8" #staromak
#url = "https://prishtine.gjirafa.com/live/dCynrjRK8sEsrYu0zDtDg8l4KaXbFpXl/t00g1y1080/index.m3u8" # ulice v praze

c = cv2.VideoCapture(url) # ulice v praze
#c = cv2.VideoCapture(0)

_,f = c.read()
 
avg = np.float32(f)
 
while(1):
    _,f = c.read()
     
    cv2.accumulateWeighted(f,avg,0.002)

    res = cv2.convertScaleAbs(avg)

    cv2.imshow('img',f)
    cv2.imshow('avg1',res)

    k = cv2.waitKey(20)
    if k == 27:
        break

cv2.destroyAllWindows()
c.release()

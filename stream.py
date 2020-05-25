import re, random

import pafy
import requests
from bs4 import BeautifulSoup

YTVideos = {
        'brno': 'https://www.youtube.com/watch?v=yoLlXu0AmxA',
        'time square': 'https://www.youtube.com/watch?v=mRe-514tGMg',
        'bryant park': 'https://www.youtube.com/watch?v=0uA1tv6MFB0'
    }

MallVideos = {
    "staromak": "https://www.mall.tv/stavby-a-technologie/stavba-marianskeho-sloupu-na-staromestskem-namesti",
    "praha": "https://www.mall.tv/slowtv-spolecnost-a-kultura/volny-pohyb-v-centru-prahy"
}

def getYTStream(url: str) -> str:
    """
    Gets stream's URL of YouTube video.
    """
    vPafy = pafy.new(url)
    play = vPafy.getbest(preftype="webm",ftypestrict=False)
    return play.url

def getMallStream(url: str, quality="1080") -> str:
    """
    Gets stream's URL of video on Mall TV.
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    meta = soup.find("meta", {"name": "twitter:image"})


    match = re.match(r"https?:\/\/(.+)\/live\/(.+)\/(.+)-retina\.jpg", meta["content"])
    server = match[1]
    token = match[2]
    qualityPreString = match[3]

    url = "https://" + server + "/live/" + token + "/" + qualityPreString + str(quality) + "/index.m3u8"
    return url

def getRandomYTStream():
    video = random.choice(list(YTVideos.values()))
    return getYTStream(video)

def getRandomMallStream():
    video = random.choice(list(YTVideos.values()))
    return getMallStream(video)

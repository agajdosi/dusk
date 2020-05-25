import re, random

import pafy
import requests
from bs4 import BeautifulSoup

def getYTStream(url: str) -> str:
    """
    Gets stream's URL of YouTube video.
    """
    vPafy = pafy.new(url)
    play = vPafy.getbest(preftype="webm",ftypestrict=False)
    return play.url

# make a module from this!
# or PR it into some existing module like Pafy
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

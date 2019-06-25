from bs4 import BeautifulSoup
import urllib.request
import re

def extractURL(card):
   url = card.find("img")
   return url.get("data-src")

basePage = 'https://www.discogs.com/search/?sort=have%2Cdesc&format_exact=Album&layout=med&style_exact='

urlSuffix = '&type=all'

subGenre = 'Heavy+Metal'

pageNumStr = "&page=20000000"

pageURL = basePage + subGenre + urlSuffix + pageNumStr

genreList = [
    "Heavy Metal",
    "Black Metal",
    "Death Metal",
    "Thrash",
    "Doom Metal",
    "Grindcore",
    "Nu Metal",
    "Metalcore",
    "Power Metal",
    "Progressive Metal",
    "Folk Metal",
    "Post-Metal"]

for genre in genreList:
    endOfResults = False
    while(!endOfResults):
        try: 
            page = urllib.request.urlopen(pageURL)

            soup = BeautifulSoup(page,'html.parser')

            albumPics = soup.find_all("div",{"class":"card_image"})

            imgURL = str(extractURL(albumPics[0]))
            print(imgURL)

        except urllib.error.HTTPError as e:

            if e.code == 404:
                print("shit dont exist")
                endOfResults = True

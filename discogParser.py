from bs4 import BeautifulSoup
import urllib.request
import re

def extractURL(card):
   url = card.find("img")
   return url.get("data-src")

basePage = 'https://www.discogs.com/search/?sort=have%2Cdesc&format_exact=Album&layout=med&style_exact='
urlSuffix = '&type=all'

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
    pageNum = 1

    if ' ' in genre:
        genreURL = genre.replace(' ','+')

    while(!endOfResults):
        if pageNum > 1:
            pageNumStr = "&page=" + str(pageNum)
        else:
            pageNumStr = ""

        pageURL = basePage + genreURL + urlSuffix + pageNumStr

        try: 
            page = urllib.request.urlopen(pageURL)
            soup = BeautifulSoup(page,'html.parser')

            albumPics = soup.find_all("div",{"class":"card_image"})

            fileNum = 0
            for entry in albumPics:
                imgURL = str(extractURL(entry))
                fileName = "./" + genreURL + str(fileNum)
                urllib.request.urlretrieve(imgURL,fileName)
                fileNum = fileNum + 1

            pageNum = pageNum + 1

        except urllib.error.HTTPError as e:

            if e.code == 404:
                print("page does not exist")
                endOfResults = True

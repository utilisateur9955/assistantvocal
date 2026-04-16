import os
import tldextract #pip install tldextract

def test() :
    os.startfile("E:\BOB") #ouvrir un dossier
    os.startfile("output.mp3") #ouvrir un fichier
    os.startfile("https://youtube.com") #ouvrir un site web

def open(path):
    if tldextract.extract(path).suffix:
        url = "https://" + path
        os.startfile(url)
    else :
        googlesearch = "https://www.google.com/search?q=" + path
        os.startfile(googlesearch)

open("youtube.com")
open("wikipedia chien")
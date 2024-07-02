import requests
from bs4 import BeautifulSoup

#
with open("index.html") as fb:
    soup=BeautifulSoup(fb.text,"html parser")
    heading =soup.find('h1')
    paragraph =soup.find('p')    
    tag =soup.find("a")
    
    
    url =tag('href')
    print(heading)
        
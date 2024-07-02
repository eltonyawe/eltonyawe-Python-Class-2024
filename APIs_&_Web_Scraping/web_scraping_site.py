from bs4 import BeautifulSoup
import requests
#Retrieving/ colleting data from the site to scrape
page_to_scrape = requests.get('https://example.com')

#Parsing the html content
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
#Extracting and printing content from the site
title = soup.find("title",attrs={"class":"........."})
heading1 = soup.find("h1",attrs={"class":"........."})
paragraph = soup.findAll("p",attrs={"class":"........"})

print(heading1)

from bs4 import BeautifulSoup
import requests


page_to_scrape = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
quotes = soup.findAll("span", attrs= {"class" : "text"})
quotes1 =soup.findAll("small", attrs= {"class" : "author"})
for quote in quotes:
    print(quote.text)
    
print("*****************************")   


for quote in quotes1:
    print(quote.text)
    
    
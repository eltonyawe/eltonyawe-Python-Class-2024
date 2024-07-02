import requests
from bs4 import BeautifulSoup
url = "http://dihfahsih.com/"
response =requests.get(url)
soup = BeautifulSoup(response.text,'html.pasrer')
title1 =soup.find('h1')
title2 =soup.find('h2')
title6 = soup.find('h6')
paragraph =soup.find('p')
print(f'Title1 : {title1}')
print(f'Title2  : {title1}')
print(f'Title6 : {title1}')
print(f'Paragraph : {paragraph}')
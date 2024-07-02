import requests
from bs4 import BeautifulSoup

url = "http://dihfahsih.com/"
response = requests.get(url,)

if response.status_code==200:
    soup=BeautifulSoup(response.text,'html.parser')
    heading1 =soup.find('h1')
    heading2 = soup.find('h2')
    heading6 =soup.find('h6')
    paragraph = soup.find('p')
    
    print(heading1)   
    print(heading6)
    print(paragraph)
    
    
    links =soup.find_all('a')
    for link  in links:
        href = link.get('href')
        text =href
        print(f"Link Text :{text} \nURL :{href}")
        
    else:
        print(f"Failed retrive web error :{response.status_code}")
        
        
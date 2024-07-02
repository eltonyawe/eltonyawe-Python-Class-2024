#How to GET an API
import requests 

#URL of the API & end point
url = "https://jsonplaceholder.typicode.com/posts"

#Making a GET request to  a server(rretriving or collecting data)
response = requests.get(url)

#Checking if the request was successful
if response.status_code == 200:
    #parse the json response
    data = response.json()
    print("Data submitted",data)
else:
    print("Failed to retrive")



#How to deal with secure APIs

import requests 

url = "https://dihfahsih.com/api/reviews-list-secured/"
token = "a847aa77929479dcf4ac15a3f5c71b28ea646771"
token_payload = {
    "Authorization" : f'Token {token}'
}
response = requests.get(url,headers=token_payload)

if response.status_code == 200:
    data = response.json()
    print(data[-1])
else:
    print("Failed to retrive")
    print("Status_cod :",response.status_code)   
    print("Response",response.text)     
    
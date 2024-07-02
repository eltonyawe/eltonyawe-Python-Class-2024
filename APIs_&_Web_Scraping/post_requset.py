#How to POST an API
import requests
#URL of the API & end point
url = "https://dihfahsih.com/api/review/"

#Data to be sent
data ={
    "first_name" : "Yawe",
    "last_name"  : "Elton",
    "relationship" : "Class mate",
    "compliment" : "Promising"
}

response = requests.post(url,json=data)
#Checking if the request was successful
if response.status_code==201:
       #parse the json response
    new_post=response.json()
    print("Data submited",new_post)
    
else:
    print("Failed to create a post")
    print("Status_cod :",response.status_code)   
    print("Response",response.text) 
    
    

#How to deal with a secure API 

import requests
url = "https://dihfahsih.com/api/review-secure-post/"

data ={
    "first_name" : "Tiyo",
    "last_name"  : "Isaac",
    "relationship" : "Teammate",
    "compliment" : "Testing API call"
}
token = "a847aa77929479dcf4ac15a3f5c71b28ea646771"
token_payload = {
    "Authorization" : f'Token {token}'
}

response = requests.post(url,json=data,headers=token_payload)
if response.status_code==201:
    new_post=response.json()
    print("Data submited",new_post)
    
else:
    print("Failed to create a post")
    print("Status_cod :",response.status_code)   
    print("Response",response.text)     
    

#Data Science and Analysis
import pandas as pd
import numpy as np
import json

#Loading/Reading a a csv using pandas 
band_df = pd.read_csv ('Datasets/band-csv.csv')


#Loading/Reading a json file as in file handling
with open('Datasets/users.json') as file:
    user_data = json.load(file)
users_df = pd.json_normalize(user_data)
    
    
#lOading each file displaying the description of the head() function
print('Band DataFrame using a head in bulit function (showing few rows of data)')
print(band_df.head()) 
print('User DataFrame using a head in bulit function (showing few rows of data)')
print(users_df.head())  



#lOading each file displaying the description of describe() function 
print('Band DataFrame using a describe in bulit function(showing the summary of the DataFrame)')
print(band_df.describe())
print('User DataFrame using a describe in bulit function(showing the summary of the DataFrame)')
print(users_df.describe())     

#Finding whether there are some missing data for data cleaning
print(band_df.isnull())

#Finding missing data & adding it together soas to know thw the exact number of missing items /data
print(band_df.isnull().sum())



#Converting string columns as intergers
band_df.fillna({
    'year' : '2026',
    'Industry_name_NZSIOC' : 'Undefined Industry',
    'value' : 0
}, inplace=True)

print('DataFrame head after filling...thus cleaned ')
print(band_df.head()) 


#How to Convert string columns 'id' , 'age' into interger
users_df['id'] = users_df['id'].astype(int)
users_df['age'] = users_df['age'].astype(int) 


#Basic Analysis Using Pandas

#Displaying every city in our dataset
print('Adisplay of Cities in our dataset ')
print(users_df['city'])


#Counting the occurance of each city in our dataset
print('A Display of each city and people leaving there')
user_age_count =users_df['city'].value_counts()
print(user_age_count)

#Finding the mean Age of user's DataFrame and converting it to an interger
user_mean_age =users_df['age'].mean()
print(f"The Average age of Users in a float format  {user_mean_age}")

user_mean_age1 =users_df['age'].mean().astype(int)
print(f"The Average of Users after converting afloat to an interger :{user_mean_age1}")



#BASIC TRANSFORMATION METHODS USING NUMPY
#Creating a numpy array from a Dataframe column of 'age' 
ages= users_df['age']
mean_age=np.mean(ages)
std_age = np.std(ages)

#Normalizing the Age
normalazied_age=(ages-mean_age)/std_age

#Displaying the mean age and Standard Deviated age 
print(f"The Average age of Users is :{mean_age} \nThe Standard Deviatited age is : {std_age}  ")

#It displays the 1st ten normalized age
print(f"The normalized age of Users is : {normalazied_age}") 
print('**************************************************************')



#Advanced Data Transformation
#current_year=pd.Timestamp.now('year')
#band_df['value']=current_year-band_df['year'].astype(int)
#print(band_df['value'].head())



#Catergorize Users into age groups
def age_group(age):
    if age < 20 :
        return 'Teen'
    elif 20 <= age < 30:
        return 'Young Adult'
    elif 30 <= age <50:
        return 'Adult'
    else :
        return 'Senior'
    
    
    
#Data set without Age group
print('Old Data without the Age Group') 
print(users_df.head()) 

#Adding another column of Age group in our dataset
users_df['Age Group'] = users_df['age'].apply(age_group)
print('New DataFrame with the Age Group')
print(users_df.head())





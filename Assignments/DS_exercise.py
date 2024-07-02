import pandas as pd

#df = pd.read_csv('Datasets/band-csv.csv')
#print(df.head())


#Data cleaning

data = {
        'Name' : ['Elton','Samson','Aford',None,'Tonny'],
        'Age'  : [23,None,26,28,34],
        'Salary' : [2000,4000,3500,None,12000],
        'City' : ['Kampala','Masaka','Entebbe','Jinja',None]
}        

#df = pd.DataFrame(data)
#print(df)


#Dropping/Deleting missing values
#df_dropped = df.dropna()
#print(df_dropped)

#df_filled = df.fillna()
#print(df_filled)

#Sample DataFrame with Categories
data001 ={
    'ID' :[1,2,3,4,5,6,7],
    'Categories' :['A','B','C','A','B','C','A']
}

df = pd.DataFrame(data)

#Define mapping of categories to integers
category_mapping ={'A':1, 'B':2, 'C':3}
df['Categories'] = df ['Categories'].map(category_mapping)
print("Data Frame after mapping....")
print(df)


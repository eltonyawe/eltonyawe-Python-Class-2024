import pandas as pd


#Simple Data Frame
data = {
        'Name' : ['Elton','Samson','Aford','Yaseen','Tonny'],
        'Age'  : [23,21,26,28,34],
        'Salary' : [2000,4000,3500,5900,12000],
        'City' : ['Kampala','Masaka','Entebbe','Jinja','Mukono']
}        

df = pd.DataFrame(data)
print(df)

print(df['Age'])   #Accessing values using keys in the dictionary 
print(df.describe())   #it only operates with integers




#Example of a DataFrame with missing values

data1 = {
        'Name' : ['Elton','Samson','Aford',None,'Tonny'],
        'Age'  : [23,21,None,28,34],
        'Salary' : [2000,4000,3500,5900,12000],
        'City' : ['Kampala','Masaka','Entebbe','Jinja',None]
}  


df_missing = pd.DataFrame(data1)


#Displaying the missing values in
print(df_missing)


#Droping rows with missing values  (It removes data with missing values)
df_dropped =df_missing.dropna()
#print(df_dropped)

#Filling missing data  in DS
df_filled = df_missing.fillna({
    'Name' : 'Unknown',
    'Age' : int(df_missing['Age'].mean()),
    'Salary' : 0,
    'City' : 'Paradise'
})

#print(df_filled)



#Data  Filtering in Data science
df_filtered = df_missing[df_missing['Age'] > 25]
#print(df_filtered)


#Data grouping in DS

#Grouping by City and calculate mean age of each city
group_df =df_filled.groupby('City')['Age'].mean()
print(group_df)

#Grouping by Name and calculate mean salary of each city
group_df1 =df_filled.groupby('Name')['Salary'].mean()
print(group_df1)
import pandas as pd
import numpy as np

data1 ={
    "ID" : [1,None,None,None,5,6,None,8,9,10],
    "Name" : [None ,"John","Peter","Seeka",None,"Mugisha","Akiiki",None,"Emma","Yasin"],
    "Age" :  [53,None,21,63,56,78,None,44,50,88,],
    "Status" : ["Married","Single","Married",None,"Married","Single","Married",None,"Married","Single"],
    "Nationality" : ["Ugandan",None,"Ugandan","Sudanese","Ugandan","Kenyan","Congoless","Sudanese","Rwandans","Sudanese"],
    "Profession" : [None,"Doctor","Computer programmer",None,"Civil Engineer","Teacher",None,"Chef","Teacher","Doctor"],
    "Annual Salary" : [132000,120000,1570000,97800,67000,None,110000,50000,140000,None]
} 

df = pd.DataFrame(data1)
print(df)

#Displaying 1st five rows of the dataset in the DataFrame 
print(df.head())

#Displaying the general summary of the dataframe
print(df.describe())

#Displayiny the type of items ineach column
print(df.info())

#Checking missing values
#print(df.isnull().sum())
print(df.head())


#Filling the missing values with a value
df['Age'].fillna(df["Age"].mean(), inplace=True)
df["Annual Salary"].fillna(df["Annual Salary"].mean(), inplace=True)
df["ID"].fillna(df["ID"].mean(), inplace=True)

print(df.isnull().sum())

print(df.dropna)

df['Name'].fillna(df["Name"].mode()[0], inplace=True)
df['Status'].fillna(df["Status"].mode()[0], inplace=True)
df['Nationality'].fillna(df["Nationality"].mode()[0], inplace=True)

print(df.isnull().sum())









#Concatinating / Joining two dataframes as one with similar keys
data001 ={ 
         'Name' : ['Elton','Samson'],
        'Age' : [23,21]
}
df001 = pd.DataFrame(data001)
#print(df001.head())


        
data002 ={
    "Name":['Aford','Yaseen'],
    "Age" :[28,34]
}


df002 = pd.DataFrame(data002)
#print(df002)


df003 = pd.concat([df001,df002])
#print(df003)



#Merging/ Jioning two dataframes as one with different keys

info_df1 =pd.DataFrame({'Name' : ['Mathew','Simon'], 'Age' : [23,21]})
#print(info_df1)


info_df2 = pd.DataFrame({"Name":['Mathew','Simon','Simon'],"Salary" :[50000,42900,100000]})
#print(info_df2)


merged_df =pd.merge(info_df1,info_df2, on="Name")
#print(merged_df)



employment_df=pd.read_csv('Datasets\Employment.csv')
print(employment_df.head())




#print(employment_df.info())
print(employment_df.isnull().sum())

employment_df.fillna({
    'Week_end': "Unknown week_end",
    "High_industry": "Unknown Industry",
    "Value": 0
    
},inplace= True)


print(employment_df.head())
print(employment_df.tail())

#employment_df['Value'].fillna(employment_df['Value'].mean(),inplace=True)
#employment_df['Week_end'].fillna(employment_df['Week_end'].mode(),inplace=True)
#employment_df['High_industry'].fillna(employment_df['High_industry'].mode()[0],inplace=True)

#print(employment_df.isnull().sum())



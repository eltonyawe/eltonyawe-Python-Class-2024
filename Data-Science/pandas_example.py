import pandas as pd

#Introduction to Data collecting and loading
#Creating a Data Frame
data = {
        'Name' : ['Elton','Samson','Aford','Yaseen','Tonny'],
        'Age'  : [23,21,25,28,32],
        'Course': ['Python','Java','C++','Javascript','SQL']
}
# Data Frame created
df =pd.DataFrame(data)



#Accessing Data
print(df.head())#head function collects afew rows and columns of the data


df1 =pd.read_json('Datasets/users.json')
df2 =pd.read_csv('Datasets/band-csv.csv')
print(df1.head())

#Data Cleaning
#It involves handling missing values,removing duplicates and correcting data types


#Checking for the missing values     #Note : isnull function identifies missing values
#print(df.isnull().sum())

#Filling missing values with the mean of the column
#df['value'].fillna(df['value'].mean())



#Basic Statistics of a dataset
#print(df.describe())          #NB:describe function is used describe data and match it together on a graph



data001 = {
        'Name' : ['Elton','Samson'],
        'Age'  : [23,21]

}

data002 ={
        'Name' : ['Elton','Samson'],
        'City' : ['Kampala','Mukono']
}


df001 =pd.DataFrame(data001)
df002 =pd.DataFrame(data002)
print(df001)
print(df002)



#Merge based on common columns
#merged_df = pd.merge(df001,df002,on='Name',how='inner')
#print(merged_df)


# Calculation
#mean_age = merged_df['Age'].mean()
#print(mean_age)

#median_age = merged_df['Age'].median()
#print(median_age)










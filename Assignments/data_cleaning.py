import pandas as pd
import numpy as np


#Reading the datasets in the dataframe imported 
df =pd.read_csv('band-csv.csv')
print(df.head())#It displays  few lines of data in the dataframe soas to know the values of each column & row 
print('************************')


print(df.describe())#It displays the summary of the dataframe
print("*************************")

print(df.isnull().sum())#It identifies missing values and adds them up together
print("DataFrame already clean there are no missing values in data frame of csv so nothing is to be replaced.....")
import numpy as np
import pandas as pd

#Create numpy array
data = np.array([[1,2,3,4],[5,7,8,9]])

#Create DataFrame from numpy array
df =pd.DataFrame(data,columns=['A','B','C','D'])
print(df)

print('**********************')


#Creating  Series
df1 =pd.Series([1,2,3,4,5])
print(df1)


#Creating a dataframe with random numbers in amatrix of 5rows and 3 columns
df2 = pd.DataFrame(np.random.randn(5,3))
print(df2)




#Introduction to Data collecting and loading
#Creating a Data Frame
data1 = {
        'Name' : ['Elton','Samson','Aford','Yaseen','Tonny'],
        'Age'  : [23,21,25,28,32],
        'Course': ['Python','Java','C++','Javascript','SQL'],
        'Telephone' :[2560347500,+230034678,+45003789,+115578899,+569900776]
}
# Data Frame created
df001 =pd.DataFrame(data1)



#Accessing Data
print(df001.head())#head function collects afew rows and columns of the data



import pandas as pd
import numpy as np

#Simple Data Frame
data = {
        'Name' : ['Elton','Samson','Aford','Yaseen','Tonny'],
        'Age'  : [23,21,26,28,34],
        'Salary' : [2000,4000,3500,5900,12000],
        'City' : ['Kampala','Masaka','Entebbe','Jinja','Mukono']
}        

df = pd.Series(data)
print(df)


df1 = pd.Series(data)   #Accesing values in series
print(df1['City'][1])


#Creating a DataFrame using random numbers by 4rows *3columns matrix
data_frame=pd.DataFrame(np.random.randn(4,3))
print(data_frame)



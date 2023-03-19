'''

What is Pandas?
ans: Pandas is a tool that for data processing which helps in data analysis
it provides function and methods to efficiently manuplate large dataset
data structure in Pandas is type :-
1. Series (one dimensional array)
    series is a one dimensional array with labels. it can contain any data type include integer float string python object and many more
2. DataFrame(two-dimensional array)
    Dataframe is a two-dimensional data structure  with label. We can use label to locate data


'''

import pandas as pd
import numpy as np
print(pd.__version__)

# ************** series => create , manipulate, query, delete ******************

# create series from list
arr=[0,1,2,3,4]
s1= pd.Series(arr)
print(s1,)
print()
order=[1,2,3,4,5]
s2=pd.Series(arr,index=order) # we can set index num here
print(s2)
n=np.random.randn(5) # create random numpy array
index=['a','b','c','d','e']
s3=pd.Series(n,index=index)
print(s3)
print()
d={'a':1,'b':2,'c':3,'d':4,'e':5} # create dictonary as pandas array
s4=pd.Series(d)
print(s4)
print()

# Modifying index of series
s1.index=['a','b','c','d','e']
print(s1)
print()

# slicing
print(s1[:3])
print()
s4=s1.append(s2)
print(s4)
print()
print(s4.drop('e'))

# Series Operation
arr1=[1,2,3,4,5,6,7]
arr2=[1,2,3,4,5]
s5=pd.Series(arr1)
s6=pd.Series(arr2)
s7=s5.add(s6)
print(s7)
print()
s8=s5.sub(s6)
print(s8)
print() # also can we s5.multi(s6) and s5.div(s6)
print('medium',s6.median())
print('max',s6.max())
print('min',s6.min()) # we can view some statistic of array
print()

# ******* Create DataFrame **********
dates=pd.date_range('today',periods=6)
#print(dates)
numarr=np.random.randn(6,4)
#print(numarr)
columns=['A','B','C','D']
df1=pd.DataFrame(numarr,index=dates,columns=columns)
print(df1)
# create Dataframe With Dictionary
data={'animal':['dog','cat','snake','dog1','frog','bird','crocodile','elephent'],
      'age':[2.5,2,5,5,10,2.7,15,36],
      'visits':[1,3,2,3,1,3,1,2],
      'priority':['yes','yes','no','no','yes','yes','no','yes']
      }

labels=['a','b','c','d','e','f','g','h']
df2=pd.DataFrame(data,index=labels)
print(df2)
# print(df2.head()) First theke print korrbe
# print(df2.tail()) last theke
# print(df2.values) # make array in nice order
# see statical data of DataFrame
print(df2.describe())
print(df2.T) # its manuplate data as index as columns and columns as index
print(df2.sort_values(by='age')) # we can also sort the values
# we can also be slicing and also sort and do many thing with data
# ********** Query ***********
# query by tag
print(df2[['age','visits']])
# print(df2.iloc[1:3])  same as slicing
df3=df2.copy() # by this we can copy an array
print(df3.isnull()) # make true false and false true
df3.loc['f','age']=4.5 # by this we can actually change the value of data
print(df3)

#****** why not work dont know
#print(df3.mean()) # gives only numirical value dont work on string or char
#print(df3.add())
string=pd.Series(['ada','A','B','C',np.nan,'owl','ag'])
print(string.str.lower()) # make lower

# ************* operation with DataFrame ************
df4=df3.copy()
# DataFrame File operation
df3.to_csv('animal.csv') # create data into csv file
df_animal=pd.read_csv('animal.csv') # read that csv file
print(df_animal.head(3))
# we can also create many type of file like excel html sql










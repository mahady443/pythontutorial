'''
What is Numpy?
ans: Numpy is the core library  for scientific numerical computing in python
its provide high performance  multidimensional array object and tool for working with array
1. numpy main object is the multidimensional array
2. it is a table of elements (usually number ) all the same types indexed by a tuple of positive integer
3. in Numpy dimension are called axes

why should we use numpy when we have python list
1.Fast 2.Convenient 3.less memory
'''

import numpy as np
a=np.array([1,2,3])
print(a)
print(a[1])

import time
import sys
b=range(1000)
print(sys.getsizeof(5)* len(b))
c= np.arange(1000)
print(c.size*c.itemsize)

size=100000
L1=range(size)
L2=range(size)
A1=np.arange(size)
A2=np.arange(size)
start=time.time()
result= [(x+y) for x,y in zip(L1,L2)]
print(result)
print("Python list take time ",(time.time()-start)*1000)

start=time.time()
result=A1+A2
print("Numpy array take time ",(time.time()-start)*1000) # example of time

c=np.array([[1,2], [3,4], [5,6]])
print(c.ndim) # no of dimension
print(c.itemsize)
print(c.shape)
d=np.array([[1,2], [3,4], [5,6]],dtype=np.floor(64)) # convert in float
print(d)
print(d.itemsize) # iteam size change cause of float all rest same

e=d=np.array([[1,2], [3,4], [5,6]],dtype=np.complex128)  # complex convert
print(e)
print(e.itemsize)

f=np.zeros((3,4)) # create zero matrix
print(f)

print(np.arange(5)) # create 0-4 array

s=np.char.add(['He','the'],['is','boss']) # concatenation array
print(s)
t=np.char.multiply('hello  ',3) # multiply the char
print(t)
v=np.char.center('hello',20,fillchar='-')
print(v)
print(np.char.capitalize('how are you doing?')) # Capital first letter
print(np.char.title('how are you ?')) # capital all word first letter
print(np.char.lower('HOW ARE YOU?')) # all in lower
print(np.char.upper('how are you ?'))  # all in upper
print(np.char.split("Hello\nAre You There"))
print(np.char.splitlines("Hello\nAre You There"))
print(np.char.strip(['admin, alarm,hola'],'a')) # kono letter ba word bad dewar jonno
print(np.char.replace("He is a good player","is","was"))








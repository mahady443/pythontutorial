'''
What is array?
ans: Array is a container which store same type of multiple values
syntax: var_name= array(typecode,[elements])
there are huge typecode available see more  . https://www.educative.io/answers/what-are-type-codes-in-python
'''
from  array import *
var=array('i',[1,2,3,4])
print(type(var))
print(var)
print(var.buffer_info())
print(var[2])


for i in var:
    print(i) # eivabe o array print kora jai
for pnt in range(1,4): # pnt = pointer just like i nothing special
    print(pnt,var[pnt]) # amra jodi chai 1-3 er elements print korte then range function dia kora jai

var.reverse() # array reverse er jonnno amra reverse function use korte pari
print(var)
var.append(2) # add with append
print(var)

var.remove(2) # remove keyword to remove eikhane same multuple value thakle amader first er ta jabe baki gula thakbe
print(var)
print(var.index(2)) # index e ki ace ta print korbe index=1 theke hoi 0 theke noi
# ************ input an array from user *************
arr=array('i',[])
n=int(input("Enter array size : "))
print("enter %d elements: "%n)
for i in range(n):
    x=int(input())
    arr.append(x)
print(arr)



print("Hello World")


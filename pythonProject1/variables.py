import os
integer = 100
print(type (integer))   # int type
floatVariable = 3.1416  # float type
print(type(floatVariable))

string_type = "ME is the best"
print(type(string_type))

list = [14,13,31]
print(type(list)) # lsit type variable er jonno third bracker dia shuru korte hoi
print(list[2])

# tuple er jonne first bracket dia shuru korte hoi

tuples= (31,1,36)
print(type(tuples))
print(tuples[1])
''' tuple and  list er modde diffrence hoilo
tuple er value change kora jai na like x[1]=30 eita final keyword er moto
list er value change kora jai like x[2]=36
'''
#file pointer
filepionter=open('variables.py','r')
print(type(filepionter))

#multi value assign
(first,second,third)= (1,2,3)
print(first)

first=second=third = 3 # same value assaign
print(second)

# **********Arithmatic Operation*************

a= 3
b = 2
result = a+b
print(result)

result = a-b
print(result)

result = a*b
print(result)

result = a/b
print(result)

result = a%b # vagsesh modulas ber korar jonno
print(result)

result = a//b
print(result)

# ***********String Operation*************

Var = "Mahady is always good"

print(Var[3]) # extract single character

print(Var[0:6]) # multiple character print korar jonno



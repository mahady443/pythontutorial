'''
what is list in python???
A list is a collection of data. it can hold multiple data types
third bracket diya shuru hoi
'''

num= [3,1,1,5,9]
print(num)
letter= ['a','f','h' ]
print(letter)
strs=["mahady","is ","genius"]
print(strs)
mix=["no",1 ,"is ", "me ","<3", 2 ]
print(mix)
# list is list like matrix
mat= [[1,2],['a','b']]
print(mat)

# **************Accessing in list ************
# access er jonno third bracket diya indice num dile hobe

print(mix[2])
print(mix[-2]) # minus dile last theke count kore jamon eikhane 2nd last
print(mix[:3]) # multiple list access er jonno
print(mix[3:]) # eikhane 3 theke start korbe
print(mix[::2]) #2 dara vag hobe so 2,4,6,8 eigula bad jabe
print(mix[::-1])  #reverse order e print hobe


# ***************** Operation In LIST ****************

z= [0]*5
print(z)
# concated 2 string

conc= strs+letter
print(conc)
var= list("hello mahady") # string re list e convert korar operation
print(var)
one,two, *other = num
print(one)
print(two)
print(other) # er maddome list theke value extract kora hoice first indices er jonno one then two,three eivabe

# ************Method in List *************

print(num)
num.append(7) # kono kicu last e add korte chaile
print(num)
num.extend(strs) # ek list er moodde onno list add korte chaile extend
print(num)
num.insert(6,"oh") # kono element majkhane kothao add korte chaile
print(num)
num.insert(6,36) # syntax hoile first e (indices_num, element)
print(num)
num.remove("oh") # kono element remove korar jonno
print(num)  # ekshate multiple remove  kora jai na  r jodi ekta word bar bar thake tahole shudu first er ta remove kore
# sorting
var1=['a','g','e','z','l']
var1.sort()
print(var1)
num2= [3,1,6,4,2]
num2.sort()
print(num2)


# built-in function with list

a= [3,5,6,7,1]
print(len(a)) # list er length ber korar jonno
print(min(a))
print(max(a))
print(sum(a))
print(sum(a)/len(a))











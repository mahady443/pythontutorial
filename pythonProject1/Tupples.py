'''
what is tuple?
ans: tuple is collection of  immutable heterogeneous python object
# tuple first bracket diya shuru hoi but  na dile eita tuole hisabe naoa hoi kintu ekta comma dite hobe oita tuple bananor jonno
naile eita k str ba int ei hisabe print korbe
immutable mane amra tuple change korte parbo na
amra kokon tuple use kori jokon mone hoi amader r value change kora lagbe na ex: country name , place , school etc
'''
emp = ()
print(type(emp))
print(emp)

tup = "mahady",
print(type(tup))


tup1= ("mahady","hasan", "is ", "genius")
list1= ["mahady","hasan", "is ", "genius"]
list1.append("no doubt")
# tup1.append("no doubt") its cant coz tuple value was like final keyword we cant change through the code
print(list1)
print(tup1)

print(tup1[3]) # same as list and string sob gulai ei vabe value extract kora hoi

# ************** Concatenation *****************

num= 1,2,3,4
print(num+tup1)

# ************ nesting ****************

nest =(num,tup1) # er maddome onno tuple k r ekta tuple e store kora hoi
print(nest)

# ************* repetition *************

rep1 = ("mahady",) *5 # ekta value multi time print er jonno
print(rep1)
rep1=("mahady",)
print(rep1*5) # another way

# ********** Slicing **************
num1= 1,2,3,4
print(num[1:])
print(num[ :: -1])

# ********* Unpacking ***********
print(tuple ("mahady"))

a,b,c,d = num
print(a,b,c,d) # assign value one by one i another

a,*b,c= num # ei khane *b dara bujano hoice amra  first and last ta a and c te dice baki ja ace ta b er modde list hisave thakbe
print(a,b,c)
print(type(b))

# **************Deleting ******************

del1 = 1,2,3,4
print(del1)
del(del1)
# error print(del) karon already tuple delete hoia gase amra jani j tuple er value chage kora jai na so amra delete o korte pari na but pura tuple delete kora jai

# *******************Built in function on tuple *******************

num2 = (1,2,3,4,3,4,5,1,2,3,4)
print(num2.count(3)) # koita 3 ace eita count kore
print(sum(num2))
print(len(num2))
print(max(num2))
print(min(num2))

# ***************** Converting ******************

list3 = [1,2,3,4]
print(type(list3))
tup3 = tuple(list3)
print(type(tup3))

# ************ Nesting in Tuple in list ************

lst = [(1,2,3),[4,5,6]]
print(lst)
lst.append(("tuple", "is","there")) # add new tuple
print(lst)
lst.remove((1,2,3)) # remove tuple
print(lst)

# ************* Nesting List in Tuple *************

tup2= (['a','b','c'],['d','e','f'])
print(tup2)
tup2[0].append('z') # jodio tuple er value add kora jai na kintu amara tuple er modde thaka list er value add korte pari
print(tup2)
tup2[0].remove('z')
print(tup2)

'''
But we cant add new tuple in there
tup.append(['x','y'])
eita error dibe
'''



'''
What is Dictionaries ?
ANS: Dictionaries is an unordered collection of data stored as a pair of key and value
Syntax : {key:value}

'''

d1= {}
print(type(d1))

d2={1:"Mahady",2:"is",3:"a",4:"genius"} # thats not mandatory  only integer can indice number
print(d2)

d3={"name":"Mahady","age":"20","profession":"Student"}
print(d3)

d4=dict({1:"Mahady",2:"is",3:"a",4:"genius"})  # another method to create using dict function
print(d4)
d5=dict([(1,"mahady"),(2,"hasan"),(3,"munna")])  # another method to create using dict function
print(d5)


# ******************** Nested dictionary ********************
d6={"name":{"first":"Mahady","last":"Hasan"},"age":"20","profession":"Student"}  # dictonary in dictonary
print(d6)

# ************** Adding Element ******************

d7={}
print(d7)
d7[0]="hello"
print(d7)
d7[1]=("how","are","u") # add tuple in dictionary
print(d7)
d7["name"]= "Mahady hasan" # we can add string value also
print(d7)
d7["name"]= {"first":"Mahady","last":"Hasan"} # we can also update dictionary and also add dictionary in dictionary
print(d7)



#  ************* Access in Element ****************
print(d7[1])
print(d7["name"]["first"]) # extract data in dict into dict

print(d7.get(1)) # special method to extract data in dict


# *************** Deleting Element in Dict *****************

d7.pop(0) # pop keyword diye delete kora hoi
print(d7)

d7.popitem() #popitem er madome always sesh indice delete kora hoi
print(d7)


# ******************* In built Function ***************

d8= {"name":{"first":"Mahady","last":"Hasan"},"age":"20","profession":"Student"}

print(d8.values()) # return value not key name

key= {'a','b','c','d'}
value=1
d9= dict.fromkeys(key,value)
'''jodi multiple key er same value  hoi amra dict.fromkeys er maddome ekshate assign korte pari and 
 ei khane output kayal korle dekha jai dictiionary unorder e thake '''
print(d9)

d8.clear() # pura dict delete koira dei
print(d8)

'''
what is set?
ans: set is an unordered collection of unique elements
set er modde jodi ekta value double thake tahole set oi vlue thika ekta e nai baki sob bad diya dai (see set1 example)
set use kora hoi beshi math (er set) problem solve er joonno jamon union set ,
'''

set1={10,20,30,10} # amra jodi key :value er moto  na likhi 2nd bracket er modde taile oita automatic set hoia jai

print(set1,type(set1))
set2= set([10,20,30,40])# set keyword diya o create kora jai
print(type(set2))
set2.add('a') # kono value add korte hoile add keyword
print(set2) # print output e dekha jai eita unorder e asce

# *****************Frozen Set *******************

fs1=frozenset([10,20,30])
# fs1.add('a') we cant add value to the frozen set karon eita immutable. frozenset use korle amra r oi set er value add korte patbo na

set4={1,2,3}
set5={4,3,5}
print(set4.union(set5)) # union ber kore

print(set4.difference(set5))
print(set4.intersection(set5))


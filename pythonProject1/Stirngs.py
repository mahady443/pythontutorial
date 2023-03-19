'''
 What is String ?
 ans: String is one kind of data type in Python, composed of collection of  character  Ex: Mahady , Hasan, Munna
String double or single quotes er vitor lekte hoi
but single character er jonno single and ekta sentence er jonno double use kora valo
'''

str1='a'
str2= "mahady"
print(str1,str2)

str3='''this is 
multiple line string 
'''  # 3 qoutes dia start korte hoi
print(len(str2))  # length of string
print(str3[3])  # Extract value

for i in  str2:  # print all character line under line
    print(i)

for i in str2:
    print(i, end=" ")
    # print all in one line




# **************** Slicing ****************
print(str2[0:5])
print(str2[3:])
print(str2[2:4])

# ***************** Built in Method ****************

str4 = "Mahady Hasan"
print(str4.upper()) # all in capital
print(str4.lower()) # all in lower

print(str4.find('a')) # find character  index num
print(str4.index('a'))  # same as find  but jodi multimple time oi character thake tahole  era shudu first  er tar index num dibe

# ***************** Split Function ****************

print(str4.split(" ")) # like split kore ekta sentece ba string k list e convert kore but bole dite hoi what is the key to split. ex . Mahady Hasan e space

x= str4.split(" ") # eivabe ekta variable e store kora jai value
print(x)

# **************** Replace Function ****************

print(str4.replace("Hasan","munna")) # kono kicu replace korar jonno

# ************* R Partion Method ******************
print(str4.rpartition( " ")) # eitai tuple convert kore but amra jai parameter diya change korbo oitao add hobe like space

# *********** Concataning in String **************

str5= "Mahady is "
str6= "genius"
print(str5 + "a " + str6) # amra chaile store o korte pari just variable er modde declare korte hobe

'''
*************** Format function ************
amade kace jodi onk string thake amra eigula k concatating korte chai abar space ba diffrent symbol dite chai tahole oita onk tough hoi
tai amra format use kori
'''
str7= "{}  {}  ! " .format(str5,str6)
print(str7) # jei format e print korte chai oi vabe likle hobe



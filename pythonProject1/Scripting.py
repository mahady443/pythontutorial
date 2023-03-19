import os
print(os.listdir())

def currentdirectory():
    cwd=os.getcwd() # print current work directory
    print(cwd)

currentdirectory()

#time
import time
epc = time.time()
print(epc)
localtime= time.localtime(epc) # format e time print kora
print(localtime)
print(localtime.tm_year) # if we want to extract any kind of data
print(time.ctime(epc)) # if we want to print time in actual format use cttime keyword

# SMTP
# ******* Sending Mail *******
# its not work now try to find more info
'''
import smtplib
import ssl
sender_email="mahadyhasan355@gmail.com"
password=str(input("please enter password"))
rec_email="mahadyhasan252@gmail.com"
message="hello buddy"

smtobj=smtplib.SMTP('smtp.gmail.com',587)
smtobj.starttls()
smtobj.login(sender_email,password)
print("login succesfully")

smtobj.sendmail(sender_email,rec_email,message)
print("message is sent")
'''
# ********* Create file ***********
from os import path

def createFile(dest):
    if not (path.isfile(dest)):
        f=open(dest,'w')
        f.write("Welcome to the world of python")
        f.close()

dest="D:\\python\\pythonProject1\\sample.txt"
createFile(dest)
print("File created")

# ********** Run TIME *********

def func1(*args): # args er maddome amra unlimited value nite pari diffrent type of value o jai
    for i in args:
        print(i)
func1(10,20,30,40)

def func2(*args,**kwargs): # kwargs e amra variable o nite pari
    for i in kwargs.items():
        print(i)
func2(a=20,b=30)

# *********** Nested Function *************
'''
why need nested function?
ans: So, in Python, nested functions have direct access to the variables and names that you
define in the enclosing function. It provides a mechanism for encapsulating functions
creating helper solutions, and implementing closures and decorators
'''
def func3():
    x=10
    def func4(x):
        return x+1
    return func4(x)
result=func3()
print(result)


def func5(called_func):
    print("this is first function ")
    def nested_func(called_func):
        print("this is nested function")
        called_func()
    return nested_func(called_func)
@func1
def outer_func():
    print("this is outer function")

outer_func

# ****** create class in runtime ***********
#that called Factory

B=type("Baseclass",(object,),{})
C1=type("C1",(B,),{'val':5})
C2=type("C2",(B,),{'val':20})

def ClassCreator(bool):
    if bool:
        return C1()
    else:
        return C2()

print(ClassCreator(True).val)
print(ClassCreator(False).val)

# why that's not output because too much thing is run if we create separate then it run well





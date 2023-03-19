'''
What if Function?
ans: a function is a set of code that performs some task
syntax: def function_name:
                statement(s)

'''

def welcome():
    print("Good Morning")

welcome() # always function execute korar jonno amader function call korte hobe

def add(b,a):
    total= a+b
    print("a:%d  b:%d" %(a,b))
    print("the sum is ",total)


add(10,20)
#or
x=14
y=15
add(x,y)
add(a=10,b=20) # suppose we dont know the position a is first or second then we can use keyword to define the value

# if we want to set a defualt value on parameter in function we can
def add1(a=0,b=0):
    total1= a+b
    print(total1)
add1(10)
# we can add a  list that can give user to  put multiple value or single also
def add2(*a):
    total2=0
    for i in a :
        total2=total2+i
        print("the sum of your list is : " ,total2)

add2(20,30,440,1)
add2(12)






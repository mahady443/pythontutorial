'''
While loop?
ans: while loop is used to repeat a section of code unknown number of time until it matched  the specific  condition
Syntax while expression:
            statement

'''
i = 1
while i <= 10:
    print(i, "Mahady is a genius")
    i += 1  # its like i++
print()
i = 10
while i >= 1:
    print(i, "Mahady is genius")
    i -= 1
print()
# ****************1st 10 number Sum *********************
i = 1
sum = 0
while i <= 10:
    sum = sum + i
    i += 1  # eikhane jodi sum amra loop e increment or decrement value dite hobe naile error hoi
print(sum)  # sum while loop er modde korle amra protibar i er value pabo ex, 1+2=3 ,3+3=6,6+4=10 eivabe

# ************** print even num sum ****************

i = 1
sum = 0
while i <= 10:
    if i % 2 == 0:
        sum = sum + i
    i += 1  # eikhane i amader if condition er baire rakte hobe karon eita 10 time increment korbe i k tai
print(sum)

# ************* Reverse Number **************
# too hard to understand  need more to learn
n= int(input("Enter ta Number: "))
nr=0
while n%10 !=0:
    c= n%10
    nr=nr*10+c
    n=n//10
print(nr)

# ******* find length ******

x=[1,2,3,"mahady"]
length=0
i=0
try:
     while x[i]:
        length+=1
        i+=1
except IndexError: # kono error handle korar jonno
    print(length) # eikhane ekta error dai jodi amra simple print korte chai karon index er baire chole jai tai maybe int er modde string use kora hoice tai

# ******** print pattern with while loop ***********

n=int(input("Enter a number: "))
i=1
while i<=n:
    j=1
    while j<=i:
        print(i,end=' ')
        j+=1
    i+=1
    print()



'''what is for loop?
ans: For loop is use to iterate over a sequence ,which could be a tuple list or string
syntax: for counter  in sequence:
                        statement
ex: for loop
'''

x=[1,4.2,"mahady"]
for i in x :
    print(i, end=" ") # print the element of list

for i in range(0,20,2):
    print(i)
'''
    range function er kaj hocce koto bar amra loop chalaite chai
    range er 3 ta vag ace 
    range(start,condition,icrement value)
    start hocce koto num index theke value store hoa shuru hobe  jamon kono kicu na thakle 0, ba amra define kore dite pari 1,2 etc
    condition  hocce amra ki korte chai code er modde upore jamon amra 20 porjonto int number nici eirokom amader ja dorkar tai amra condition e likbo
    icrement value hocce koto kore value bar be jamon upore 2 daoa hoice so 2 kore num barbe jamon 2,4,6. Kono kicu na thakle 1 kore bare (like ++)
    for loop e always range asbe 
'''
sum=0
for i in range(11):
    if i%2==0:
        sum=sum+i
print(sum,end=" ") # sum of first 10 even num (*amader 11mane 10 alwasys 1 beshi nite hobe )

# ********** make pattern **********
# pattern print er jonno best hocce loop
x=int(input("Enter your num :- "))
for i in range(1,x+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

# ********** Metrix sum ***********
# so dangerous need to learn more
r=int(input("Enter of row :- "))
c=int(input("ENter colum no:-"))
x=[]
val=[]

for i in range(r):
    for j in range(c):
        val.insert(j,int(input("Enter the  %d * %d element"%(i,j))))
    x.insert(i,val)
    val=[]
y=[]
for i in range(r):
    for j in range(c):
        val.insert(j,int(input("Enter the  %d * %d element"%(i,j))))
    y.insert(i,val)
    val=[]

sum1=[]
for i in range(r):
    for j in range(c):
        val.insert(j, x [i] [j] + y [i] [j])
    sum1.insert(i,val)
    val=[]

print(sum1)








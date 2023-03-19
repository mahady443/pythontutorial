'''
What is loops?
ans: a loop is an instruction that repeats multiple times as long as condition is met.
how many loop in python?
ans : 3 loops . 1. for loop 2. while loop 3.nested loop

what is while loop?
ans: the while loop is repeat a section  of a code an unknown number of times until a specific condition  is met
syntax: while Expression:
                        statements
ex:while loop

what is for loop?
ans: For loop is use to iterate over a sequence ,which could be a tuple list or string
syntax: for counter  in sequence:
                        statement
ex: for loop

what is nested loop?
ans: its mean loop in loop. canbe for in for or while in while or  for in while or while in for
matrix er jonno use kora jai
loop control statement?
ans: loop control statement alter the regular flow of a loop
most use 2 control statement is
1. break
2. Continue

break : transfer control to the statement right after the loop
Continue: Skip the statement following it and return control to the beginning  of the loops
'''



# *************** While loop ******************

val=int(input("Enter number multiple of 7:- "))
while val % 7 !=0:
   val=int(input("Enter a number that multiplied by 7:-")) # jodi 7 er multiple na dai taile abr user theke input nibe (*remember it)
else:
   print("%d is a multiple of 7 " %val)

# ************** For loop ****************

x=[1,6,"mahady"]
for i in x :
    print(i) # jokon amra i print dibo tokon oita ekber jabe and first,second eivabe print korbe

# ************ Nested loop ***************

X=[[1,2,3],['a','b','c']]
for i in X :
    for j in i :
        print(j, end=" ") # end function new line toiri korte dai na
    print()

# ************** Break *************

s1="geu . hasan"
for k in s1:
    if k==".":
        break # simply jodi kotao loop er moode condtion true hoile baki ongsher dorkar hoi na tokon break use kore loop e
    print(k, end=" ")
    print()

# ************** Continue ************

for i in [1,13,20,4,23]:
    if i>10 :
        continue
    # else:  eikahen else er dorkar nai karon continue keyword punarai abr control for loop re diya dai
    print(i)


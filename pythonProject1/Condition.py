
'''
what is if else statement in python?
ans: if else is a decision-making  format
pyhton jehuto case sensitive so condition lekhar somoy kayal rakte hobe

what is if condition ?
ans: only execute the true statement .

what is if else ?
ans: if will execute true and else will false

what is if elif else ?
ans: jokon onk gula true statement thake tokon
basically kiekhane true pai oi khane print kore

'''
# ********************* If *************************
a=int(input())
if (a%2)==0:
    print(a,"is even number")  # eikahne shudu true hoile dekabe amra jodi odd nai kono kicu return korbe na

# ************** if-else ***************
b=int(input())
if (b%2)==0:
    print(b,"is Even Number")
else:
    print(b,"is odd Number")


# ***************Nested Statement **************
'''jokon condition er modde condition thake thokon amara nested statement use kori
eita avoid kora ucit karon onk boro program e eita kottin hoie jai tai joto para jai avoid kora valo.
'''
c=int(input())
if c<30:
    if c%2==0:
        print(c,"is a even and less than 30")
    else:
        print(c,"is odd number and less than 30")
else:
    print(c,"is a grater than 30")

# **************** if-elif-else ****************

d=input(21)

if d == 'a':
    print("is a vowel a")
elif d=='e':
    print("is a vowel e")
elif d=='i':
    print("is a vowel i")
elif d=='o':
    print("is a vowel o")
elif d=='u':
    print("is a vowel u")
else:
    print(d,"is a consonant")


'''
task
Create a calculator using condition 
'''



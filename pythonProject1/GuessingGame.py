import random
nump=random.randint(1000,9999)
print(nump)
n=int(input("Enter a 4 digit number"))
while n !=0:
    num=nump
    cor=0
    while num%10:
        numc=num%10 #numc = number correct
        nc=n%10
        num=num//10
        n=n//10
        if numc==nc:
            cor=cor+1
    if cor==4 :
        print("Congrats guess alll")
        break
    else:
        print("%d digit u guess"%cor)
        n=int(input("Enter 4 digit number again"))
else:
    print("You quit the game !")



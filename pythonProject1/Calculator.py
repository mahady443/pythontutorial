
# ***************** Calculator using conditions ******************

num1=eval(input("Enter first number: "))
num2=eval(input("Enter second number: "))

opt=input("Enter ur operation ")

if opt=="+":
    print(num1+num2)
elif opt=="-":
    print(num1-num2)
elif opt=="*":
    print(num1*num2)
elif opt=="/":
    print(num1/num2)
else:
    print("invalid Operation")
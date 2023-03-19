'''
What is class ?
ans: A class is like a blueprint while an instance is a copy of the class with actual values
what is object ?
ans: An Object is an instance of a Class
'''


class Person:  # create a class
    def __init__(self):  # define variable
        self.name = "Mahady"
        self.age = 20
        self.gender = " Male"

    def talk(self):  # create method
        print("Hi i am ", self.name)

    def voter(self):  # create method
        if self.age > 18:
            print("iam eligible to vote ")
        else:
            print("iam not eligible for vote")


obj = Person() # create  object for class
Person.talk(obj)
Person.voter(obj)
# or
obj.talk()
obj.voter()

# ******** if we have many object **********

class Person1:  # create a class
    def __init__(self,name,age,gender):  # ei khane amra ekon onk object create korte parbo
        self.name = name
        self.age = age
        self.gender = gender

    def talk(self):  # create method
        print("Hi i am ", self.name)

    def voter(self):  # create method
        if self.age > 18:
            print("iam eligible to vote ")
        else:
            print("iam not eligible for vote")

obj1=Person1("Mahady Hasan",23,"Male")
obj2=Person1("Asha",18,"Female")
print(obj1.name+" And  "+obj2.name)
obj1.voter()
obj2.voter()










'''
What is oops?
ans: object-oriented programing
'''

class Car :
  def __init__(self,speed):
    self.speed=speed
    def getspeed(self): # here getspeed refer to function name or method like java and self describe getspeed it self
        print("The speed is ",self.speed)
    def setspeed(self,speed): # Set method
        self.speed=speed

Bmw=Car(155)
Ford=Car(140)
Bmw.getspeed()
Ford.getspeed()
#or
Car.getspeed(Bmw) # jodi amra class doira call kori taile amader BMW parenthesis e dite hoi er jonno self keyword use kora hoi
Car.getspeed(Ford)
Bmw1=Car(160)
Bmw1.getspeed()
Bmw1.setspeed(143) # set the speed by set method
Bmw1.getspeed()

'''
Inheritance?
ans: Inheritance is a mechanism for a new class to use the features of another class 
'''
class Sadan(Car):
    def opentrunk(self):
        print("Trunk is opened")

Honda= Sadan(150)
Honda.getspeed()
Honda.opentrunk()
# Bmw1.opentrunk() give error karon amra parent er gula child e use korte parbo kintu child er function parent e na

'''
Encapsulation ?
ans : the feature of preventing data from direct access called encapsulation 

need to get more info 
'''
'''
Polymorphism?
ans : polymorphism is  the feature of using the same function in multiple ways

need to get more info
'''










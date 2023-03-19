'''
What is thread?
ans: a thread is a sequence    of instructions in a program that can be executed independently of the remaining program

need to learn more
'''
from threading import *

def show():
    print("This is a child thread")
t= Thread(target=show())
t.start()
print("This is a parents thread")

class MyThread(Thread):
    def run (self):
        for i in range(5):
            print("\n Child Threading")
t= MyThread()
t.start()
for i in range(5):
    print("\n Parent thread")

class Demo:
    def show(self):
        for i in range(3):
            print("this is child threads")
obj=Demo()
t=Thread(target=obj.show())
t.start()
for i in range(3):
    print("Main Thread")


'''
Context Switching
ans: Storing the state of thread and resumung its execusion in latar time is called Context Switching
'''
'''
Multithreading in python ?
ans : a model where multiple threads within a process execute independently while sharing the same resource called multi threading .
'''

import time # import time function
class Calculate:
    def num (self):
        for i in range(1,6):
            print("The number is ",i)
            time.sleep(1) # 1 secend por execute hobe totokon next thread execute hobe
    def double(self):
        for i in range(1):
            print(" The double of this number is ",2*i)
            time.sleep(1)
    def square(self):
        for i in range(1,6):
            print("The square of number is ",i*i)
            time.sleep(1)

obj1= Calculate()
t1=Thread(target=obj1.num())
t2=Thread(target=obj1.double())
t3=Thread(target=obj1.square())
t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()

t1.join()
t2.join()
t3.join()

print("main thread")




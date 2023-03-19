
name=input("Enter your name: ")
print("Welcome to the Quiz Game "+ name)

playing=input("You want to play game:  ")

if playing.lower() != "yes":
    quit()
print("let's Start The Game !")
score=0

answer = input("1. How Many Continents Are There ?  ")
if answer == "7":
    print("Answer is correct")
    score += 1
else:
    print("answer is incorrect")

answer = input("2. What is The Biggest Continent ?  ")
if answer.lower() == "asia":
    print("Answer is correct")
    score += 1
else:
    print("answer is incorrect")

answer = input("3. Which is the Smallest Continent ?  ")
if answer.lower() == "australia":
    print("Answer is correct")
    score += 1
else:
    print("answer is incorrect")

answer = input("4. Which Country is the Largest Country in the World ?  ")
if answer.lower() == "russia":
    print("Answer is correct")
    score += 1
else:
    print("answer is incorrect")

answer = input("5. Smallest Country in the World ?  ")
if answer.lower() == "vatican city":
    print("Answer is correct")
    score += 1
else:
    print("answer is incorrect")

print("You answered "+str(score)+ " questions")
print("You got"+ str((score /5)*100)+ "%")





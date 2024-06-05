print("Welcome to my computer quiz!")
answer = input("Do you want to continue? ")

if answer.lower() == "yes":
     print("Okay! let's play :) ")
else:
    quit()

score = 0
question = input("What does OS stand for? ").lower()
if question == "operating system":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")   

question = input("What does HTML stand for? ")
if question.lower() == "hyper text markup language":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 

question = input("What does CSS stand for? ")
if question.lower() == "cascading style sheet":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 

question = input("What does JS stand for? ")
if question.lower() == "javascript":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 

print("You got "+ str(score) + " scores") 
print(f"You got {(score/4*100)} %")   




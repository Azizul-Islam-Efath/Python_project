
import random

RandomNumber = random.randrange(0,100)

UserInput = int(input("What number would you like to guess? \n"))

if UserInput > RandomNumber:
    print(RandomNumber)
    print(f"Sorry, {UserInput} is too high")
elif UserInput < RandomNumber:
    print(RandomNumber)
    print(f"Sorry, {UserInput} is too low")
else :
    print(RandomNumber)
    print(f"{UserInput} is correct")




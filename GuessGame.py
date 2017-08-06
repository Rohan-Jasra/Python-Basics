import random

print("I am thinking of a number between 1 and 20, can you guess what it is?")

answer=input()

secretAnswer=random.randint(1,20)

tries=1

if secretAnswer>int(answer):
    print("That is too low.")

elif secretAnswer<int(answer):
    print("That is too high.")


elif answer==str(secretAnswer):
    print("Awesome, you guessed the correct answer on your first try!")
  

while str(secretAnswer)!=answer:
    tries=tries+1
    print("Please try again.")
    answer=input()

    if int(answer)==secretAnswer:
        print("Awesome, you guessed the correct answer in "+str(tries)+" tries")
        break

    elif secretAnswer>int(answer):
        print("That is too low.")

    elif secretAnswer<int(answer):
        print("That is too high.")
    


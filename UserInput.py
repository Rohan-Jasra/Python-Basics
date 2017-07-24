print ("Hello, what is your age?")

age=input()

print ("Excellent, you will be "+str(int(age)+1) +" next year.")

print ("What is your occupation if you don't mind me asking?")

occupation=input()

print ("Wow that's amazing! Do you enjoy being a "+occupation+"?"+" Please choose Yes or No.")

answer=input()

if answer=="Yes" or "yes":
    print("Awesome, I hope you get a raise soon!")
elif answer=="No" or "no":
    print ("That's okay, doing what we don't like can be a way to build discipline!")
else:
    print("You didn't choose Yes or No! Please run the program again")


#I need to figure out a way for my code to go back to the input if I get an answer outside of Yes or No

eggs=1
print(eggs)

def spam():
    global eggs
    eggs=5
    print(eggs)

spam()

eggs=1

spam()

print(eggs)
eggs=1
print(eggs)

#the above global statement in the function lets the function know to create the variable eggs in the global enviornment
#when we first call the function, 5 is printed because the global statement allowed us to modify the variable inside the function and didn't create it locally
#we reassign the variable eggs to equal 1
#the function is called again but the value returned is still 5-->This is so because the function call jumps back to the line of code under the spam(): which assigned the variable eggs to a value of 5
#we then print eggs and it also returns 5 because of how the code was run in the previous function call
#the last print call will return 1 because the variable has been reassigned to a value of 1 and we are not jumping back and forth to the spam function to modify it

"""
def food():
    print(bacon)
    bacon=5

bacon=10
food()
"""

#the above example if run will produce an error saying that variable referenced before assignment
#even though the bacon variable has been created and set equal to 10, this is only true in the global enviornment
#however when the function is called, it checks for the variable in the local enviornment and the variable bacon doesn't exist


def food():
    global bacon
    print(bacon)
    bacon=5

bacon=10
food()

#the above will print 10 since the variable bacon is now called upon its value which is stored in the global enviornment

def hello(greeting,name='you',question=" What is your favourite pet?"):
    print(greeting+" "+ name+". How do you do?"+question+".")

hello('Howdy')
hello('Howdy','Bob')
hello('Howdy',question=' Who are you?',name='Bob')
#hello()

#the greeting is a required positional argument in the hello function. The function will not execute unless the required positional argument is passed
#the name is a keyword argument which is optional
#when calling a function, the positional argument must be passed before the keyword argument


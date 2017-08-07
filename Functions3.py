def hello(greeting):
    print(greeting+" Bob.")

hello('Hi')

def hello2():
    return "How do you do"

print(hello2())
hello(hello2())

#functions can accept other functions as inputs but the brackets should be there on the function being inputted as well
#the return value of the hello2 function then becomes the local variable greeting

def spam(divideby):
    return 42/divideby
    

print(spam(1))
print(spam(2))
#print(spam(0))
print(spam(10))

#the third print call above will cause our python program to crash which results in the fourth print call not being executed
#the error that is shown by the python program is ZeroDivisionError


def spam(divideby):
    try:
        return 42/divideby
    except ZeroDivisionError:
        print("Error: Can't divide by zero")

print(spam(30))
print(spam(0))
print(spam(5))

#When inside of a try coding block, any code that runs into an error will immediately skip to the except clause and then continue running as normal
#We didn't need to specify ZeroDivisionError in the except statement, however this makes exception handling easier when multiple errors can go wrong and different except clauses need to be used


def spam2(divideby):
    return 42/divideby


try:
    print(spam2(1))
    print(spam2(0))
    print(spam2(1))

except ZeroDivisionError:
        print("Error: Can't divide by zero")

#notice in the above that the code didn't execute the last print call because after it detected the error, it jumped to the except clause but never went back

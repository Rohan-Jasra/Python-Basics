language='Python'

if language=='Python':
    print("Good language choice!")

elif langauge=="Javascript":
    print("That's a good choice to!")

else:
    print("I suggest you pick up a language!")

#the if/elif/else will return a boolean value of true or false
#the code will check each statement in order that it is written, so because the above if statement returned True, the other 2 statements are ignored

age=100

if age==25:
    print("Nice!")

elif age>25:
    print("This will print")

elif age==100:
    print("This wont print")

else:
    print ("This won't print either")

#even though the third block of code is equal to exactly the age specified, that block never gets executed because the block before returned true
#the else block will only get executed if all blocks before returned false

a=[1,2,3]
b=[1,2,3]

print(a==b)
print(a is b)

print(id(a))
print(id(b))

#the "is" is a comparison operator which checks if one object in memory is the same as another object in memory--> memory essentially is the ID number that python assigns each variable

a=b
print(a is b)
print(a==b)

print(id(a))
print(id(b))

#because we made a==b, the id's of both are now equal to each other

#False values
    #False
    #None
    #Zero of any numeric type
    #Any empty sequence --> " ", (), [] (Empty string, empty list, empty tuple, empty list
    #any empty mapping --> {} (Dictionary)

#if any of the above values are passed in any conditional statements, the statement will be evaluated to false:

RJ=0

if RJ:
    print ("This wont print")
else:
    print ("This will print")

JR=[]

if JR:
    print ("This wont print")
else:
    print ("This will print")

AA=None

if AA:
    print ("This wont print")
else:
    print ("This will print")

#the above false check can be useful if you want to check whether a list/tuple/map/string is empty since if passed in a conditional; it will evaluate to false
    

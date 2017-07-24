"""
H E L L O   W O R L D
0 1 2 3 4 5 6 7 8 9 10
"""
message="Hello World"

print (len(message))

#the above will print 11 as there are 11 characters in the variable message and the len method returns the length of the string

print (message[8])

#the square bracket above acts as a index. The above will return r

print (message[0:5])
print (message[:5])

#the above will print Hello since the index specified in both calls to print are to the index 4

print (len(message[:5]))

#the above example highlights the subtle differences between the length size of strings snd how the index function works on strings
#the index function above will print every character from 0 upto but not including 5. However the length function will still return 5 as there are 5 characters--> 0 1 2 3 4 


print (message.lower())
print (message.upper())

#the above functions don't accept any arguments from what I tested which means I cant specify how many characters I want to classify as uppercase using the brackets

print (message.count("Hello"))
print (message.count("HELLO"))
print (message.count("l"))

#the above function simply counts how many times the argument in within the variable. Strings are case sensitive!

print (message.find("w"))
print (message.find("l"))
print (message.find("or"))

#the above function returns the first index number of the argument given and in the case that the argument given is not in the variable, it returns -1

message.replace("World","Universe")
print(message)
new_message=message.replace("World","Universe")
print (new_message)
print (message.replace("World","Universe"))

#the above replace function accepts 2 arguments, the first is the old string which will be replaced and the second argument is the new string. However, the first call to print will not print "Hello Universe"
#the reason is because the original variable message is still "Hello World". But if we assign the new replace method a variable and print that, we will get "Hello Universe"

greeting="Hello"
name="Jack"

sentence=f"{greeting}, Hows's is going {name}? Welcome!"
print (sentence)

#the above f method ida way to format string, curly brackets are used as placeholders for variables and things like commas and spaces can be included without using plus signs and extra quotation marks

print(dir(greeting))
#the above will print a directory of methods we can use to modify the the variable greeting

#print(help(str)) will print a detailed description of the methods that are used with strings

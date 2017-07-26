# Arithmetic operators

# Addition                3+2
# Subtraction             3-2
# Multiplication          3*2
# Division                3/2
# Floor division          3//2
# Exponent                3**2
# Modulus                 3%2

#floor division checks how many times the second number goes into the first

print (5//2)
print (17//3)

#the above will always return an integer (data type)

print (5/2)
print (17/3)

#the above will return a float which is a number that has a decimal(data type)

print (5%2)
print (6%2)
print (7%2)
print (8%2)

#the above operator is a modulus which divides the two numbers and returns the remainder
#since everything is divisble by the number 2 besides odd numbers, this is a good check to see if a number is even or odd
#all odd numbers when divided by 2 will have a remainder of 1

num=3

num=num+1

#the above will give me 4

print(num)

#the above is an operation called incrementing variables

print(abs(-25))
print (abs(42))
print (abs(-37.52))

#the abs function just removes the negative sign from the integer/float

print (round(-3.49))
print (round(-3.51))
print (round(7.4))

#we can even pass an argument to the round method/function which will then specify how many decimal places we want to round to

print (round(4.73647,3))
print (round (3.2,3))

#Comparison operators:

#Equal:                 3==2
#Not Equal:             3!=2   
#Greater Than:          3>2    
#Less Than:             3<2
#Greater or Equal:      3>=2
#Less or Equal:         3<=2

#1 equal sign is for assigning variables, 2 equal signs is for comparison
#the result of comparison will be booleans

num1=5
num2=7

print(num1==num2)
print(num1!=num2)
print(num1>num2)
print(num1<num2)
print(num1>=num2)
print(num1<=num2)

num3="5"
num4="7"

print(num3+num4)

#the above will give "57" as it is concatenating 2 strings
#if we wanted to "cast" the above strings and pass it as integers, we could do the following:

print (int(num3)+int(num4))

#or we could simply cast the variables as integers:

num3=int("5")
num4=int("7")

print(num3+num4)

#in this lesson, the principles we learned about were incrementing variables and casting variables (converting from 1 data type to another)



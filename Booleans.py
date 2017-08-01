#Boolean is a type of data which only has 2 values--> True or False
#True and False are keywords which can't be used to store variables
#True=42 will return an error

#However, True and False and be used like so:
#George=True
#in the above statement, the variable George contains the boolean value True
#https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response?noredirect=1&lq=1

George=True
print(George)

#Comparison operators

# == Equal to
# != Not equal to
# > greater than
# < less than
# <= less than or equal to
# >= greater than or equal to

#The result of using comparison operators in an expression will always return a boolean value. The expression will either be evaluated to True or False.

print (50==52)
print(47>=42)
print('Harry'=='Harry')
print(42==42.0)
print('42'==42)

#the integer 42 is different from the string 42 which is why the last comparison will return false
#double equal sign (==) is a comparison operator while a single equal sign (=) is used for assignment (variables)

eggcount=50

print (eggcount>=75)

#values stored in variables can be compared


#Boolean operators

#and :Only if all the conditions specified are true will the boolean value also be True
#or :If any one of the conditions specified is True, the boolean value returned will be True
#not : This can only be used on 1 expression and will return the opposite of the boolean value being tested

#boolean operators also have an order in which they are evaluated--> The not operator goes first, followed by and, then or.

print(2+2==4 and 2+2==4 or 3+2==4 and 3+2==4)

#the above will evaluate to true because one of the expressions seperated by the or operator are correct even though the other isn't


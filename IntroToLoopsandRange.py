name="Rohan"

for x in name:
    print("Looping")
    
#the variable x was created in the for loop above
#what actually is happening in the above statement is that the variable x is being iterated over each character in the variable name. Each time x is iterated, it prints "Looping"

for y in name:
    print (y)

for z in name:
    print ("One of the letters in my name is:"+" " +z)

#what's happening in the above 2 statements is that the variable y and z are iterating over each character in the variable name and since y/z become the character it loops over, it simply prints each character that y/z are assigned to

for z in name:
    print (x)
    
#what's happening in the above statement is that the variable z is looping over each character and will print the variable x
#Since the variable x has already been defined and the last character that it looped over was n which is the last letter of my name, printing x will simply print n


for a in range(5):
    print (a)
print ("end of loop")
#the above will simply print each number in the range of 5 as we know the variable a takes the place of each character that it iterates over. We also know the ultimate value of a will be the last character that it iterates over

print (a)

#the above will print 4 as it was the last character that the variable a iterated over

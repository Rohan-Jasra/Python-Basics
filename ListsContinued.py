#we can also remove values from our list by using the remove method

courses3=['Gym','Science','Art']

courses3.remove('Gym')

print (courses3)

popped=courses3.pop()

print(popped)
print(courses3)

#the pop method is also a way to remove items from the list, however, it will always remove the last item from the list
#another cool thing the popped method allows us to do is use it as a variable
#since the pop always removes the last item from the list, when we make a variable equal to the pop method; it will grab the item that it removed

cities=['Toronto','Mississauga','Oakville','Markham']
cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)

#the sort method puts our list in alphabetical order but we can also pass an argument reverse=True to sort it in the opposite order

cities_sort=sorted(cities)
print(cities_sort)

#sometimes we don't want to modify the original list but create a new one in its place which has the attributes we want. passing the sorted function into a variable and printing that variable will give us the result we want.

print(cities.index('Mississauga'))

#the above index method will give us the index of the argument we entered

print ('Toronto' in cities)
print ('NewYork' in cities)

#the in operator is used to check whether or not an item is on the list, it will return a boolean data type

for x in cities:
    print(x)

#the above for loop will print out the entire list

for index,x in enumerate(cities):
    print (index,x)

#the above loop in addition to returning the list, will also return the index associated with the item on the list

for index,x in enumerate(cities,start=8):
    print (index,x)

#the above enumerate function will allow us to pass an argument of start which will print out the list starting from the index we specify

cities_str=" " .join(cities)

print(cities_str)

#the .join function will turn a list into a string using any parameters that come before it, if we want a list to have its values seperated by hyphens, we would do:

cities_str2=" - ".join(cities)
print(cities_str2)

string_cities="Toronto Oakville Mississauga Markham"
list_cities=string_cities.split(" ")
print(list_cities)

#the split method allows us to turn a string into a list. The argument we pass into the split method will dictate what items are in the list
#in the above example, we passed a " " argument in the method which tells us that any item seperated by a space will become an item on the list

string_cities2="Toronto Oakville Mississauga-Markham"
list_cities2=string_cities2.split(" ")
print(list_cities2)

string_cities3="Toronto Oakville Mississauga  Markham"
list_cities3=string_cities3.split("  ")
print(list_cities3)


string_cities4="Toronto Oakville Mississauga Markham"
list_cities4=string_cities4.split("HELLO")
print(list_cities4)
#the above 3 examples further demonstrate that an item on the list is dictated by being seperated by a space (or whatever argument we pass on to the split method
#in the last example, we pass an argument which we know wont seperate any of our values in which case, the entire string is made into 1 item on a list


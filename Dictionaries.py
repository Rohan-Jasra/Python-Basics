#Dictionaries

#a pair consisting of a key and a value

student={'name':"John",'age':25,'courses':['Math','Compsci']}
print(student)
#name, age, courses are the key while the adjacent items are values
#keys can be any immutable data types like integers/strings
#the value can take on a lot of data type/structures like string/integer/floats/list

print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', "Not found"))

#the get method allows us to check whether a key is in the dictionary or not
#we can also pass a second argument in the get method which will return the message we want if the key isn't present

student['phone']='555-555-5555'
print(student)

#the above is how you add a key/value pair

student['name']="Ricky"
print(student)

student.update({'name':'Rohan','age':24,'phone':"999-999-9999",'height':5.9})
print(student)

#the update method is very helpful if you want to update multiple key/value pairs in the dictionary
#student.update method takes the dictionary as an argument and you simply enter the new values
#you can also add new key/value pairs using the update method

del student['age']
print(student)

courses=student.pop('courses')
print(student)
print(courses)

#we can use the del keyword by specificying a ket to remove pairs from the dictionary
#also, we can use the pop method to remove key and make a variable out of the popped key
#the item that will be returned when you access the popped variable will be the value side of the pair and not the key

print(len(student))

#we get a length of 3 because there are 3 key-value pairs remaining

print(student.keys())
print(student.values())
print(student.items())

#the above methods allow us to access the dictionary in different ways


for key in student:
    print(key)

#for value in student:
    #print(values)

#the above wont work because accesing the student dictionary will only print the keys as it doesn't recognize the values unless we pass a specific method
    
for value in student.values():
    print(value)


for key,value in student.items():
    print(key,value)

#the above are the different ways to loop through the dictionary

student['Name']=student.get('name')

print(student)

student.pop('name')
print(student)

#the above is 1 way to update a key in the dictionary, however the new pair will be at the last index of the dictionary








#Lists

courses= ['History', 'Math', 'Science', 'English']

print (len(courses))

print (courses[:2])

#we can use the index and len methods on lists
#to access the last item on a list, we can use -1 in the index method

print(courses[-1])

courses.append('Art')

#the append method can be used on a list to add to it, this will always place the appended value at the end

#if we wanted to add a value to the list at a certain index, we could use the insert method

courses.insert(0,'Physics')

#the insert function accepts 2 arguments, the first is the index location, second is the value being inserted

print(courses)

#we can even insert a list within a list

courses2=['Gym','CompSci']

courses.insert(0, courses2)

print (courses)

print (courses[0])

#however, if we want to merge 2 lists together, we will need to use the extend function. The extend function only accepts 1 argument, it is the value that the list is being extended by

courses.extend(courses2)

print (courses)

#we cant append 2 lists together contained in variables as it would create a list within a list similar to the insert method. 



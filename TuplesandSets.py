#lists are mutable
list1=["History", "Math", "Physics", "CompSci"]
list2=list1

print(list1)
print(list2)

list1.append("Art")

print(list1)
print(list2)


#by changing list 1, list 2 is also modified as list 2 is a mutable object

"""
tuple1=("History", "Math", "Physics", "CompSci")
tuple1.append("Art")
print(tuple1)

The above wont work if executed
"""
#tuples use round brackets and are inmutable. The methods that can be applied to lists can't be applied to tuples.
#however, other than being unmodfiable, tuples behave very similarily to lists and can be accessed/looped through
#the takeaway here is that if you want to structure items that can be easily modified->use lists, otherwise use tuples


#Sets

#sets are values that are unordered values without duplicates

set1={"Science", "Math","Art","History","Math"}
set2={"Science", "Math","CompSci","Gym"}
print(set1)
#it wont print the math duplicate

print("Math" in set1)
#returns a boolean value

print(set1.intersection(set2))
#the above will check what courses are in set 1 which are ALSO in set 2

print(set1.difference(set2))
#the above will check what courses are in set 1 which ARENT in set 2

print(set1.union(set2))
#the above will compile a set which contains all values from both sets (not including duplicates)

empty_list=list()
empty_tuple=tuple()
empty_set=set()

"""in this lesson, I learned:
        -Tuples can't be modified like lists
        -However, tuples can be accessed and looped through
        -Tuples use rounded brackets

        -Sets are unordered and ignore duplicates
        -Sets are optimized for checking whether a value exists
        -the following methods were learned: intersection, difference, union
        -The intersection method returns the values similar in both lists
        -The difference method returns the values of set which the method is being applied to and returns the differences against the set which the argument was passed on
        -Creating empty lists/tuples/sets using the built in function
        
"""


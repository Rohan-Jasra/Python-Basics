def hello(name):
    print("Hello " + name)
    x="Hi"

hello('Jim')
hello('Bob')
#print(name)


#in the above, I created a function by using the def keyword with the name hello which has the argument of name
#an argument simply stores a parameter/varibale. If we think of a variable as a box that contains some value, an argument is a box which houses the variable box (boxception)

#the third/fourth line of code is me calling the function hello
#a function call is simply typing in the name of the function followed by a parentheses and any arguments that a function accepts
#anytime a function gets defined, python skips over that code unless that function is called, in which case, python then goes back to whereever the function is and starts executing that code
#notice when I print the variable name, it gives an error. This is so because even though the last value the varibale name took on was Bob, it forgets that after that line of code is executed
#in other words, the parameter/variable box is taken out of the argument box when the code is done executing

def hello_func():
    return "Hello Function."

def hello_func2():
    print("Hello Function")

if hello_func()!=None:
    print("This will get printed")

if hello_func2()==None:
    print("This will also get printed")

#the above example demonstrates that a function without a return value takes on a special data type called None-->None data type represents the absence of a value
#the function hello_func stores a string value

#in the function hello(name), the variable(or parameter passed as an argument) name is a local scope variable
#a local scope is created whenever a function is called
#any variable outside the local scope or functions is known as a global scope variable

name='Hello'
print(name)

#the above is an example of a global scope variable
#the above print call further demonstrates that the values stored inside the variables in the local scope are forgotten once the local scope execution ends
#This is why the global and local scope can share the same variable name

#print(x)

#the hello(name) function has a variable called x inside it but this print call wont work on it because the global scope can't use any local scope variables

def food():
    eggs=99
    bacon()
    print(eggs)


def bacon():
    eggs=0

food()

#the above example illustrates that a local scope can't use variables in other local scopes
#what happend above is that the variable eggs was created in the local scope of food and set to 99, then the function bacon was called which also has the variable eggs at a value of zero
#calling bacon meant that a second local scope was created. We know from previous examples that when a function is done executing, any variables inside of it are destroyed and forgotten
#this is why 99 is printed because within the local scope of food, the variable eggs takes on 99

def test():
    print (testing)

testing="This will get printed"
test()
print(testing)

#the above example demonstrates that global variables can be read from a local scope



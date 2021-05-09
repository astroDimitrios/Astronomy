# © Dimitrios Theodorakis GNU General Public License v3.0 https://github.com/DimitriosAstro/Astronomy
# A brief intro to python (there is a Jupyter Notebook version of this code)
# Find more info at www.w3schools.com, www.python.org, www.learnpython.org
# Numpy section adapted from work by Ridwan Barbhuiyan (https://github.com/rbarbhuiyan)

# Welcome to another astronomy and python video. In this video we will explore 
# the basics of python and Numpy which is a python module.

# To get started open up a new .py file or head over to https://jupyter.org/try and select the python notebook option.
# Notebooks allow us to write up what we do in markdown (this is the text you see)
# They are an interactive way of coding in python
# click on file new notebook python 3

# you can change the filename by clicking on unititled at the top 
# remember to save regularly using the save button in the top left hand corner

# let's start by assigining a variable

# assigning a variable
a = 2
# assigning a float not an integer
a = 2.

# here we have assigned a to an integer and then a float.
# we have overwritten the value of a with the second line
# it's important to choose variable names carefully so this doesn't cause errors in your code

# now let's assign a string which is text

# assigning a string
b = "Hello World!"

# to print this in python we have to use the print() function
# in an interactive notebook typing just the variable name works too provided it's at the end of the code cell

# printing to the terminal
print('1 - My first print statement!')
print(b)

# Let's try some basic maths
# The asterik means times and a double asterik means to the power

# basic maths (times = *, exponential = **)
c = 2+2
d = 2-2
e = 2*2
f = 2/2
g = 2**2

# We can print text and numbers like so:
# this converts the number stored in c to a string and combines the two strings
print("2 - Numbers and Strings")
print("My number is: "+str(c))

# Let's have a look at the list data structure
# lists are constructed inside square brackets
myList = [1,2,3,4,5]
print("3 - My first list")
print(myList)

# to add something to your list we use the append() function
myList.append(6)
print("4 - Adding to my list")
print(myList)

# now let's create a tuple. a tuple is a (ordered and unchangeable) list
myTuple = (1,2,3,4)
print("5 - My first tuple")
print(myTuple)

# To access values in the list we can use square brackets with the index of the value we want
# The first value is given an index of 0
print("6 - Indexing my lists")
print(myList[0])
print(myList[1])

# a negative index starts at the end (-1 first)
print("7 - Negatice indices")
print(myList[-1])
print(myList[-2])

# getting multiple items from a list
# to get multiple values we can use slices
# this slice will get the values from index 0 up to but not including index 3
print("8 - Printing multiple items from a list")
print(myList[0:3])

# simple for loop
# for each item (i) in our list do this
# for loops are a great way to repeat operations over a list
# here we are looping over every value in our list and printing it
print("9 - A simple for loop")
for i in myList:
    print(i)

# import a library
# numpy is used for numerical computations and to create arrays which is an effieicnet way of storing data
# you normally do this at the start of your code
''' the as np means we don't have to type out numpy 
each time we want to use a numpy function'''
import numpy as np

# create a numpy array (generally faster than using lists)
# there are many ways to create numpy arrays
# one way is to use the arange() function
# notice the np shorthand for numpy
array1 = np.arange(1,11)
print("10 - My first numpy array")
print(array1)

# get the datatype of a variable
# we can check we made an array with the built in python type function
print(type(array1))

# notice the difference between that and the type for myList
# compare that ouput with what we get printing the type of our list
print(type(myList))

# for loops also work on arrays!
for i in array1:
    print(i*2)

# but we could have just made a new array like this then printed it
# multiply everything in the array by 2
array2 = array1*2
print("11 - maths on an array")
print(array2)
# other maths operations will also work on arrays and are performed elementwise

# create an array using linspace, int turns a float into an integer
# another way of creatin an aray is using linspace
# here we have defined the start, finish, and number parameters to pass to linspace
start = 0
finish = 5
step = 0.5
number = int((finish - start) / step) + 1

array3 = np.linspace(start, finish, number)
print("12 - A linspace array")
print(array3)

# you can create 2-D arrays full of zeros or ones
# you can also create arrays of zeros and ones
# these are two dimensional arrays The (2,2) specifies the shape of the array
array4 = np.zeros((2,2))
array5 = np.ones((2,2))

print("13 - Arrays of zeros and ones")
print(array4)
print(array5)

# accessing a 2-D array [row, column]
print("14 - Acessing the (2,2) element of an array")
print(array4[1,1])

# setting values in a 2-D array
array4[1,1] = 1
print(array4)

# numpy maths
print("15 - Maths with Numpy")
print(np.pi)
print(np.log(10))

'''
Over to you!

Task 1: Create a list with your top 3 favourite foods. Print the list.
Task 2: Print just your third favourite food.
Task 3: Create an array using arange of the numbers 1-4. Print the square of those numbers.
Task 4: Create a new 2-D array of zeros with size (3,3). Set the diagonals to 1 and print the array.
'''

# Solutions

print("\n") # newline command

print("Task 1")
food = ["loukomathes", "gyro", "opera cake"]
print(food)

print("Task 2")
print(food[2])

print("Task 3")
newArray = np.arange(1,5)
print(newArray)
print(newArray**2)

print("Task 4")
newZeros = np.zeros((3,3))
newZeros[0,0] = 1
newZeros[1,1] = 1
newZeros[2,2] = 1
newZeros[2,0] = 1
newZeros[0,2] = 1
print(newZeros)

print("Or")
# or the easier way using the built in function fill_diagonal
np.fill_diagonal(newZeros, 2) # fill the main diagonal
np.fill_diagonal(np.fliplr(newZeros), 2) # fill the other diagonal
print(newZeros)
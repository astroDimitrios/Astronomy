# © Dimitrios Theodorakis GNU General Public License v3.0 https://github.com/DimitriosAstro/Astronomy
# A brief intro to python (there is a Jupyter Notebook version of this code)
# Find more info at www.w3schools.com, www.python.org, www.learnpython.org
# Numpy section adapted from work by Ridwan Barbhuiyan (https://github.com/rbarbhuiyan)

# assigning a variable
a = 2
# assigning a float not an integer
a = 2.

# assigning a string
b = "Hello World!"

# printing to the terminal
print('1 - My first print staement!')
print(b)

# basic maths (times = *, exponential = **)
c = 2+2
d = 2-2
e = 2*2
f = 2/2
g = 2**2

# printing text and a number
# this converts the number stored in c to a string and combines the two strings
print("2 - Numbers and Strings")
print("My number is: "+str(c))

# create a list of numbers
myList = [1,2,3,4,5]
print("3 - My first list")
print(myList)

# add to a list
myList.append(6)
print("4 - Adding to my list")
print(myList)

# create a tuple (ordered and unchangeable)
myTuple = (1,2,3,4)
print("5 - My first tuple")
print(myTuple)

# accessing items in a list
# the index starts at 0!
print("6 - Indexing my lists")
print(myList[0])
print(myList[1])

# a negative index starts at the end (-1 first)
print("7 - Negatice indices")
print(myList[-1])
print(myList[-2])

# getting multiple items from a list
print("8 - Printing multiple items from a list")
print(myList[0:3])

# simple for loop
# for each item (i) in our list do this
print("9 - A simple for loop")
for i in myList:
    print(i)

# import a library
# numpy is used for numerical computations
# you normally do this at the start of your code
''' the as np means we don't have to type out numpy 
each time we want to use a numpy function'''
import numpy as np

# create a numpy array (generally faster than using lists)
array1 = np.arange(1,11)
print("10 - My first numpy array")
print(array1)

# get the datatype of a variable
print(type(array1))

# notice the difference between that and the type for myList
print(type(myList))

for i in array1:
    print(i*2)

# multiply everything in the array by 2
array2 = array1*2
print("11 - maths on an array")
print(array2)

# create an array using linspace, int turns a float into an integer
start = 0
finish = 5
step = 0.5
number = int((finish - start) / step) + 1

array3 = np.linspace(start, finish, number)
print("12 - A linspace array")
print(array3)

# you can create 2-D arrays full of zeros or ones
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
# #SIT320 Python Reference Sheet

# #Built in Data Types & Literals
# #Integers
# from asyncio import Condition


# num = 3
# #Floating Point Numbers
# pi = 3.14

# #Strings and Characters
# name = "Claire"

# # Creating a string
# my_string = "Hello, World!"

# # Accessing characters
# first_char = my_string[0]
# last_char = my_string[-1]

# # String operations
# length = len(my_string)
# uppercase = my_string.upper()
# lowercase = my_string.lower()
# concatenation = my_string + " How are you?"

# #Boolean
# is_valid = True
# is_false = False

# # Logical operators
# result = True and False
# result = True or False
# result = not True


# #Working with Strings
# #Assignment (giving a string a value)
# my_string = "Hello, World!"

# #Concatenation (joining strings)
# first_name = "Te"
# last_name = "Claire"
# full_name = first_name + " " + last_name

# #Comparison
# string1 = "fan"
# string2 = "table"

# result1 = string1 == string2  # False
# result2 = string1 < string2   # True


# #Construction from other types
# age = 30

# #str(): Converts a value into its string representation
# age_string = str(age)  # "30"

# #format(): Formats a string by substituting values into placeholders
# message = "I am {} years old.".format(age)  # "I am 30 years old."
# words = ["Hello", "World", "!"]

# #join(): Concatenates a sequence of strings using a specified delimiter
# joined_string = ", ".join(words)  # "Hello, World, !"


# #Simple Programming Statements
# #Constant declaration
# PI = 3.14159
# MAX_VALUE = 100

# #Variable declaration
# message = "Hello, World!"
# count = 10

# #Assignment
# x = 5
# name = "Claire"

# #Method call
# length = len("Hello")

# # Custom method call
# def greet(name):
#     print("Hello, " + name + "!")

# greet("Sarah")

# #Sequence of statements - grouped
# if Condition:
#     # Statement 1
#     # Statement 2
#     # ...
#     # Statement N

#Structured programming statements
#If statement
# if condition1:
#     # code block executed if condition1 is true
# elif condition2:
#     # code block executed if condition2 is true
# else:
#     # code block executed if all conditions are false


#Case statement
    #Use a combination of if, elif, and else statements to achieve similar 
    # functionality when dealing with multiple conditions

# #While loop
# while condition:
#     # code block executed while condition is true

# #Repeat loop
# while True:
#     # code block executed repeatedly
#     if condition:
#         break  # exit the loop when condition is true


# #For Loop
# for item in iterable:
#     # code block executed for each item in the iterable


#Declaring Methods
def greet(name):
    print("Hello, " + name + "!")

greet("Claire")


#Declare a method that returns data
def add(a, b):
    return a + b

result = add(3, 6)
print(result)  # Output: 9

#Pass by reference
def modify_list(my_list):
    my_list.append(4)  # Modifying the original list

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)  # Output: [1, 2, 3, 4]





#Boolean Operators and Other Statements
#Comparison: equal, less, larger, not equal, less
a = 5
b = 10

result1 = a == b  # False
result2 = a < b   # True

#Boolean: And, Or, and Not
x = 5
y = 10
z = 15

result1 = (x < y) and (y < z)  # True
result2 = (x > y) or (y < z)   # True
result3 = not (x > y)          # True

#Skip an iteration of a loop
for i in range(5):
    if i == 2:
        continue
    print(i)

#End a loop early
while True:
    user_input = input("Enter a number: ")
    if user_input == "quit":
        break
    print("You entered:", user_input)


#End a method:
def greet():
    print("Hello, World!")
    # End of method

greet()  # Method call


# Custom Types
#Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

# Creating an object (instance) of the class
claire = Person("Claire", 30)

# Accessing attributes and calling methods
print(claire.name)  # Output: John
claire.greet()      # Output: Hello, my name is Claire

#Enumerations
    #define a set of named values as a distinct type

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Using enum values
favorite_color = Color.BLUE
print(favorite_color)  # Output: Color.BLUE

#Structs
# Using a class as a struct-like structure
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
print(p.x, p.y)  # Output: 2 3

# Using namedtuple as a struct-like structure
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(2, 3)
print(p.x, p.y)  # Output: 2 3






#Arrays
#Declaration
# Declaration of an array using a list
my_array = [1, 2, 3, 4, 5]

#Access
    #Use the [] operator with index

my_array = [1, 2, 3, 4, 5]

first_element = my_array[0]   # Accessing the first element
second_element = my_array[1]  # Accessing the second element


#Loop with index i
my_array = [1, 2, 3, 4, 5]

for i in range(len(my_array)):
    element = my_array[i]
    print(element)

#For each loop
my_array = [1, 2, 3, 4, 5]

for element in my_array:
    print(element)



#Programs and Modules
#Creating a program
#File: my_program.py

def greet(name):
    print("Hello, " + name + "!")

greet("Claire")


# run the program in command prompt
# " python my_program.py "

#Using a class from a library
# Importing the datetime module
import datetime

# Using the datetime class from the datetime module
current_time = datetime.datetime.now()
print(current_time)



#Other Things
#Reading from Terminal
# Reading input from the terminal
name = input("Enter your name: ")
age = input("Enter your age: ")

# Printing the values entered
print("Hello, " + name + "! You are " + age + " years old.")
	
#Writing to Terminal
# Writing output to the terminal
print("Hello, World!")

#Comments
# This is a single-line comment

"""
This is a
multi-line
comment
"""

# This is an example of a comment within the code
x = 5  # Assigning a value to x








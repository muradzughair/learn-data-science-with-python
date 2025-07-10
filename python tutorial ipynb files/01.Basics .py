# ------------------------------------------------------------
# 1. Variables and print() Statement
# ------------------------------------------------------------

# a) Variables

# Creating variables in Python (no need to declare data types explicitly)
age = 19         # int
name = 'Murad'   # str
avg = 4.2        # float

# Using type() to display the variable's data type
print(type(age))   # <class 'int'>
print(type(name))  # <class 'str'>
print(type(avg))   # <class 'float'>

# Variables can be reassigned without error
a = 23
a = 45
print(a)  # Output: 45

# TypeError: you cannot add a string and an integer directly
# a = 1 + '1'  # ❌ This will raise an error

# b) print() Statement

# 1. Using '+' requires explicit type conversion and does not insert spaces
print('My name is ' + name + ' and I am ' + str(age) + ' years old.')

# 2. Using ',' automatically adds spaces and handles type conversion
print('My name is', name, 'and I am', age, 'years old.')

# 3. Using f-strings allows easy inline formatting
print(f"My name is {name} and I am {age} years old.")

# Preventing newline at the end of print
print('Hello', end='')

# ------------------------------------------------------------
# 2. Math in Python
# ------------------------------------------------------------

# a) Arithmetic Operations

a = 5
b = 2
result = a / b      # Division always returns a float (2.5)
print(result)

# Floor division returns the integer part of the result
print(7 // 3)       # Output: 2

# b) Logical Operators

# Logical AND
print(10 > 0 and 5 > 0)  # True

# Logical OR
print(-3 > 0 or 7 > 0)   # True

# Logical NOT
x = False
print(not x)             # True

# c) Comparison Operators

# Chained comparisons
result = 10 > 5 and 10 < 20
result = 20 > 10 > 5     # Valid and returns True

# d) Arithmetic Assignment Operators

friends = 10
friends = friends + 2
friends += 2

friends = friends - 2
friends -= 2

friends = friends * 2
friends *= 2

friends = friends / 2
friends /= 2

friends = friends ** 2   # Exponentiation
friends **= 2

friends = friends % 2    # Modulo

# e) Built-in Math Functions

a = -7
x = 3.14
y = 4
z = 5

print(round(x))        # 3 — Rounds to nearest integer
print(abs(a))          # 7 — Absolute value
print(pow(2, 3))       # 8 — 2 to the power of 3
print(max(x, y, z))    # 5 — Maximum value
print(min(x, y, z))    # 3.14 — Minimum value

# f) Math Module

import math
x = 9

# Constants and common functions from math
print(math.pi)         # π = 3.14159...
print(math.e)          # e = 2.71828...
print(math.sqrt(x))    # Square root
print(math.ceil(x))    # Rounds up
print(math.floor(x))   # Rounds down

# ------------------------------------------------------------
# 3. Type Casting
# ------------------------------------------------------------

# Type casting = converting one data type into another

name = "Bro"
age = 21
gpa = 1.9
student = True

age = float(age)
print(type(age))       # <class 'float'>

gpa = int(gpa)
print(type(gpa))       # <class 'int'>

student = str(student)
print(type(student))   # <class 'str'>

name = bool(name)
print(type(name))      # <class 'bool'>

# ------------------------------------------------------------
# 4. User Input
# ------------------------------------------------------------


''''
IN python, input() function is used to take user input.
The input is always returned as a string, so you may need to convert it to the desired type.
Lets see some exersises to practice user input
'''''

# Exercise 1: Mad Libs — Fill-in-the-blanks game using user input

adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter an adjective: ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw {noun}.")
print(f"{noun} was {adjective2} and {verb}ing.")
print(f"I was {adjective3}!")

# Exercise 2: Area Calculator — Computes the area of a rectangle

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"The area is: {area} cm²")

# Exercise 3: Shopping Cart — Calculates total price

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}(s)")
print(f"Your total is: ${round(total, 2)}")

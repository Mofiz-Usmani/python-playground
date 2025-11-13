# ==========================
# Variables and Data Types
# ==========================


# immutable data type
a = 10
print(a)
print(type(a)) #Output: <class 'int'>

# immutable data type
b = 3.14
print(b)
print(type(b)) #Output: <class 'float'>

# immutable data type
c = "Hello, World!"
print(c)
print(type(c)) #Output: <class 'str'>


d = True
print(d)
print(type(d)) #Output: <class 'bool'>

# Ordered collection of values (mutable)
e = [1, 2, 3, 4, 5]
print(e)
print(type(e)) #Output: <class 'list'>


# Immutable sequence of values
f = (1, 2, 3) 
print(f)
print(type(f)) #Output: <class 'tuple'>


# Key-value pairs (mutable)
g = { "name": "Alice", "age": 30 }
print(g)    
print(type(g)) #Output: <class 'dict'>


# Unordered collection of unique values (mutable)
h = {1, 2, 3, 4, 5}
print(h)
print(type(h)) #Output: <class 'set'>


i = None
print(i)
print(type(i)) #Output: <class 'NoneType'>


# used to represent complex numbers like 2 + 3j to use in mathematical calculations
j = complex(2, 3)
print(j)
print(type(j)) #Output: <class 'complex'>


# ==========================
# Type Conversion
# ==========================

x = 5          # int
y = 2.5        # float
z = "10"       # str
print(type(x), type(y), type(z)) #Output: <class 'int'> <class 'float'> <class 'str'>

# Converting int to float
x_float = float(x)
print(x_float)          #Output: 5.0
print(type(x_float))    #Output: <class 'float'>

# Converting float to int
y_int = int(y)
print(y_int)          #Output: 2
print(type(y_int))    #Output: <class 'int'>

# Converting str to int
z_int = int(z)
print(z_int)          #Output: 10
print(type(z_int))    #Output: <class 'int'>

# Converting str to float
z_float = float(z)
print(z_float)          #Output: 10.0
print(type(z_float))    #Output: <class 'float'>

# Converting int to str
x_str = str(x)
print(x_str)          #Output: "5"
print(type(x_str))    #Output: <class 'str'>






# =========================================
# Every thing in Python is an Object
# =========================================

# What “Everything is an object” means in Python

# In Python:

# An object is anything that stores data and can do things.
# Everything you use in Python is one of these objects — numbers, text, lists, functions, even your own programs are objects.

# 1. Objects have three things

# Identity: Who the object is (like its ID).

# a = 5
# print(id(a))  # prints a unique number identifying this object


# Type: What kind of object it is.

# a = 5
# print(type(a))  # <class 'int'> → it's an integer object


# Value: What it actually holds.

# a = 5
# print(a)  # 5

# 2. Objects can do things (Methods)

# Each object can have actions (functions attached to it) called methods.

# Example: a string object "hello" can do .upper(), .replace(), etc.

# name = "jackal"
# print(name.upper())  # JACKAL

# 3. Even functions, classes, and modules are objects

# Functions can be stored in variables:

# def greet():
#     print("Hi!")
# f = greet  # assign function to variable
# f()  # prints "Hi!"


# Classes are objects too, which is why you can create classes dynamically.

# 4. Why it matters

# Python treats everything uniformly.

# This makes the language flexible — you can:

# Pass functions as arguments

# Store objects in lists or dictionaries

# Add attributes to objects dynamically



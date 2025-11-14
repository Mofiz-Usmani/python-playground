# ===============
# Type Casting
# ===============


a = "1"
b = "2"
print(a + b)  # Output: "12" (string concatenation)

print(int(a) + int(b))  # Output: 3 (integer addition)

c = "1Alex"
d = "2"
# print(int(c) + int(d))  # Raises ValueError: invalid literal for int() with base 10: '1Alex'



# Python automatically converts
# a to int
a = 7
print(type(a))

# Python automatically converts b to float
b = 3.0
print(type(b))

# Python automatically converts c to float (float addition)
c = a + b
print(c)
print(type(c))





# Explicit Type Casting (Done by User)

x = 1       # int
y = 2.8     # float
z = "3"     # str

# convert from int to float
a = float(x)
print(a)  #Output: 1.0
print(type(a))  #Output: <class 'float'>

# convert from float to int
b = int(y)
print(b) #Output: 2
print(type(b))  #Output: <class 'int'>

# convert from string to int
c = int(z)
print(c)  #Output: 3
print(type(c))  #Output: <class 'int'>


# convert from string to float
d = float(z)
print(d)  #Output: 3.0
print(type(d))  #Output: <class 'float'>








# Implicit Type Casting (Done by Python Interpreter)

x = 5       # int
y = 2.0     # float
z = 3j      # complex

# int to float
a = x + y
print(a)  #Output: 7.0
print(type(a))  #Output: <class 'float'>


# float to complex
b = y + z
print(b)  #Output: (2+3j)
print(type(b))  #Output: <class 'complex'>


# int to complex
c = x + z
print(c)  #Output: (5+3j)
print(type(c))  #Output: <class 'complex'>


# Mixed Type Expressions
x = 5       # int
y = 2.0     # float 
z = 3j      # complex

a = x + y + z
print(a)  #Output: (7+3j)
print(type(a))  #Output: <class 'complex'>
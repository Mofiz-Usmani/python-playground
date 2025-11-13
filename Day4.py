# ==========================
# Variables and Data Types
# ==========================



a = 10
print(a)
print(type(a)) #Output: <class 'int'>

b = 3.14
print(b)
print(type(b)) #Output: <class 'float'>

c = "Hello, World!"
print(c)
print(type(c)) #Output: <class 'str'>

d = True
print(d)
print(type(d)) #Output: <class 'bool'>

e = [1, 2, 3, 4, 5]
print(e)
print(type(e)) #Output: <class 'list'>


f = (1, 2, 3)
print(f)
print(type(f)) #Output: <class 'tuple'>


g = { "name": "Alice", "age": 30 }
print(g)    
print(type(g)) #Output: <class 'dict'>


h = {1, 2, 3, 4, 5}
print(h)
print(type(h)) #Output: <class 'set'>


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


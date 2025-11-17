# =====================
# Functions in Python
# =====================


# A function is a block of code that:
# ✔ has a name
# ✔ runs only when you call it
# ✔ helps avoid repeating code



# Simple function
def greet():
    print("Hello!")

greet()





# Function with Parameters
# Parameters = input values.

def add(a, b):
    print(a + b)


add(5, 3)







# Function with Return Value
# return sends back a result.

def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)
# or
# print(multiply(4,5))









# Default Parameters
# If user doesn’t give value, default is used.

def greet(name="User"):
    print("Hello", name)

greet()         # uses default "User"
greet("Eddie")  # uses provided value












# Function with Multiple Returns
def calc(a, b):
    return a+b, a-b, a*b

x, y, z = calc(10, 5)

print("Addition:", x)
print("Subtraction:", y)
print("Multiplication:", z)









# ===============================
# BUILT-IN FUNCTIONS IN PYTHON
# ===============================

# These are functions that Python already provides.
# You don’t need to create them — just use them directly.

# Examples:
# print(), len(), type(), range(), input(), etc.








def is_palindrome():
    s = input("Enter a string: ")
    temp = ""
    for i in range(len(s)-1, -1, -1):
        temp += s[i]
    if temp == s:
        print("Palindrome")
    else:
        print("Not Palindrome")

is_palindrome()

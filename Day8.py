#==================
# Input Functions
#==================



# a = input("Enter something: ")
# print(a)
# print(type(a))   #Output: <class 'str'> By default, input() returns a string.


# b = int(input("Enter an integer: "))   # Convert input string to integer
# c = int(input("Enter another integer: "))  # Convert input string to integer
# b = b + c
# print(b)   #Output: Sum of two integers





# d = float(input("Enter a float number: "))  # Convert input string to float
# e = float(input("Enter another float number: "))  # Convert input string to float



A = input("Enter first number: ")
B = input("Enter second number: ")
print(int(A) + int(B))  # Convert inputs to integers and add
print(float(A) + float(B))  # Convert inputs to floats and add





# Take Multiple Input in Python

x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)




x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
# #==================
# # Input Functions
# #==================



# # a = input("Enter something: ")
# # print(a)
# # print(type(a))   #Output: <class 'str'> By default, input() returns a string.


# # b = int(input("Enter an integer: "))   # Convert input string to integer
# # c = int(input("Enter another integer: "))  # Convert input string to integer
# # b = b + c
# # print(b)   #Output: Sum of two integers





# # d = float(input("Enter a float number: "))  # Convert input string to float
# # e = float(input("Enter another float number: "))  # Convert input string to float



# A = input("Enter first number: ")
# B = input("Enter second number: ")
# print(int(A) + int(B))  # Convert inputs to integers and add
# print(float(A) + float(B))  # Convert inputs to floats and add





# # Take Multiple Input in Python

# x, y = input("Enter two values: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)




# x, y, z = input("Enter three values: ").split()
# print("Total number of students: ", x)
# print("Number of boys is : ", y)
# print("Number of girls is : ", z)








# Dynamic Typing : 

# Python variables are dynamically typed, meaning the same variable can hold 
# different types of values during execution.

x = 10
x = "Now a string"
print(x)  #Output : Now a string






# Multiple Assignments : 
# Python allows multiple variables to be assigned values in a single line.

# Assigning the Same Value
# Python allows assigning the same value to multiple variables in a single line, 
# which can be useful for initializing variables with the same value.

a = b = c = 100
print(a, b, c)    #Output : 100 100 100




# Assigning Different Values
# We can assign different values to multiple variables simultaneously, making the-
# code concise and easier to read.

x, y, z = 1, 2.5, "Python"
print(x, y, z)    #Output : 1 2.5 Python




import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords are : ")
print(keyword.kwlist)










# ===============
# Questions : 
# ===============


# Take two numbers as input from the user and print their sum, difference,
# product, and quotient.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

a = input("Enter first number: ")
b = input("Enter second number: ")

print("Sum is : ", int(a) + int(b))
print("Differnce is : ", int(a) - int(b))
print("Product is : ", int(a) * int(b))
print("Quotient is : ", int(a) / int(b))









#? Ask the user to enter two integers and one float. Convert them all to floats
#? and print their average.

a = float(input("Enter the first value: "))
b = float(input("Enter the second value: "))
c = float(input("Enter the third value: "))

average = (a + b + c) / 3
print(average, type(average))







#? Evaluate and print the result of the following expression:

x = 10 + 3 * 2 ** 2
print(x)











#? Write a program to swap values of two numbers entered by the user.

a = int(input("Enter number a : "))
b = int(input("Enter number b : "))


print("Before Swap a : ",a)
print("Before Swap b : ",b)


temp = a
a = b
b = temp

# a, b = b, a


print("After Swap a : ",a)
print("After Swap b : ",b)













#? Ask the user for a temperature in Celsius (string input). Convert it to ,
#? then calculate and print temperature in Fahrenheit.
#? Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) + 32


celsius = input("Enter a temperature in Celsius : ")

celsiusTemp = int(celsius)

fahrenheitTemp = (celsiusTemp * (9/5)) + 32

print("Temperature in Fahrenheit : ",fahrenheitTemp)










#? Take a decimal number as input (like ) and output its:
#? • integer part - 45
#? • fractional part - .78



num = float(input("Enter a decimal number: "))

integer_part = int(num)
fractional_part = num - integer_part

print("Integer part:", integer_part)
print("Fractional part:", fractional_part)

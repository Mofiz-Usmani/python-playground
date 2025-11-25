# ==============================
# Exception Handling in Python
# ==============================



num = input("Enter the Number: \n")

print(f"Multiplication Table of {num} is : \n")


try:
    for i in range(1, 11):
        print(f"{int(num)} X {i} = {int(num)*i}")
except Exception as e: 
    print(e)



print("End of Program!!!")






# Multiple Exceptions : Handles different exceptions separately.

try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input, enter a number")








# Catching All Exceptions: 

# Exception catches any exception.
# e stores the exception message.

try:
    x = int("abc")
except Exception as e:
    print("Error:", e)
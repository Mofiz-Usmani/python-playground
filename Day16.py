# ====================
# Recursion in Python
# ====================


# Recursion is when a function calls itself to solve a smaller version of the same problem.

# It keeps calling itself until it reaches a base case (a stopping condition).
# Without a base case, it will go infinite loop → crash.




def factorial(num) :
    if (num == 1 or num == 0) :
        return 1
    else : 
        return (num * factorial(num - 1))


num = 5
print("Factorial: ",factorial(num))
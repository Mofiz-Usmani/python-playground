# ====================
# Recursion in Python
# ====================


# Recursion is when a function calls itself to solve a smaller version of the same problem.

# It keeps calling itself until it reaches a base case (a stopping condition).
# Without a base case, it will go infinite loop → crash.



# Factorial of a number: 
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: multiply n with factorial of (n-1)
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120








# Sum of first n natural numbers: 
def sum_natural(num):
    if num == 0:
        return 0
    else:
        return num + sum_natural(num-1)

print(sum_natural(5))


# =====================
# Lists in Python
# =====================
# A list is a collection of items in a particular order.
# ✔ Ordered
# ✔ Changeable (mutable)
# ✔ Allows duplicate elements
# ✔ Can contain different data types (numbers, strings, etc.)



# ---------------------
# 1. Creating Lists
# ---------------------
# Empty list
my_list = []
print("Empty list:", my_list)





# List with elements
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)





# Mixed data types
mix = [1, "hello", 3.5, True]
print("Mixed list:", mix)






# ---------------------
# 2. Accessing Elements
# ---------------------
fruits = ["apple", "banana", "cherry"]

print("First element:", fruits[0])   # Index 0
print("Last element:", fruits[-1])   # Negative index
# or
print("Last element:", fruits[len(fruits)-1])  
print("All elements: ", fruits[:])   # Prints all elements





# TO check if element present in list using (in) keyword
if "apple" in fruits:
    print("YES")
else : 
    print("NO")







# ---------------------
# 3. Slicing Lists
# ---------------------
numbers = [10, 20, 30, 40, 50, 60]

print("")
print("First 3 elements:", numbers[:3])
print("From index 2 to 4:", numbers[2:5])
print("Every 2nd element:", numbers[::2])
print("Reversed list:", numbers[::-1])
print("Jump Index: ", numbers[0:5:2])   #skip one value 









# =====================
# List Comprehension
# =====================

# A compact way to create lists.

# Can replace loops and append() calls.

# Format:
# [expression for item in iterable if condition]

# expression → what you want in the new list
# item → each element from the iterable
# condition (optional) → filter elements


evens = [i for i in range(10)]
print(evens)   



# With Condition (Filter)
# Only even numbers
evens = [i for i in range(10) if i % 2 == 0]
print(evens)   # Output: [0, 2, 4, 6, 8]






# Simple Example: Create a list of squares
# Without list comprehension
squares = []
for i in range(5):
    squares.append(i**2)
print(squares)   # Output: [0, 1, 4, 9, 16]




# With list comprehension
squares = [i**2 for i in range(5)]
print(squares)   # Output: [0, 1, 4, 9, 16]





lst = [i*i for i in range(10)]
print("List : ",lst)



lst = [i*i for i in range(10) if i%2==0]
print(lst)

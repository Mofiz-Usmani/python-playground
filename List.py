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
print(type(fruits), fruits)




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









# ====================
# List Comprehension
# ====================

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












# --------------
# List Methods
# --------------

# Adding Elements

fruits = ["apple", "banana"]

fruits.append("cherry")      # Add at end
print("After append:", fruits)

fruits.insert(1, "orange")   # Add at specific position
print("After insert:", fruits)

fruits.extend(["kiwi", "mango"])  # Add multiple elements
print("After extend:", fruits)






# Removing Elements

fruits = ["apple", "banana", "cherry", "banana"]

fruits.remove("banana")      # Remove first occurrence
print("After remove:", fruits)

popped_item = fruits.pop()   # Remove last element and return it
print("Popped item:", popped_item)
print("After pop:", fruits)

del fruits[0]                # Remove by index
print("After del:", fruits)

fruits.clear()               # Remove all elements
print("After clear:", fruits)






# List Operations

a = [1, 2, 3]
b = [4, 5, 6]

print("Concatenate:", a + b)      # Combine lists
print("Repeat:", a * 3)           # Repeat list
print("Check membership:", 2 in a)  # True or False







# Useful List Methods

numbers = [5, 2, 9, 1, 5, 6]

print("Length:", len(numbers))     # Number of elements
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))

numbers.sort()                     # Sort ascending
print("Sorted:", numbers)

numbers.sort(reverse=True)         # Sort descending
print("Reverse sorted:", numbers)

numbers.reverse()                  # Reverse order
print("Reversed:", numbers)

print("Index of 5:", numbers.index(5))  # First occurrence

print("Count of 5:", numbers.count(5))  # Number of occurrences





lis = [1, 2, 3, 4, 5, 6]
lis.reverse()
print("Reverse Order:", lis)







# copy() Method in Python (List Copy)

lis = [1, 2, 3]

new_lis = lis.copy()

print(lis)       # [1, 2, 3]
print(new_lis)   # [1, 2, 3]






# Proof that copy() creates a NEW list

lis = [1, 2, 3]
new_lis = lis.copy()

new_lis.append(99)

print(lis)       # [1, 2, 3]
print(new_lis)   # [1, 2, 3, 99]

# Old list did NOT change
# New list changed







# If you use = (assignment)

lis = [1, 2, 3]
new_lis = lis

new_lis.append(99)

print(lis)       # [1, 2, 3, 99]  (changed!)
print(new_lis)   # [1, 2, 3, 99]


# Both change because they are pointing to the same object.









# ============
# Questions
# ============


#? Given a list of integers compute the average of all numbers in the list.

#? Input two lists of integers from the user. Merge them into one list and sort the
#? result.
#? Eg - list1 = [1, 2, 7] , list2 = [2, 4, 5]
#? result = [1, 2, 3, 54, 5, 7]


#? Given a list, print all elements that appear more than once in the list.

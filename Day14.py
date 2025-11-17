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






if "apple" in fruits:
    print("YES")
else : 
    print("NO")
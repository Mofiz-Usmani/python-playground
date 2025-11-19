# ==================
# Tuples in Python
# ==================


# A tuple is a collection of items just like a list, but once created—

# 👉 You cannot change it (no adding, removing, updating).
# 👉 That’s why it's called immutable.



# Creating Tuples
# ✔ Normal tuple
t = (1, 2, 3)

# ✔ Tuple without brackets (Python allows it)
t = 1, 2, 3

# ✔ Single value tuple (IMPORTANT)
t = (5,)   # comma is important

# t = (5)    # ❌ this is not a tuple, just a number


print(type(t))












# Accessing tuple elements
# Same like lists, using indexing:

t = ("apple", "banana", "mango")
print(t[0])   # apple
print(t[2])   # mango
print(t[-1])  # mango










# Tuple Slicing
# You can slice it just like a list:

nums = (10, 20, 30, 40, 50)
print(nums[1:4])   # (20, 30, 40)







# Tuple Methods
# Only 2 methods exist because tuple is fixed:

# ✔ count() → Counts how many times an element appears
t = (1, 2, 2, 3)
print(t.count(2))   # 2




# ✔ index() → Gives first index of an element
t = (10, 20, 30, 20)
print(t.index(20))   # 1
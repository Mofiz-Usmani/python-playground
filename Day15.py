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
# ================
# Set in Python
# ================


# A set is a collection of items where:

# No duplicates allowed
# Order is not fixed (items can appear in any order)
# You can add or remove items
# Uses { } curly braces
# Set are 

# Think of a set like a bag of unique items. If you try to add the same item again, Python ignores it.


my_set = {1, 2, 3, 4}
print(my_set)
print(type(my_set))





# If you add duplicates: Python removes the duplicate 2.
s = {1, 2, 2, 3}
print(s)   # output: {1, 2, 3}








# ✔ Sets are MUTABLE

# You can add, remove, and change items inside a set.

s = {1, 2, 3}
s.add(4)
print(s)   # {1, 2, 3, 4}






# ❌ But the items inside a set must be IMMUTABLE

# You cannot put a list or another set inside a set because they are changeable.

# ✔ Allowed items: numbers, strings, tuples
# ❌ Not allowed: lists, sets, dictionaries

# s = {1, 2, [3, 4]}   # ❌ ERROR — list is mutable








# A frozenset is just like a normal set but:

# ❌ You cannot change it

# No add

# No remove

# No update

# ✔ Items are fixed forever → immutable set

fs = frozenset([1, 2, 3, 4])
print(fs)
print(type(fs))     #<class 'frozenset'>


# fs.add(5)     # ❌ Error
# fs.remove(2)  # ❌ Error










s = {}
print(type(s))   # <class 'dict'>  → NOT a set!

p = set()
print(type(p))   # <class 'set'>
p.add(1)
print(p)         # {1}
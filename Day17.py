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









# ================
# Sets Methods
# ================


# add() - Adds an item to the set (chages done in the original set)

s = {1, 2}
s.add(3)
print(s)   # {1, 2, 3}





# remove() - Removes an item from the set
# ⚠️ Gives error if item not found.

s = {1, 2, 3}
s.remove(2)
print(s)   # {1, 3}





# update() - Adds multiple items to the set

s = {1, 2}
s.update([3, 4, 5])
print(s)   # {1, 2, 3, 4, 5}





# discard() - Removes an item from the set
# ✔️ No error if item not found.

s = {1, 2, 3}
s.discard(5)   # no error
s.discard(2)
print(s)       # {1, 3}





# pop() - Removes a random item (because sets have no order).

s = {1, 2, 3}
item = s.pop()
print(item)  # could be 1, 2, or 3
print(s)  
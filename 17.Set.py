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










s = {}              # Empty curly braces create an empty DICTIONARY, not a set
print(type(s))      # <class 'dict'>

p = set()           # Correct way to create an empty set
print(type(p))      # <class 'set'>

p.add(1)            # Adds element 1 to the set
print(p)            # {1}


# {} → dictionary
# set() → empty set









# ================
# Sets Methods
# ================


# add() - Adds an item to the set (changes done in the original set)

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


h = {1, 2, 5, 6}
h2 = {3, 6, 7}
h.update(h2)
print(h)   # {1, 2, 3, 5, 6, 7}





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


l = {4,5,6,7}
l.pop()
print(l)


g = {10,20,30,40}
g.pop()
print(g)







# del - Deletes the entire set

s = {1, 2, 3}
del s
# print(s)   # ❌ Error: s is deleted








# clear() - Empties the set
s = {1, 2, 3}
s.clear()
print("Set s : ",s)   # set()







# Set Operations


# Union → Combine sets (no duplicates)

a = {1, 2}
b = {2, 3}
print(a | b)     # {1, 2, 3}
print(a.union(b))  # {1, 2, 3}






# Intersection → Common items

a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)     # {2, 3}
print(a.intersection(b))  # {2, 3}






# Difference → Items in A but not in B

a = {1, 2, 3}
b = {3, 4}
print(a - b)     # {1, 2}
print(a.difference(b))  # {1, 2}









# symmetric_difference()

# This returns a NEW set with items that are NOT common in both sets.
# It does NOT change the original set.

a = {1, 2, 3}
b = {3, 4}

print(a.symmetric_difference(b))   # {1, 2, 4}
print(a)   # still {1, 2, 3}
print(b)   # still {3, 4}






# symmetric_difference_update()

# This updates the original set.
# It changes a itself and keeps only NOT common items.

a = {1, 2, 3}
b = {3, 4}

a.symmetric_difference_update(b)

print(a)   # {1, 2, 4}
print(b)   # still {3, 4}










# isdisjoint() Method


# ✔ What it checks?
# It checks whether two sets have NO common elements.

# ✔ Returns:

# True → if both sets do NOT share any element
# False → if they share at least one element

a = {1, 2, 3}
b = {4, 5, 6}

print(a.isdisjoint(b))   # True (no common elements)












# isSuperset() Method

# ✔ What it checks?
# It checks whether a set contains all elements of another set.
# ✔ Returns:
# True → if the set is a superset
# False → if it is NOT a superset


a = {1, 2, 3, 4, 5}
b = {2, 3}

print(a.issuperset(b))   # True (a contains all elements of b)
print(b.issuperset(a))   # False (b does not contain all elements of a)














# isSubset() Method

# ✔ What it checks?
# It checks whether all elements of a set are present in another set.

# ✔ Returns:
# True → if the set is a subset
# False → if it is NOT a subset

a = {1, 2}
b = {1, 2, 3, 4, 5}
print(a.issubset(b))   # True (all elements of a are in b)
print(b.issubset(a))   # False (not all elements of b are in a)
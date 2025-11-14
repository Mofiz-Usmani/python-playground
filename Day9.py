# ===============
# String
# ===============

# Strings are Immutable


name = "Jackal"
print(name)
print(type(name))   #<class 'str'>



print("He said, \"I want to eat an apple\"")


# to print multiline string 
print('''
Conditional Statements in Python

comments
Conditional statements in Python are used to execute certain blocks of code based
 on specific conditions. These statements help control the flow of a program, 
 making it behave differently in different situations.
''')




newName = "Alex"
print(newName[0])  
print(newName[1])
print(newName[2])
print(newName[3])

for char in newName:
    print(char)





# slicing (ending index is not inxluded)
# format : 
# string[start : end : step]

s = "Python"
print(s[0:2])    # Py
print(s[2:])     # thon
print(s[:3])     # Pyt
print(s[-3:])    # hon



# len() - for length
print(len(s))



#upper(), lower()
print("cat".upper())  # "CAT"
print("DOG".lower())  # "dog"




# strip() – removes spaces
m = "    hi     "
print(m.strip())




#  replace() - replaces teh value with new
z = "Hello, Jackal"
print(z.replace("Jackal", "Python"))




# split() – convert string → list
print("hi hello hey".split())   # ["hi", "hello", "hey"])




# join - 
print("-".join(["a","b","c"]))   # "a-b-c"
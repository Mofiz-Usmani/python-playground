# ==================
# Strings in Python
# ==================

# Strings are immutable (cannot change characters inside them)
name = "Jackal"
print(name)
print(type(name))   # <class 'str'



# Printing a string with quotes inside
print("He said, \"I want to eat an apple\"")


# Multi-line string using triple quotes
print('''
Conditional Statements in Python

Comments:
Conditional statements execute code only if certain conditions are True.
''')


# Accessing characters by index
newName = "Alex"
print(newName[0])  # 'A'
print(newName[1])  # 'l'
print(newName[2])  # 'e'
print(newName[3])  # 'x'


# Loop through each character in a string
for char in newName:
    print(char)



# ===================
# String Slicing
# ===================
# Format: string[start:end:step] ; end index not included
s = "Python"

print(s[0:2])    # Py
print(s[2:])     # thon
print(s[:3])     # Pyt
print(s[-3:])    # hon
print(s[:])      # Python (whole string)
print(s[0:len(s)-2])  # Pyth
print(s[-3:-1])  # ho
print(s[-4:-2])  # th


# Length of string
print(len(s))  # 6




# Changes done using methods create a new string orignal remains the same
v = "Hello"
k = v.upper()
print("k : ", k)
print("v : ", v)   #Orignal remains the same



# Convert to upper and lower case
print("cat".upper())  # CAT
print("DOG".lower())  # dog


# Remove spaces from start and end
m = "    hi     "
print(m.strip())  # hi
f = "!!!!Hello!!!!!!"
print(f.rstrip("!")) 


# Replace a substring with another (all occurence changes with new)
z = "Hello, Jackal"
print(z.replace("Jackal", "Python"))  # Hello, Python


# Split string into a list of words (str to list)
print("hi hello hey".split())  # ['hi', 'hello', 'hey']


# Join list of strings into one string with separator
print("-".join(["a","b","c"]))  # a-b-c


# Find the index of first occurrence of a character
g = "Hello"
print(g.find("e"))  # 1


# Count occurrences of a character
print("banana".count("a"))  # 3


# Check if string starts or ends with a substring
print("python".startswith("py"))  # True
print("python".endswith("on"))    # True

str1 = "Welcome to the Console !!!"

# endswith("to", 4, 10) → checks if substring from index 4 to 10 ends with "to"
print(str1.endswith("to", 4, 10))



# capitalize() turns first letter of the word to uppercase and else into lowercase
blogHeading = "introduction to Python Learning"
print(blogHeading.capitalize())
blogHeading = "introduction tO PythoN Learning"
print(blogHeading.capitalize())




# center() method is used to center-align a string within a specified width
text = "Hello"
print(text.center(11))

text = "Hello"
print(text.center(146, "*"))




# index() finds the position (index number) of the first occurrence of a substring-
# inside a string.
# If the substring is not found, it gives an error (ValueError).
text = "banana"
print(text.index("a"))  #output 1

# Find next occurrence
text = "banana"
print(text.index("a", 2)) #Output 3

# Using start and end
text = "Hello World"
# Searches "o" only in "World" part.
print(text.index("o", 5, 10))   #Output 7



text = "hello"
# print(text.index("z"))   # ERROR

 



# isalnum() is a string method in Python that checks if all characters in the string-
# are either alphabets (a–z, A–Z) or numbers (0–9).

s = "Hello123"
print(s.isalnum())   #Output True


s = "Hello 123"
print(s.isalnum())   #Output False


s = "12345"
print(s.isalnum())   #Output True






# isalpha() checks if all characters in the string are alphabets only (a–z or A–Z).
s = "Python"
print(s.isalpha())     #Output True


s = "Hello World"
print(s.isalpha())     #Output False 








# islower() checks if all the alphabetic characters in the string are lowercase.
s = "python"
print(s.islower())   #Output True


s = "Python" 
print(s.islower())   #Output False

#if only numbers the false if mix of num and lowercase letter then true





# isprintable() checks if all characters in a string are printable.
s = "Hello World!123"
print(s.isprintable())    #Output True



s = "Hello\nWorld"
print(s.isprintable())    #Output False

# Empty string is considered printable





# isspace() checks if all characters in a string are whitespace characters.
# Whitespace characters include: space ' ', tab \t, newline \n, carriage return \r, etc.

s = "     "
print(s.isspace())  #Output True


s = " \t  "
print(s.isspace())  #Output True


s = " hello "
print(s.isspace())  #Output False

# Empty string has no characters, so it’s not considered whitespace







# istitle() checks whether a string is in title case.
# A string is considered title case if each word starts with an uppercase letter and the remaining letters are lowercase.

s = "Hello World"
print(s.istitle())    #Output True



s = "hello World"
print(s.istitle())    #Output False







# isupper() checks whether all alphabetic characters in a string are uppercase.
s = "PYTHON"
print(s.isupper())    #Output True


s = "Python"
print(s.isupper())    #Output False

# Numbers with words do not affect the result








# swapcase() converts all lowercase letters to uppercase and all uppercase-
# letters to lowercase in a string.
s = "Hello World"
print(s.swapcase())   #Output hELLO wORLD


s = "python"
print(s.swapcase())   #Output PYTHON








# The title() method converts a string to title case:
# The first letter of each word becomes uppercase
# All other letters become lowercase


s = "pyTHon proGRAMMing"
print(s.title())    #Output Python Programming








# TO check if element present in string using (in) keyword
if "Har" in "Harry":
    print("YES")
else: 
    print("NO")




 





# ===================
# String Formatting
# ===================
name = "Eddie"

# f-string (best & modern)
print(f"Hello {name}")  # Hello Eddie


# format() method
print("Hello {}".format(name))  # Hello Eddie

letter = "Hey my name is {} and I am form {}"
country = "India"
name = "Jackal"

# print(letter.format(country, name)) #complicated way

print(f"Hello my name is {name} and I am form {country}")  #Better way


print(f"Hello my name is {{name}} and I am form {{country}}")  #To print as it is





price = 49.0999
txt = f"For only {price: .2f} dollars!"
print(txt)



num = f"{2 * 30}"    
print(num)            #So it prints "60" as text.



print(40*40)   #Python calculates 40 × 40 = 1600 and prints the number.




# Old-style formatting
print("Hello %s" % name)  # Hello Eddie



# Multi-line string
text = """This
is
multiline"""
print(text)


# Check if substring exists in string
print("py" in "python")  # True


# Concatenate strings
a = "Hello"
b = "World"
print(a + b)  # HelloWorld


# Repeat strings multiple times
print("Hi" * 3)  # HiHiHi
















# =====================
# DocStrings and PEP-8
# =====================

# A docstring is a description written inside triple quotes """ """ at the-
# start of a function or class to explain what it does.




# def add(a, b):
#     """This function adds two numbers and returns the result."""
#     return a + b

# help(add)   # Output: add(a, b)
#     # This function adds two numbers and returns the result.

# print(add(4,6))








def square(n):
    '''Takes in a number n, returns the 
    square of n'''
    print(n**2)

square(5)
print(square.__doc__)  #Takes in a number n, returns the square of n
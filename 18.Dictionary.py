# ======================
# Dictionary in Python
# ======================


# Dictionary Features

# Stores data as key : value
# Keys are unique
# Keys can be: string, number, tuple
# Values can be: anything (list, dict, int, string…)
# Order is preserved (Python 3.7+)
# Mutable (you can change values)





# Creating a Dictionary

my_dict1 = {"name": "Alice", "age": 25, "city": "New York"}  # Using curly braces {}
my_dict2 = dict(name="Bob", age=30, city="Los Angeles")  # Using dict() constructor with keyword arguments
my_dict3 = dict([("name", "Charlie"), ("age", 35), ("city", "Chicago")])  # Using dict() constructor with a list of tuples
print(my_dict1)
print(my_dict2) 
print(my_dict3)










# Accessing Values

print(my_dict1["name"])  # Accessing value using key (direct access, raises KeyError if key not found)
print(my_dict2.get("age"))  # Accessing value using get() method (safe access, returns None if key not found)
print(my_dict3.get("country", "USA"))  # Using get() with default value if key not found
print(my_dict1.keys())  # Getting all keys
print(my_dict2.values())  # Getting all values
print(my_dict1.items())  # Getting all key-value pairs as tuples


for key, value in my_dict1.items():  # Iterating through dictionary
    print(f"{key}: {value}")







# =======================
# Methods of Dictionary
# =======================


student = {
    "name": "Eddie",
    "age": 20,
    "course": "Python"
}


# keys() - Returns all keys.

print(student.keys())



# values() - Returns all values.

print(student.values())




# items() - Returns key–value pairs as tuples.

print(student.items())




# get(key) - Safely get a value without error.

print(student.get("name"))




# update() - Add or update values.

student.update({"age": 21})
print(student.get("age"))


emp1 = {12: 45, 13: 89, 14: 69}
emp2 = {22: 67, 33: 90}
emp1.update(emp2)
print(emp1)
print(emp2)





# pop(key) - Remove a key and return its value.

print(student.pop("course")) 
print(student)





# Add new key:

student["city"] = "Mumbai"
print(student)






# popitem() - Removes the last inserted key–value pair.

student.popitem()
print(student)






# clear() - Removes all items.

# student.clear()
# print(student)






#* del - 
# del is not a method, it is a keyword used to delete:

# a key-value pair
# the entire dictionary

my_dict4 = {'name': 'Alex', 'age': 24}
print(my_dict4)
del my_dict4["age"]
# del my_dict4
print(my_dict4)




# copy() - Creates a copy of dictionary.

new_dict = student.copy()
print(new_dict)






# fromkeys() - Creates dictionary with given keys and same value.
# keys → list/tuple/set of keys
# value → single value for all keys

a = dict.fromkeys(["a", "b", "c"], 0)
print(a)



# Change value:

a["a"] = 1
a["b"] = 2
a["c"] = 3
print(a)









# Loop keys:

for k in student:
    print("Keys : ", k)





# Loop values:

for v in student.values():
    print("Values : ", v)







# Loop key–value:

for k, v in student.items():
    print("Key : Value - ",k, v)











# ============
# Questions
# ============



#? Create a dictionary where:
#? • Keys = student names
#? • Values = marks (integer)
#? Write a menu-based program where user presses a key (’A’, ‘B’, ‘C’, ‘D’)
#? depending on the operation they want to perform on the dictionary:
#? 1. A - Add a student
#? 2. B - Update marks
#? 3. C - Search for a student
#? 4. D - Display all students and marks


# Given a list of words:
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# Create a dictionary that maps each word to its length.
# Example:
# {"apple": 5, "banana": 6, "kiwi": 4, ...}

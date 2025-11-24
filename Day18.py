# # ======================
# # Dictionary in Python
# # ======================


# # Dictionary Features

# # Stores data as key : value
# # Keys are unique
# # Keys can be: string, number, tuple
# # Values can be: anything (list, dict, int, string…)
# # Order is preserved (Python 3.7+)
# # Mutable (you can change values)





# # Creating a Dictionary

# my_dict1 = {"name": "Alice", "age": 25, "city": "New York"}  # Using curly braces {}
# my_dict2 = dict(name="Bob", age=30, city="Los Angeles")  # Using dict() constructor with keyword arguments
# my_dict3 = dict([("name", "Charlie"), ("age", 35), ("city", "Chicago")])  # Using dict() constructor with a list of tuples
# print(my_dict1)
# print(my_dict2) 
# print(my_dict3)










# # Accessing Values

# print(my_dict1["name"])  # Accessing value using key (direct access, raises KeyError if key not found)
# print(my_dict2.get("age"))  # Accessing value using get() method (safe access, returns None if key not found)
# print(my_dict3.get("country", "USA"))  # Using get() with default value if key not found
# print(my_dict1.keys())  # Getting all keys
# print(my_dict2.values())  # Getting all values
# print(my_dict1.items())  # Getting all key-value pairs as tuples


# for key, value in my_dict1.items():  # Iterating through dictionary
#     print(f"{key}: {value}")







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






# pop(key) - Remove a key and return its value.

print(student.pop("course")) 
print(student)
# =================
# OOPS in Python
# =================







#* Attributes and Methods:

# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand      # attribute
#         self.color = color      # attribute

#     def start(self):            # method
#         print(self.brand, "is starting...")

#     def drive(self):            # method
#         print(self.brand, "is driving...")


# my_car = Car("BMW", "Black")    # object created
# my_car.drive()
# my_car.start()
# print(my_car.color)
# print(my_car.brand)





#* Constructor

class Student:
    def __init__(self, name, age):   # constructor
        self.name = name              # attribute
        self.age = age                # attribute

# creating object
s1 = Student("Ali", 18)   # constructor runs automatically




class Student:
    name = "Alex"

stu1 = Student()
print(stu1.name)







#* Default Constructor

# A default constructor is when __init__() is written with NO parameters
# (or even if you don’t write __init__() at all).

class Student:
    def __init__(self):   # default constructor
        print("Object Created")

s1 = Student()   # constructor runs automatically


# Note: If you don’t write __init__(), Python gives a built-in empty default constructor.

# Example:

class A:
    pass

obj = A()   # also works → default constructor created by Python








#* Parameterized Constructor

# A parameterized constructor takes data (parameters) when the object is created.

# ➡️ Used when objects must have different values.


class Student:
    def __init__(self, name, age):   # parameterized constructor
        self.name = name
        self.age = age

s1 = Student("Alex", 18)
s2 = Student("John", 20)

print(s1.name, s1.age)  # Alex 18
print(s2.name, s2.age)  # John 20
# Each object stores its own values



# | Type                      | Meaning                            |
# | ------------------------- | ---------------------------------- |
# | Default Constructor       | No data taken; just creates object |
# | Parameterized Constructor | Takes values while creating object |






# Attributes : 

# An attribute is a variable that belongs to:

# an object (instance)  (obj.attribute)
# or
# a class               (Class.attribute)


# Types of attributes:

# 1. Instance attributes

# Belong to an object
# Defined using self
# Each object has its own copy


class Student:
    def __init__(self, name):
        self.name = name   # instance attribute

s1 = Student("A")
s2 = Student("B")






# 2. Class attributes

# Belong to the class
# Shared by all objects




class Student:
    college = "ABC College"   # class attribute


print(Student.college)





# Combined : 
class Student:
    # Class attribute: shared by all Student objects
    college_name = "ABC College"
    
    # Class attribute
    PI = 3.1

    def __init__(self, name, gpa):
        # Instance attribute: unique for each object
        self.name = name
        
        # Instance attribute: unique for each object
        self.gpa = gpa

        # Instance attribute with same name as class attribute
        # This will override the class attribute for THIS object only
        self.PI = 3.14


# Creating an object (instance) of Student class
stu1 = Student("Alex", 9.2)

# Accessing instance attribute
print(stu1.name)           # Alex

# Accessing class attribute using object (allowed but not recommended)
print(stu1.college_name)   # ABC College

# Accessing class attribute using class name (best practice)
print(Student.college_name)  # ABC College

# Accessing class attribute directly
print(Student.PI)          # 3.1

# Accessing instance attribute (overrides class attribute for this object)
print(stu1.PI)             # 3.14





# Key Difference

# | Feature              | Class Attribute | Instance Attribute       |
# | -------------------- | --------------- | ------------------------ |
# | Belongs to           | Class           | Object                   |
# | Memory               | One copy        | Separate copy per object |
# | Defined              | Inside class    | Inside `__init__`        |
# | Access best practice | `Class.attr`    | `object.attr`            |
# | Override             | No              | Yes (shadows class attr) |


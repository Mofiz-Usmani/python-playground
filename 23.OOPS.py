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



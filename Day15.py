# ==================
# Tuples in Python
# ==================


# A tuple is a collection of items just like a list, but once created—

# 👉 You cannot change it (no adding, removing, updating).
# 👉 That’s why it's called immutable.

# Why use tuples?
# ✔ Faster than lists
# ✔ Use less memory
# ✔ Good for data that should not change



# Creating Tuples
# ✔ Normal tuple
t = (1, 2, 3)

# ✔ Tuple without brackets (Python allows it)
t = 1, 2, 3

# ✔ Single value tuple (IMPORTANT)
t = (5,)   # comma is important

# t = (5)    # ❌ this is not a tuple, just a number


print(type(t))









tup = (1,2,3,"HEllo", True)

if True in tup:
    print("YES")








# Accessing tuple elements
# Same like lists, using indexing:

t = ("apple", "banana", "mango")
print(t[0])   # apple
print(t[2])   # mango
print(t[-1])  # mango










# Tuple Slicing
# You can slice it just like a list:

nums = (10, 20, 30, 40, 50)
print(nums[1:4])   # (20, 30, 40)







# Tuple Methods
# Only 2 methods exist because tuple is fixed:

# ✔ count() → Counts how many times an element appears
t = (1, 2, 2, 3)
print(t.count(2))   # 2




# ✔ index() → Gives first index of an element
t = (10, 20, 30, 20)
print(t.index(20))   # 1








# Tuple Packing & Unpacking

# ✔ Packing
t = ("Eddie", 21, "India")



# ✔ Unpacking
name, age, country = t
print(name)
print(age)
print(country)










# Nested Tuples
t = (1, 2, (3, 4))
print(t[2][0])   # 4
print(t[2][1])   # 4
print(t[0])      # 1
print(t[1])      # 2









# Converting tuple to list (if you want to edit it)

countries = ("Spain", "Italy", "India", "England", "Germany")

temp = list(countries)

temp.append("Russia")

temp.pop(3)

temp[2] = "Finland"

countries = tuple(temp)

print(countries)










countriess = ("Pakistan", "Afganistan", "Bangladesh", "ShriLanka")

countries2 = ("Vietnam", "India", "China")

southAsia = countriess + countries2

print(southAsia)
print(len(southAsia))














#KBC Question : 

questions = ["Who is known as the “Missile Man of India”?", "Which is the largest planet in our Solar System?", "What is the currency of Japan?",
"Who wrote the Indian national anthem “Jana Gana Mana”?", "Which river is known as the “Ganga of the South”?"]

answers = ["Dr. A.P.J. Abdul Kalam", "Jupiter", "Yen", "Rabindranath Tagore", "Kaveri River"]
i = 0

while True :
    print("Leta Start the Game!!!")
    print(questions[i])

    ans = input("Enter the correct answer")

    if (ans == answers[i]) :
        print("Right Answer")
        i = i + 1
        ans = input("Enter the correct answer")
    else : 
        print("Wrong Answers!!!")
        break

    
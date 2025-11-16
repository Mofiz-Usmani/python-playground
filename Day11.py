# ==================
# For Loop in Python
# ==================




# Example 1: Loop over a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)




# Example 2: Loop over a string
name = "Jackal"

for char in name: 
    print(char)






# Example 3: Loop with range()
# numbers from 0 to 4
for i in range(5):
    print(i)



# numbers from 1 to 5
for i in range(1, 6):
    print(i)






# Example 4: Sum of numbers using for loop
total = 0
for i in range(1, 6):
    total += i

print("Sum =", total)







# Example 5: Nested for loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)







# step → how much to increase or decrease each time
# step is optional → default is 1.

for i in range(0, 10, 2):     #Count 0 to 9 with step 2
    print(i, end=" ")  




# Count backwards using negative step
for i in range(10, 0, -1):
    print(i, end=" ")
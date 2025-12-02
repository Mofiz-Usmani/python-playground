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

















# =============
# Questions
# =============



#? Sum of all even numbers and sum of all odd numbers in a list
#? List → [1, 2, 3, 4, 5, 6]

nums = [1, 2, 3, 4, 5, 6]

odd = 0
even = 0

for i in range(0, len(nums)):
    if(nums[i]%2 == 0):
        even += nums[i]
    else:
        odd += nums[i]
    
print(f"Even = {even}")
print(f"Odd = {odd}")
    
# OR

nums = [1, 2, 3, 4, 5, 6]

even = sum(x for x in nums if x % 2 == 0)
odd = sum(x for x in nums if x % 2 != 0)

print(f"Even = {even}")
print(f"Odd = {odd}")










#? Count how many vowels are in a string
#? Input: "hello world" → Output: 3


str = "hello world"
count = 0


for i in range(len(str)):
    if str[i] == 'o':
        count += 1
    elif str[i] == 'e':
        count += 1
    elif str[i] == 'i':
        count += 1
    elif str[i] == 'a':
        count += 1
    elif str[i] == 'u':
        count += 1

print(count)
        


# OR


s = "hello world"
count = 0

for i in range(len(s)):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        count += 1

print(count)










#? Print sum of n natural numbers

n = int(input("Enter n = "))

sum = n * (n+1) // 2
    
print(sum)


# OR


n = int(input("Enter n = "))

sum = 0

for i in range(1, n+1):
    sum += i
    
print(sum)
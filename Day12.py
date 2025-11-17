# =====================
# While Loop in Python
# =====================


# When to use while loop

# Use while loop when:
# ✔ You don’t know how many times the loop should run
# ✔ You want to repeat until a condition becomes False
# ✔ Taking continuous user input
# ✔ Waiting for something to happen

# No Do While Loop is in python




i = 1

while i <= 5:
    print(i)
    i = i + 1






# Ask user until they enter correct password
# password = ""

# while password != "abc@123":
#     password = input("Enter Password: ")

# print("Access Granted")







# Infinite Loop (runs forever)
# while True:
#     print("This never ends!")










# i = int(input("Enter the number: "))

# while (i<=10) :
#     i = int(input("Enter the number: "))
#     print(i)

# print("Done with the loop")






count = 5

while (count>=0) :
    print(count)
    count -= 1
else : 
    print("Out of Loop")








# Print numbers 1 to 5 (do-while style)
i = 1

while True:
    print(i)
    i += 1

    if i > 5:     # condition check at bottom
        break






# Do While Loop emulation
# i = int(input("Enter the number: "))
# print(i)    

# while (i<=10) :
#     i = int(input("Enter the number: "))
#     print(i)

# print("Done with the loop")








# =============================
# BREAK and CONTINUE in Python
# =============================


# Break = Stop the loop immediately
# When Python sees break, it jumps out of the loop (loop ends right there).


for i in range(1, 6):
    if i == 3:
        break
    print(i) # prints 1 2







# Example with While Loop
i = 1

while i <= 5:
    if i == 4:
        break
    print(i)   #prints 1 2 3
    i += 1







for i in range(1, 13) : 
    if i == 11:
        break
    print("5 X",i, "=", 5 * i)
    







n = 5
num = int(input("Guess the number btwn (1-10): "))

while True : 
    if n == num :
        print("Right Guess")
        break
    else:
        num = int(input("Wrong!!! Guess Again: "))

print("Game Finished")



# Continue = Skip that iteration & jump to next round of loop
# It does not stop the loop.
# It only skips the current step.




for i in range(1, 6):
    if i == 3:
        continue
    print(i)    #prints 1 2 4 5  Number 3 is skipped.







i = 0

while i < 5:
    i += 1
    
    if i == 2:
        continue
    print(i)    #prints 1 3 4 5


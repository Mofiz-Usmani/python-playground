# ==================
# If Else in Python
# ==================



# age = int(input("Enter your Age: "))

# if(age >= 18) :
#     print("Can Vote and Drive")
# else :
#     print("Cant Vote and Drive")







marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")






# IF Without ELSE
num = 10

if num > 0:
    print("Positive number")






# IF Inside Another IF (Nested IF)
age = 20
country = "India"

if age >= 18:
    if country == "India":
        print("You can vote in India")








# Short IF (Ternary Operator)
age = 16

message = "Adult" if age >= 18 else "Minor"

print(message)

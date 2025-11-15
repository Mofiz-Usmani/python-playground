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










# Complex Even-Odd Conditions
n = int(input("Enter a number: "))

if(n%2 == 0 and n%6 == 0):
    print("Super Even")
elif(n%2 == 0 and n%6 != 0):
    print("Normal Even")
elif(n%2 != 0 and n%5 == 0):
    print("Special Odd")
else:
    print("Normal Odd")








import time

# get current hour (0–23)
hour = int(time.strftime('%H'))

print("Current Hour:", hour)

if hour >= 5 and hour < 12:
    print("Good Morning!")
elif hour >= 12 and hour < 17:
    print("Good Afternoon!")
elif hour >= 17 and hour < 21:
    print("Good Evening!")
else:
    print("Good Night!")








# match–case is like switch-case in other languages.
# It is used when you want to check many conditions in a cleaner way-
# instead of writing many if–elif–else
month = int(input("Enter the Month number(1-12): "))

match month: 
    case 12 | 1 | 2 :
        print("Winter")
    case 3 | 4 | 5:
        print("Spring") 
    case 6 | 7 | 8:
        print("Summer")
    case 9 | 10 | 11:
        print("Autumn")








marks = int(input("Enter your marks: "))

match marks:
    case m if m >= 90:
        print("Grade A")
    case m if m >= 75:
        print("Grade B")
    case m if m >= 50:
        print("Grade C")
    case _:
        print("Fail")

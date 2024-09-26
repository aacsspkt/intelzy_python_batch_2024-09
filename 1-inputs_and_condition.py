# name = input("Enter your name: ")
# print("name:", name)

# age = input("Enter your age: ")
# age = int(age)

# if age < 18:
#     print("You don't have NID")
# elif age >= 18 and age < 60:
#     print("You are adult with NID")
# else:
#     print("You have elder with NID")

# female = False
# male = False
# rainbow = True

# if (
#     male or 
#     female or 
#     rainbow
# ):
#     print("It's a human")
# else:
#     print("It may be alien")

"""
write a console progam that takes number as input from user where number must be within 0 - 100
and calculate division of the user and print the division.

you may use `input and print` function and `if, elif, else` keyword for condition and 
`and, or` keyword for chaining logics.

Division :
less than 40: Failed
40 - 49: Third
50 - 59: Second
60 - 79: First
80 - 100: Distinction

"""
# marks = int(input("Enter your marks: "))

# if marks >= 0 and marks <= 100:
#     if marks >= 80:
#         print("you got distinction")
#     elif marks >= 60 and marks < 80:
#         print("you got first division")
#     elif marks >= 50 and marks < 60:
#         print("you got second division")
#     elif marks >= 40 and marks < 50:
#         print("you got second division")
#     else:
#         print("you are failed")
# else:
#     print("Invalid marks input")


uninitialized = None

if not uninitialized:
    print("It is not initialized.", "ASADSD")

uninitialized = "Initialized"

if uninitialized:
    print("It is now initialized.")

first = 10
second = 40 - 30
if first == second:
    print("They are equal")

if first is second:
    print("They are equal")

second = 50 - 30

if first != second:
    print("They are not equal")

if first is not second:
    print("They are not equal")

print("")

name = "Ashish"
age= 26

# old way
# sentence = "Hi %s! You are %d years old." % (name, age)
sentence = f"Hi {name}! You are {age} years old."

print(sentence)
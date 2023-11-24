# YPPB PYTHON WORKSHOP
################################### DAY 1 ################################################

# print("Hello")

# PRINT SINGLE VARIABLE
# name = "John"
# print("Hello, " + name) # need to allocated space within the string (if needed)
# print("Hello,", name) # automatically a space created

# PRINT MULTIPLE VARIABLES
# name1 = "Ahmad"
# name2 = "Kamil"
# name3 = "Aiman"
# print("Hello, " + name1)
# print("Hello, " + name2)
# print("Hello, " + name3)
# print("Hello, " + name1 + ", " + name2 + ", " + name3)
# print(f"Hello, {name1}, {name2}, {name3}")

## IF ELIF ELSE
# number = 0
# if number > 5:
#     print("The number is positive and greater than 0")
# elif number == 0:
#     print("The number is equal to 0")
# else:
#     print("The number is negative and lower than 0")

# print("Youre done")

## INPUT
# gender = (input("Please enter your gender (F/M):")).upper()
# age = int(input("Please enter your age:"))

# if gender == "F":
#     if age > 0 and age <= 10:
#         print("You're a female kid.")
#     elif age > 10 and age <= 18:
#         print("You're a female teen.")
#     elif age > 18 and age <= 60:
#         print("You're an female adult.")
#     elif age > 60:
#         print("You're a female Senior Citizen.")
#     else:
#         print("Invalid age!!!") 
# elif gender == "M":
#     if age > 0 and age <= 10:
#         print("You're a male kid.")
#     elif age > 10 and age <= 18:
#         print("You're a male teen.")
#     elif age > 18 and age <= 60:
#         print("You're an male adult.")
#     elif age > 60:
#         print("You're a male Senior Citizen.")
#     else:
#         print("Invalid age!!!")
# else:
#     print("Invalid gender!!!") 

## FUNCTIONS
# def print_hello(name, gender, age):
#     print("Hello, my name is", name, "\b. I am", age, "years old", gender)

# print_hello("Ahmad", "male", 30)

## DEFAULT VALUE FOR FUNCTION PARAMETER
# def display_greetings(name, gender, age = 20):
#     print("Salam "+ name, gender, age)

# display_greetings("Flora", "Female", 12)
# display_greetings(gender = "Female", name = "Catherine", age = 25)
# display_greetings("Elias", "Male")

## UNKNOWN NUMBER OF PARAMETERS
# def display_skills(*skills):
#     print(skills)
#     print(type(skills))
#     print(skills[1])

# display_skills("Python", "C++", "CAD", "Java")


## RETURN OUTPUT
# def my_func(x):
#     print("\nThe result is:", end = " ")
#     return 5*x

# my_func(3)
# print(my_func(9))

## FINAL TASK (DAY 1)
# def user_input():
#     name = input("Enter your name: ").capitalize()
#     gender = input("Enter your gender (f/m): ").lower()
#     birth_year = input("Enter your birth year: ")
#     return name, gender, birth_year

# def display_info(name, gender, age):
#     if gender == "m":
#         gender = "male"
#     elif gender == "f":
#         gender = "female"
#     print("Your name is", name, "and you are", age, "years old", gender)

# name, gender, birth_year = user_input()

# age = 2023 - int(birth_year)
# display_info(name, gender, age)

# if gender == "f":
#     if age > 0 and age <= 10:
#         print("You're a female kid.")
#     elif age > 10 and age <= 18:
#         print("You're a female teen.")
#     elif age > 18 and age <= 60:
#         print("You're an female adult.")
#     elif age > 60:
#         print("You're a female Senior Citizen.")
#     else:
#         print("Invalid age!!!") 
# elif gender == "m":
#     if age > 0 and age <= 10:
#         print("You're a male kid.")
#     elif age > 10 and age <= 18:
#         print("You're a male teen.")
#     elif age > 18 and age <= 60:
#         print("You're a male adult.")
#     elif age > 60:
#         print("You're a male Senior Citizen.")
#     else:
#         print("Invalid age!!!")
# else:
#     print("Invalid gender!!!") 






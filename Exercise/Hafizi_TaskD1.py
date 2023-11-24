
## MUHAMMAD HAFIZI
## FINAL TASK (DAY 1)
def user_input():
    name = input("Enter your name: ").capitalize()
    gender = input("Enter your gender (f/m): ").lower()
    birth_year = input("Enter your birth year: ")
    return name, gender, birth_year

def display_info(name, gender, age):
    if gender == "m":
        gender = "male"
    elif gender == "f":
        gender = "female"
    print("Your name is", name, "and you are", age, "years old", gender)

name, gender, birth_year = user_input()

age = 2023 - int(birth_year)
display_info(name, gender, age)

if gender == "f":
    if age > 0 and age <= 10:
        print("You're a female kid.")
    elif age > 10 and age <= 18:
        print("You're a female teen.")
    elif age > 18 and age <= 60:
        print("You're an female adult.")
    elif age > 60:
        print("You're a female Senior Citizen.")
    else:
        print("Invalid age!!!") 
elif gender == "m":
    if age > 0 and age <= 10:
        print("You're a male kid.")
    elif age > 10 and age <= 18:
        print("You're a male teen.")
    elif age > 18 and age <= 60:
        print("You're a male adult.")
    elif age > 60:
        print("You're a male Senior Citizen.")
    else:
        print("Invalid age!!!")
else:
    print("Invalid gender!!!") 
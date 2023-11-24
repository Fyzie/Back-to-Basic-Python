## FINAL TASK (DAY 3)
'''
1. user input (birthday date)
2. calculate the age
3. save to the file
4. read from the file

- can use -
function
date
file handling
math
exception handling (optional)
'''
from datetime import date

try:
    # user input
    birth_day = int(input("Enter your birth day: "))
    birth_month = int(input("Enter your birth month: "))
    birth_year = int(input("Enter your birth year: "))

    birth_date = date(birth_year, birth_month, birth_day)
    formatted_birth_date = birth_date.strftime("%d %B %Y")

    # calculate age
    today = date.today()
    year_now = int(today.strftime("%Y"))

    age = year_now - birth_year
    # age = 2023 - birth_year

    # create and write file
    filename = "birthdate.txt"
    file = open(filename, "w")

    file.write(f"You were born on {formatted_birth_date} and your age now is {age}")

    file.close()

    # read file
    file = open(filename)

    print(file.read())

    file.close()

except Exception as e:
    print(f"An error detected: {e}")


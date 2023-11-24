################################### DAY 3 ################################################

## DATETIME

import datetime as dt
from datetime import date

## DATE NOW
# now = dt.datetime.now()

# print(now)
# print("Year\t:", now.year)
# print("Month\t:", now.month)
# print("Day\t:", now.day)
# print(now.weekday()) # day of the week (0-6, Mon-Sun)
# print(now.isoweekday()) # day of the week (1-7, Mon-Sun)
# print(now.isocalendar())

# print("-------------------------")

# one_date = date(2022, 9, 17) # year, month, day

# print(f"One date\t: {one_date}")

# print("-------------------------")
## CREATE DATE
# two_dates = [date(2023, 11, 21), date(2023, 12, 14)]

# print(two_dates[1])
# print(two_dates[1].year)
# print(two_dates[1].month)
# print(two_dates[1].day)
# print(two_dates[1].weekday())
# print(two_dates[1].isoweekday())
# print(two_dates[1].isocalendar())

# print("-------------------------")
## STRFTIME FORMAT CODES
# print("Weekday (short)\t: ", now.strftime("%a"))
# print("Weekday (long)\t: ", now.strftime("%A"))
# print("Weekday (0-6)\t: ", now.strftime("%w"))
# print("Day of month\t: ", now.strftime("%d"))
# print("Month (short)\t: ", now.strftime("%b"))
# print("Month (long)\t: ", now.strftime("%B"))
# print("Month (01-12)\t: ", now.strftime("%m"))
# print("Year (long)\t: ", now.strftime("%y"))
# print(now.strftime("%Y"))
# print(now.strftime("%H"))
# print(now.strftime("%I"))
# print(now.strftime("%p"))
# print(now.strftime("%M"))
# print(now.strftime("%S"))
# print(now.strftime("%f"))
# print(now.strftime("%z"))
# print(now.strftime("%Z"))
# print(now.strftime("%j"))
# print(now.strftime("%U"))
# print(now.strftime("%W"))
# print(now.strftime("%c"))
# print(now.strftime("%C"))
# print(now.strftime("%x"))
# print(now.strftime("%X"))
# print(now.strftime("%%"))
# print(now.strftime("%G"))
# print(now.strftime("%u"))
# print(now.strftime("%V"))

# print("-------------------------")
## DIFFERENT DATETIME FORMATS
# today = date.today() # date only
# timedate_today = dt.datetime.now() # date and time

# print(today.strftime("%d/%m/%y"))
# print(today.strftime("%m/%d/%y"))
# print(today.strftime("%B %m, %Y"))
# print(today.strftime("%b-%m-%Y"))

# print(timedate_today.strftime("%H:%M:%S"))
# print(timedate_today.strftime("%I:%M:%S %p"))
# print(timedate_today.strftime("%I:%M %p"))

# d1 = timedate_today.strftime("%d/%m/%Y, %I:%M %p")
# print("Day 1 = ", d1)

## FILE HANDLING
'''
import os 

def file_handling(file_name):
    print("\n------------- READ ----------------\n")

    file = open(file_name)

    print(file.read())
    # print(file.read(3))

    # print(file.readline())
    # print(file.readline())

    # for line in file:
    #     print(line)

    print("\n------------- APPEND ----------------\n") # ADD TEXT INTO EXISTING FILE

    file.close()

    file = open(file_name, "a")

    # file.write("""\nThis file is for demo class\nIt will show text""")
    file.write("""\nThis file is for demo class
It will show text""")

    file.close()

    file = open(file_name)

    print(file.read())

    file.close()

    print("\n-------- WRITE (OVERWRITE) ---------\n") # OVERWRITE EXISTING FILE

    file = open(file_name, "w")

    # file.write("Hello! Welcome to Python Workshop\nHave a nice day!!!")
    file.writelines("Hello! Welcome to Python Workshop")
    file.writelines("\nHave a nice day!!!")

    file.close()

    file = open(file_name)

    print(file.read())

    file.close()

def check_file(file_name):
    if os.path.exists(file_name):
        print("--The file does exist--")
        file_handling(file_name)
    else:
        print("The file does not exist!!")

file_name = "content.txt"
check_file(file_name)
os.remove(file_name)

print("\n-------- FILE IS REMOVED ---------\n")
import time
print("Checking", end = ".")
for i in range(5):
    print(".", end = "")
    time.sleep(1)
check_file(file_name)

print("\n-------- CREATE NEW FILE ---------\n")

new_file = open(file_name, "w")
new_file.write("This is the new file")
new_file.close()
new_file = open(file_name)
print(new_file.read())
new_file.close()
'''

## MATH LIBRARIES
'''
x = min(5, 10, 25)
y = max(5, 10, 25)
z = x + y
# print(f"{x} + {y} = {z}")
# print("{1} + {0} = {2}".format(x, y, z))

print(abs(-x))

print(pow(x, 2))

import math

print(math.sqrt(64))

print(math.ceil(1.4))
print(math.floor(1.9))

print(math.cos(180))
print(math.cosh(180))
print(math.sin(180))
print(math.sinh(180))
print(math.tan(180))
print(math.tanh(180))
print(math.log10(10))
print(math.log2(180))
print(math.remainder(5, 2)) # %

## MATCH CONSTANTS
print(math.pi)
print(math.tau)
print(math.e)       # Euler's number
print(math.inf)     # floating point positive infinity
print(math.nan)     # floating point NaN (not a number)
'''

## TRY EXCEPT
# try:
#     # code that might raise an exception
#     # print(k)
#     # results = 10/0 # this will raise a ZeroDivisionError
#     lists = [1, 2, 3]
#     num = lists[4]
#     x=1
# except NameError:
#     print("Error: Name is not defined")
# except ZeroDivisionError:
#     # code to handle the exception
#     print("Error: Division by zero")
# except Exception as error:
#     # generic 'except' block that can catch any exception
#     print(f"An error occured: {error}")
# else:
#     print("No error detected. Good !")
# finally:
#     print("End of 'try except' blocks")


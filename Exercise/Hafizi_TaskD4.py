## TASK DAY 4
student_record = {
    "M01" : {
        "name" : "James",
        "cgpa" : 2.9,
        },
    "M02" : {
        "name" : "Leon",
        "cgpa" : 3.5,
        },
    "M03" : {
        "name" : "Igris",
        "cgpa" : 2.2,
        },
    "M04" : {
        "name" : "Baron",
        "cgpa" : 3.7,
        }
    }

## EXERCISE 1: add new data (faculty) for student M03
student_record["M03"]["faculty"] = "Art"
print(student_record["M03"])

## EXERCISE 2: add faculty data to ALL STUDENTS using LOOP
for key in student_record:
    student_record[key]["faculty"] = "FKE"
print(student_record.items())

## EXERCISE 3: add faculty data for all students using loop AND BY USING USER INPUT
for key in student_record:
    student_record[key]["faculty"] = input("Enter the faculty: ").title()
print(student_record.items())

## EXERCISE 4: based on the birthyear value. calculate each students' age. Then add the age data for each student
student_record = {
    "M01" : {
        "name" : "James",
        "cgpa" : 2.9,
        "birthyear" : 1998
        },
    "M02" : {
        "name" : "Leon",
        "cgpa" : 3.5,
        "birthyear" : 1989
        },
    "M03" : {
        "name" : "Igris",
        "cgpa" : 2.2,
        "birthyear" : 1997
        },
    "M04" : {
        "name" : "Baron",
        "cgpa" : 3.7,
        "birthyear" : 2001
        }
    }

from datetime import date
for key in student_record:
    birthyear = student_record[key]["birthyear"]
    year_now = int(date.today().strftime("%Y"))
    student_record[key]["age"] = year_now - birthyear
print(student_record.items())

## EXERCISE 5: complete exercise 4 using user defined function to calculate the age
student_record = {
    "M01" : {
        "name" : "James",
        "cgpa" : 2.9,
        "birthyear" : 1998
        },
    "M02" : {
        "name" : "Leon",
        "cgpa" : 3.5,
        "birthyear" : 1989
        },
    "M03" : {
        "name" : "Igris",
        "cgpa" : 2.2,
        "birthyear" : 1997
        },
    "M04" : {
        "name" : "Baron",
        "cgpa" : 3.7,
        "birthyear" : 2001
        }
    }

from datetime import date
def cal_age(birthyear):
    year_now = int(date.today().strftime("%Y"))
    age = year_now - birthyear
    return age

for key in student_record:
    student_record[key]["age"] = cal_age(student_record[key]["birthyear"])
print(student_record.items())

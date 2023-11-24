# skills = ["Writing", "Speaking", "Pitching"]

# skills.insert(2, "Writing")
# print(skills)
# skills.insert(4, "Writing")
# print(skills)

# print(skills.count("Writing")) # count how many instances of value "Writing"

# target = "Writing"
# num = skills.count(target)
# for i in range(skills.count(target)):
#     skills.remove(target)
# print(skills)

# for skill in skills:
#     if skill == target:
#         skills.remove(target)
# print(skills)

# num = skills.count(target)
# while num > 0:
#     skills.remove(target)
#     print(skills)
#     num -= 1
#     num = skills.count(target)

# skills_copy = skills.copy()
# print("Original: ", skills)
# print("Copy: ", skills_copy)
# skills.remove("C++")
# print("Original: ", skills)
# print("Copy: ", skills_copy)

# print(ord("A")) # char to unicode - 65
# print(ord("a")) # char to unicode - 97
# print(chr(65)) # unicode to char - A

# skills = ["Writing", 2, True, "Speaking", 1, "Pitching", False, True]
# skills = [2, True, 1, False, True, 3] # True == 1, False == 0
# # skills = ["Driving", "driving"]
# skills.sort()
# print(skills)
# skills.sort(reverse = True)
# print(skills)

## TUPLE
# skills = ("Swimming", "Racing", "Gaming")
# print(f"{skills} : {type(skills)}")

skills = ("Python", "C++", "Public Speaking", "C++", "C++")
# print(skills[2])
# print(skills[-2])
# print(len(skills))

# EXERCISE: use -ve index to display "Public Speaking", "C++"
# print(skills[-3:-1])

# CONSTRUCTOR
# skills_list = list(skills) # change tuple to list
# print(skills_list)
# skills_tuple = tuple(skills_list) # change list to tuple
# print(skills_tuple)

# for i, item in enumerate(skills):
#     print(i, item)

# EXCERSISE: use while loop to get the same output below
# num = len(skills)
# item = 0
# while num > 0:
#     print(item, skills[item])
#     item += 1
#     num -= 1

# num = len(skills)
# item = 0
# while item < num:
#     print(item, skills[item])
#     item += 1

# current_index = 0
# while current_index < len(skills):
#     print(current_index, skills[current_index])
#     current_index += 1

## SET

# skills = {"Python", "C++", "Public Speaking", "C++", "C++"}
# skills_ = {"Java", "SQL", "Matlab"}
# print(skills) # set does not allow duplicates
# print(len(skills))

# for skill in skills:
#     print(skill)

# skills.add("C#") # work similar as list append (add randomly into the set)
# print(skills)
# skills.update(skills_) # work as list extend
# print(skills)
# skills.remove("Java")
# print(skills)
# skills.pop()
# print(skills)
# skills.discard("SQL") # will not create an error if the item does not exist within the set

# EXERCISE: Loop through the set using while loop

# skills = {"Python", "C++", "Public Speaking", "C++", "C++"}
# num = len(skills)
# while num > 0:
#     print(skills.pop()) # however, the set will be cleared at the end of iteration
#     num = len(skills)

## DICTIONARY
# student_record = {
#     "name" : "Hafizi",
#     "cgpa" : 1.9,
#     "faculty" : "Art",
#     "attendance" : False
# }

# print(student_record)
# print(student_record["name"])
# print(student_record.values())
# print(student_record.keys())
# print(student_record.items())

# # replace value
# print("Before replacing: ", student_record.items)
# student_record["cgpa"] = 2.50
# print("After replacing: ", student_record.items())

# # add item : new key and value
# print("Before adding: ", student_record.items())
# student_record["gpa"] = 3.60
# print("After adding: ", student_record.items())

# # remove item
# print("Before removing: ", student_record.items())
# student_record.pop("gpa")
# print("After removing: ", student_record.items())

# # remove last item
# print("Before removing: ", student_record.items())
# student_record.popitem()
# print("After removing: ", student_record.items())

# # clear item
# print("Before clearing: ", student_record.items())
# student_record.clear()
# print("After clearing: ", student_record.items())

# for x in student_record:
#     # print(x) # print keys
#     print(student_record[x]) # print values

# for key in student_record.keys():
#     print(key) # print key
    
# for value in student_record.values():
#     print(value) # print value

# for pair in student_record.items():
#     print(pair) # print pair

# student_record = {
#     "M01" : {
#         "name" : "James",
#         "cgpa" : 2.9,
#         "faculty" : "Mechanical",
#         "attendance" : False
#         },
#     "M02" : {
#         "name" : "Leon",
#         "cgpa" : 3.5,
#         "faculty" : "Civil",
#         "attendance" : True
#         },
#     "M03" : {
#         "name" : "Igris",
#         "cgpa" : 2.2,
#         "faculty" : "Mechatronics",
#         "attendance" : True
#         },
#     "M04" : {
#         "name" : "Baron",
#         "cgpa" : 3.7,
#         "faculty" : "Electronics",
#         "attendance" : False
#         }
#     }

# print(student_record.items())
# print(student_record["M03"])
# print(student_record["M03"]["name"])

# import random
# birthyear = random.randrange(1980, 2000)
# for key in student_record.keys():
#     student_record[key]["birthyear"] = birthyear

# student_record["M01"]["birthyear"] = 1998
# student_record["M02"]["birthyear"] = 1989
# student_record["M03"]["birthyear"] = 2000
# student_record["M04"]["birthyear"] = 1995
# print(student_record.items())

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

faculties = ["mech", "civil", "bio", "chem"]
for key, faculty in zip(student_record, faculties):
    student_record[key]["faculty"] = faculty
print(student_record.items())

faculties = ["mech", "civil", "bio", "chem"]
for i, key in enumerate(student_record):
    student_record[key]["faculty"] = faculties[i]
print(student_record.items())

## EXERCISE 3: add faculty data for all students using loop AND BY USING USER INPUT
for key in student_record:
    faculty = input("Enter the faculty: ").title()
    student_record[key]["faculty"] = faculty
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
    birthyear = student_record[key]["birthyear"]
    age = cal_age(birthyear)
    student_record[key]["age"] = age
print(student_record.items())


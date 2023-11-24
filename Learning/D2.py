################################### DAY 2 ################################################

## WHILE LOOP
# my_num = int(input("Enter your number: "))

# while my_num <= 10:
#     print(my_num)
#     my_num += 1

## WHILE BREAK
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1
# else:
#     print("RESET")

## WHILE CONTINUE
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         # break
#         continue
#     print(i)
# else:
#     print("END")

## FOR LOOP
# skills = ["Programming", "3D Design", "Writing", "Graphic Design", "Driving"]

# for skill in skills:
#     if skill == "3D Design":
#         continue
#     elif skill == "Graphic Design":
#         break
#     print("I am good at", skill)
# else:
#     print("The loop is completed")

# print("--------------------")

# for skill in skills:
#     if skill == "3D Design":
#         continue
#     print("I am good at", skill)
# else:
#     print("The loop is completed")

## FOR RANGE
# for num in range(6):
#     print(num)

## NESTED FOR LOOP
# verbs = ["learning", "applying", "teaching"]
# skills = ["Programming", "3D Design", "Writing"]

# for verb in verbs:
#     for skill in skills:
#         print("I am good at", verb, skill)

# print("--------------------")


# for skill in skills:
#     for verb in verbs:
#         print("I am good at", verb, skill)

## STRING
# name = "Hafizi"
# edu = "Mechatronics Engineering"
# training = "Python"

# intro = "My name is " + name + ",\nI have Degree in " + edu + ",\nI am learning " + training
# print(intro)

# print("--------------------")

# ## FORMATTED STRING
# intro = f"""My name is {name},
# I have Degree in {edu},
# I am learning {training}"""
# print(intro)

## STRING LOOPING
# strings = "Hello"
# for string in strings:
#     print(string)

## STRING LENGTH
# strings = "Come and Go"
# print(len(strings))

## STRING ARRAYS
# strings = "Leading the way"
# print(strings[1])
# print(strings[1:4])
# print(strings[:7])
# print(strings[3:])
# print(strings[:])
# print(strings[-1])

## FIND IN STRING
# strings = "Ask me if you need anything"
# print(strings.find("i"))

## REPLACE STRING
# strings = "Python is hard to learn"
# print(strings.replace("hard", "easy"))

## CHECK IN STRINGS
# strings = "Welcome back to Infinite Esports"
# print("Infinite" in strings) # output will be Boolean

## ARRAYS
## LIST
# skills = ["Clear", True, 1, 1.00] # list can hold various data types
# skills = ["Driving", "Swimming", "Writing"]
# print(len(skills)) # print number of elements in list
# print(skills[1:])
# print(skills[-1])
# skills[2] = "Running" # replace list elements using index
# print(skills)

## EXERCISE: REPLACE MULTIPLE ITEMS USING INDEX
# skills = ["Driving", "Swimming", "Writing"]
# skills[1:] = ["Running", "Jumping"]
# print(skills)
# skills[:2] = ["Archery", "Horse Riding"]
# print(skills)

# LIST FUNCTIONS
# skills = ["Driving", "Swimming", "Writing"]

# skills.insert(1, "Accounting")
# print(skills)

# skills.append("Welding") # add new element into list (new index)
# print(skills)

# skills_2 = ["Gaming", "Pitching", "Soldering"]
# print(skills_2)

# skills.extend(skills_2) # combine two lists
# print(skills)

# skills.remove("Writing") # ONLY remove the first occurence
# print(skills)

# skills.pop() # remove element at the last index
# print(skills)

# skills.pop(3) # remove element using index
# print(skills)

# skills.clear(skills) # clear all elements in the list
# print(skills)

# del skills # delete the whole list from existance
# print(skills)

# for index in range(len(skills)):
#     print(skills[index])

## FINAL TASK (DAY 2)
## TASK 1
'''
1. create a list of names containing 3 items
2. create user input to get new name
3. store the new name in a variable
4. put the new name in the list

Contoh:
SEBELUM USER INPUT
[abu, ali, samad]
SELEPAS USER INPUT
[abu, ali, samad, ibrahim]
'''
# print("------------TASK 1------------")
# names = ["Aiman", "Fahmi", "Kamal"]

# name = input("Enter new name: ")

# names.append(name)
# print(names)

# print("------------TASK 2------------")
# ## TASK 2
# '''
# use loop to insert 3 new names
# '''

# names = ["Aiman", "Fahmi", "Kamal"]
# for i in range(3):
#     name = input(f"Enter new name {i+1}: ")
#     names.append(name)
# print(names)

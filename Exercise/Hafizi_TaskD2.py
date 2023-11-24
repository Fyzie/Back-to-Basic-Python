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
print("------------TASK 1------------")
names = ["Aiman", "Fahmi", "Kamal"]

name = input("Enter new name: ")

names.append(name)
print(names)

print("------------TASK 2------------")
## TASK 2
'''
use loop to insert 3 new names
'''

names = ["Aiman", "Fahmi", "Kamal"]
for i in range(3):
    name = input(f"Enter new name {i+1}: ")
    names.append(name)
print(names)
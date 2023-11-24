# NO GOOGLE OR CHATGPT ALLOWED IN FINDING THE EXACT ANSWER (jujur eh guys) 
# Algorithmic Mindset Exercise
 
# Q1: Write a Python code that will calculate the total of a list of numbers. 
# Example: [1,2,3] will get 6. 

lists = [1, 2, 3]
total = 0
for list in lists:
    total += list
print(f"Total of number values in the list: {total}")

# print(sum(lists))

# Q2: Write a Python code that will display the largest value within a list of numbers. 
# Example: [1,2,3] will get 3. 

lists = [1,2,3]
print(f"Max value in the list: {max(lists)}")

# Q3: Write a Python code that rearrange a list of numbers from largest to smallest. 
# Example: [1,2,3] will get [3,2,1] 

lists = [1,2,3]
lists.sort(reverse = True)
print(f"New arrangement: {lists}")

# Q4: Write a Python code that calculates the existence of each value. 
# Example: [1,2,3,3,2,1,2,1] will get 
# - 3 for value “1” 
# - 3 for value “2” 
# - 2 for value “3” 

lists = [1,2,3,3,2,1,2,1]
myset = set(lists) # unique value - remove duplicate in lists
for num in myset:
    calculate = lists.count(num)
    print(f"{calculate} for value \"{num}\"")

# Q5: Write a Python code that calculates the existence of each data type within a list. 
# Example: [1,2,3,”a”,”b”,”c”,True,False] will get 
# - 3 for int 
# - 3 for string 
# - 2 for boolean 

lists = [1,2,3,"a","b","c",True,False]
num_int, num_str, num_bool = 0, 0, 0
for list in lists:
    if type(list) == int:
        num_int += 1
    elif type(list) == str:
        num_str += 1
    elif type(list) == bool:
        num_bool += 1

print(f"{num_int} for int")
print(f"{num_str} for string")
print(f"{num_bool} for boolean")

# Q6: Write a Python code that calculates how many items is longer than 10 characters in a list of texts. 
# Example: ['Machine Learning Engineer', 'Data Scientist', 'AI Research Scientist', 'Computer Vision Engineer', 'Natural Language Processing Engineer', 'AI Product Manager', 'Robotics Engineer', 'Data Engineer'] will get 8 

lists = ['Machine Learning Engineer', 'Data Scientist', 'AI Research Scientist', 'Computer Vision Engineer', 'Natural Language Processing Engineer', 'AI Product Manager', 'Robotics Engineer', 'Data Engineer']
exceed = 0
for list in lists:
    if len(list) > 10:
        exceed += 1
print(f"Items that have more than 10 characters: {exceed}")

# Q7: Write a Python code that creates a list of only odd numbers using the range function.
# Stop when the list reaches 100 items. 

odd_num = []
for i in range(1, 100, 2):
    odd_num.append(i)
print(f"The odd numbers: {odd_num}")

# Q8: Write a Python code that creates a list of exponential values from a list of numbers. 

import math
lists = [2,4,5,6,8,3]
print(lists)
new_lists = []
for list in lists:
    list = math.exp(list)
    new_lists.append(list)
print(f"Exponential values: {new_lists}")

# Q9: Write a Python code that replaces the value “python” with “Python”
# from the following list without directly referring to the index.
# Iterate through the list to find the required value. 
# ['JavaScript', 'Java', 'C++', 'python', 'C#', 'Ruby', 'Swift', 'Go', 'PHP']

lists = ['JavaScript', 'Java', 'C++', 'python', 'C#', 'Ruby', 'Swift', 'Go', 'PHP']
new_lists = []
for list in lists:
    if list == "python":
        list = "Python"
    new_lists.append(list)
print(f"Replaced Python in the list: {new_lists}")

# Q10: Write a Python code that returns similar values that exist in two different lists. 

list_1 = [1, 3, 5, 7]
list_2 = [2, 6, 3, 1]
similar_value = []
for x in list_1:
    for y in list_2:
        if x == y:
            similar_value.append(x)
            # print(x)
print(f"Similar values: {similar_value}")

# Q11: Define Python function that generates unique student ID. 
# Example: B123456 (the B represents Bachelor) 

def generate_id(num_stud, base_id):
    list_id = []
    for x in range(num_stud):
        base_id += 1
        new_id = f"B{base_id}"
        list_id.append(new_id)
    print(list_id)

num_stud = 10 # number of new id needed
base_id = 192034 # recent id number
generate_id(num_stud, base_id)

# Q12: Use user input to determine they are Diploma, Bachelor or Master's students.
# Define Python function that generates unique student ID.  
# Example: M123456 D-Diploma, B-Bachelor, M-Masters. 

def generate_id(num_stud, programme, base_id):
    list_id = []
    for x in range(num_stud):
        base_id += 1
        if programme == "D" or programme == "DIPLOMA":
            new_id = f"D{base_id}"
        elif programme == "B" or programme == "BACHELOR":
            new_id = f"B{base_id}"
        elif programme == "M" or programme == "MASTERS":
            new_id = f"M{base_id}"
        list_id.append(new_id)
    print(list_id)

faculty = input("Enter your programme (D/ B/ M): ").upper()
num_stud = 10
recent_id = 123942
generate_id(num_stud, faculty, recent_id)

# Q13: Define Python function that generates unique student ID based on their faculty.
# Use user input to determine the faculty. 
# Example: B123456FKE (the FKE represents their faculty) 

def generate_id(num_stud, faculty, base_id):
    list_id = []
    for x in range(num_stud):
        base_id += 1
        if faculty == "MCT" or faculty == "MECHTRONICS":
            new_id = f"B{base_id}MCT"
        elif faculty == "MECH" or faculty == "MECHANICAL":
            new_id = f"B{base_id}MECH"
        elif faculty == "AERO" or faculty == "AEROSPACE":
            new_id = f"B{base_id}BIO"
        list_id.append(new_id)
    print(list_id)

faculty = input("Enter your faculty (MCT/ MECH/ AERO): ").upper()
num_stud = 10
recent_id = 123942
generate_id(num_stud, faculty, recent_id)

# Q14: Define a Python function that accepts user input of their birthdate and returns the day of their birth. 
# Example: 30th November 1956 returns Friday 

import datetime as dt
def identify_day(birthdate):
    birthdate = dt.datetime.strptime(birthdate, "%d-%m-%Y")
    birthday = birthdate.strftime("%A")
    print(birthday)

birthdate = input("Enter your birthdate (DD-MM-YYYY): ")
identify_day(birthdate)

# Q15:Define a Python function that calculates how many days there are between two dates from user input. 

def cal_days(date_1, date_2):
    date_1 = dt.datetime.strptime(date_1, "%d-%m-%Y")
    date_2 = dt.datetime.strptime(date_2, "%d-%m-%Y")
    days_diff = (date_1 - date_2).days
    abs_days = abs(days_diff)
    print(f"Days Difference: {abs_days} day(s)")
    
date_1 = input("Enter first date (YYYY-MM-DD): ")
date_2 = input("Enter second date (YYYY-MM-DD): ")
cal_days(date_1, date_2)

# Extra:  
# If you’ve completed all questions above,
# explore list comprehension and redo some of your codes above using list comprehension.  
# Tips: List comprehension provides a more concise syntax
# for generating a new list using the values from an existing list. 

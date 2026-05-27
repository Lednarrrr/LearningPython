# Day 07 Sets
# Exercise 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Android', 'Lenovo'])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.pop()
print(it_companies)

# What is the difference between remove and discard
print('Remove outputs an error if it cannot find it, while discard does not output an error even if they cannot find the item to be discarded')

# Exercise 2
# Join A and B
A.update(B)
print(A)

# Find A intersection B
print(A.intersection(B))

# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets
print(A.isdisjoint(B))

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# Delete the sets completely
del A
del B

# Exercise 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
set_age=set(age)
print('list length:',len(age))
print('set length:', len(set_age))

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
splitted_sentence_set = set(sentence.split())
print(splitted_sentence_set)

# Day 08 Dictionaries
# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {'name': 'doug', 'color': 'white', 'breed': 'wolf', 'age': '2'}

# Create a student dictionary and add first_name, last_name, gender,
# age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name': 'John', 'last_name': 'Doe', 'gender': 'male', 'age': '22', 
           'marital_status': 'single', 'skills': ['programming'], 'country': 'Philippines',
           'city': 'Manila City', 'address': 'No'}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(type(student['skills']))

# Modify the skills values by adding one or two skills
student['skills'].extend(['drawing', 'speaking'])
print(student['skills'])

# Get the dictionary keys as a list
studentKeys_list = student.keys()
print(studentKeys_list)

# Get the dictionary values as a list
studentValues_list = student.values()
print(studentValues_list)

# Change the dictionary to a list of tuples using items() method
student_tuples = student.items()
print(student_tuples)

# Delete one of the items in the dictionary
student.pop('gender')
print(student)

# Delete one of the dictionaries
del student
print(student)
'''
'''
# Day 09 Conditionals
# Exercise 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, 
# give feedback: You are old enough to drive. If below 18 give feedback to 
# wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive')
else:
    print(f'You need {18-age} more years to learn to drive')

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
# Use input(“Enter your age: ”) to get the age as input. You can use a nested condition 
# to print 'year' for 1 year difference in age, 'years' for bigger differences, and a 
# custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.
my_age = int(input('Enter my age: '))
your_age = int(input('Enter your age: '))
if my_age > your_age:
    print(f'I am older than you by {my_age-your_age} {'year' if my_age-your_age == 1 else 'years'}.')
elif my_age == your_age:
    print('We are the same age')
else:
    print(f'You are {your_age-my_age} {'year' if your_age-my_age == 1 else 'years'} older than me.')

# Get two numbers from the user using input prompt. If a is greater than b return a is 
# greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
one = int(input('Enter number one: '))
two = int(input('Enter number two: '))
if one > two:
    print(f'{one} is greater than {two}')
elif one < two:
    print(f'{one} is less than {two}')
else:
    print(f'{one} is equal to {two}')

# Exercise 2
# Write a code which gives grade to students according to theirs scores:
# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# ```
grade = int(input('Enter your grade: '))
if grade >= 90 and grade <= 100:
    print('You are A')
elif grade >= 80 and grade <= 100:
    print('You are B')
elif grade >= 70 and grade <= 100:
    print('You are C')
elif grade >= 60 and grade <= 100:
    print('You are D')
elif grade <= 59 and grade <= 100:
    print('You are F')
else:
    print('Invalid')

# Get the month from user input then check if the season is Autumn, Winter, 
# Spring or Summer. If the user input is: September, October or November, the 
# season is Autumn. December, January or February, the season is Winter. March, 
# April or May, the season is Spring June, July or August, the season is Summer
season = input('Enter month: ').lower()
if season == 'september' or season == 'october' or season == 'november':
    print('The season is Autumn')
elif season == 'december' or season == 'january' or season == 'february':
    print('The season is Winter')
elif season == 'march' or season == 'april' or season == 'may':
    print('The season is Spring')
elif season == 'june' or season == 'july' or season == 'august':
    print('The season is Summer')
else:
    print('Invalid')

# The following list contains some fruits:
# ```sh
# fruits = ['banana', 'orange', 'mango', 'lemon']
# ```
# 
# If a fruit doesn't exist in the list add the fruit to the list and 
# print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
input = input('Enter fruit: ')
if input in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(input)
    print(fruits)

# Exercise 3
# Here we have a person dictionary. Feel free to modify it!
#         person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#  * Check if the person dictionary has skills key, if so print out the middle skill 
# in the skills list.
if 'skills' in person:
    print(f'{person['skills'][len(person['skills'])//2]}')
else:
    print('no skills')

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' 
# skill and print out the result.
if 'Python' in person['skills']:
    print('Python')
else:
    print('No python')

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!
if 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('He is a front end developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a backend developer')
elif 'Node' in person['skills'] and 'React' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a fullstack developer')
else:
    print('unknown title')

#  * If the person is married and if he lives in Finland, print the information in the 
# following format:
# Asabeneh Yetayeh lives in Finland. He is married.
if True is person['is_married'] and 'Finland' is person['country']:
    print(f'{person['first_name']} {person['last_name']} lives in {person['country']}. He is married')
else:
    print('loser')
'''
python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = f'The following are python libraries: {python_libraries}'
print(formated_string)

language = 'Python'

a,b,c,d,e,f = language # unpacking sequence characters into variables
print(language[0]) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

slice=language[0::2]
print(slice)
word='python'.endswith('ion')
print(word)

nya=['nyo', 'nyi', 'nyu', 'nye', 'nyo']
print(' '.join(nya))

nya=['nyo', 'nyi', 'nyu', 'nye', 'nyo']
ya='nyo nyi nyu nye nyo'.split(' ')
first=ya[0]
second=ya[1]
third=ya[2]
fourth=ya[3]
fifth=ya[4]


print('python code code code'.startswith('python code'))

# Exercise
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
word=['Thirty', 'Days', 'Of', 'Python']
print(' '.join(word))

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'. & Declare a variable named company and assign it to an initial value "Coding For All". & Print the variable company using print(). & Print the length of the company string using len() method and print(). & Change all the characters to uppercase letters using upper() method. & hange all the characters to lowercase letters using lower() method. & Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All. & Cut(slice) out the first word of Coding For All string. & Check if Coding For All string contains a word Coding using the method index, find or other methods. & Replace the word coding in the string 'Coding For All' to Python. & Change "Python for All" to "Python for Everyone" using the replace method or other methods. & Split the string 'Coding For All' using space as the separator (split()) . & "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma. & What is the character at index 0 in the string Coding For All. & What is the last index of the string Coding For All. & What character is at index 10 in "Coding For All" string. & Create an acronym or an abbreviation for the name 'Python For Everyone'. & Create an acronym or an abbreviation for the name 'Coding For All'. & Use index to determine the position of the first occurrence of C in Coding For All. & Use index to determine the position of the first occurrence of F in Coding For All. & Use rfind to determine the position of the last occurrence of l in Coding For All People. & Does 'Coding For All' start with a substring Coding? & Does 'Coding For All' end with a substring coding? & '   Coding For All      '  , remove the left and right trailing spaces in the given string. & Which one of the following variables return True when we use the method isidentifier():
word2=['Coding', 'For' , 'All']
company=' '.join(word2).capitalize().title()
swapcasecompany=company.swapcase()
sliced=' '.join(word2[1:])
replace=company.replace('Coding', 'Python')
replace2=replace.replace('For All', 'For Everyone')
splitcompany=company.split(' ')
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(swapcasecompany)
print(sliced)
print(company.index('Coding'))
print(replace)
print(replace2)
print(splitcompany)
browsers='Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(', ')
print(browsers)
print('the character on the index 0 in the company variable is:', company[0])
print('the last index of the company variable is:', company[-1])
print('the character on index 10 in the company variable is:', company[10])
word3='Python For Everyone'.split(' ')
print(word3[0][0], word3[1][0], word3[2][0])
print(word2[0][0], word2[1][0], word2[2][0])
print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))
print('Is it true that', company, 'starts with the substring Coding?', company.startswith('Coding'))
print('Is it true that', company, 'ends with the substring coding?', company.endswith('coding'))
print('   Coding For All      '.strip(' '))
print('thirty_days_of_python'.isidentifier())

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction' & Use rindex or rfind to find the position of the last occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction' & Slice out the phrase 'because because because' from the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence='You cannot end a sentence with because because because is a conjunction'
sentencedslice=sentence[sentence.index('because'):sentence.rindex('because')+len('because')]
print(sentencedslice)
'''
pythonLibraries=' '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'])
print(pythonLibraries)
print()
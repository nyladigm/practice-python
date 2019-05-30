

'''
Exercise 1 from Practice Python.
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''


import datetime
'''
ask for the users' name and age:
'''
your_name = input('What is your name: ')
user_age = int(input('What is your age: '))

'''
determine the year a user will turn 100 years of age:
'''
now = datetime.datetime.now()
new_age = str((now.year - user_age) + 100)

'''
print the final message of the year a user will turn 100
'''
print(your_name + ' will be 100 years old in the year ' + new_age)
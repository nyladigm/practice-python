'''
Exercise 3: List Less Than Ten from Practice Python.
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for numbers in a:
    if numbers < 5:
        print(numbers)
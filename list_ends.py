'''
Exercise 11 - List Ends from Practice Python
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list. For
practice, write this code inside a function.
'''

# the original list of numbers
og_list = [5, 10, 15, 20, 25]

# create a function that takes in a list and returns the first and last elements
def list_ends(og_list):
    return [og_list[0], og_list[len(og_list)-1]]

# print the outcome just to check
print(list_ends(og_list))

'''
Exercise 6 - String Lists from Practice Python
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''

#ask the user for a string
new_string = input('Please enter a string: ')

#reverse the users string input
reverse_string = new_string[::-1]

# check to see if the original string matches the reverse string:
if new_string == reverse_string:
    print('this is definitely a palindrome')
else:
    print('nope, not a palindrome')

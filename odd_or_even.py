'''
Exercise 2 - Practice Python: Odd or Even
Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?
'''

'''
Ask the user for a number.
'''
number = int(input('Please enter a number: '))


'''
Tell user if the number is odd or even.
'''
if (number % 2 == 0):
    print('Your number is even.')
else:
    print('Your number is odd.')
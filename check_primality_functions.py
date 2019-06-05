'''
Exercise 11 - Check Primality Functions from Practice Python
Ask the user for a number and determine whether the number is prime or not. (For those
who have forgotten, a prime number is a number that has no divisors.). You can (and should!)
use your answer to Exercise 4 to help you. Take this opportunity to practice using
functions, described below.
'''

# use a function to prompt the user to input a number
def get_integer():
    return int(input('Please enter a number: '))

# Check to see which numbers divide equally into the user number.
check_prime = get_integer()
if check_prime % 2 != 0:
    print('this number is prime')
else:
    print('nope, this is not a prime number')

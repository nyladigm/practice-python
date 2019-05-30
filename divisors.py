'''
Exercise 4 - Divisors
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

number = int(input('Please enter a number: '))

'''
Create a range of numbers from two to the number the user entered.
'''
x = range(2, number)

'''
Check to see which numbers divide equally into the user number.
'''
for num in x:
    if number % num == 0:
        print(num)
'''
Exercise 12 - Fibonacci from Practice Python.
Write a program that asks the user how many Fibonnaci numbers to generate and
then generates them. Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the
sequence is the sum of the previous two numbers in the sequence. The sequence
looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

# ask the user for a number that generates the corresponding numbers in the Fibonacci sequence
user_number = int(input('hey user, tell me how many numbers to generate: '))

# write a function that takes an input (n) and generates Fibonacci numbers
def fib(x):
    user_number, b = 0, 1
    for items in range(x):
        yield user_number
        user_number, b = b, user_number + b

print(list(fib(user_number)))

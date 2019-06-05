'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the
number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember
to use the user input lessons from the very first exercise)
'''

# generate a random number between and including 1 through 9
import random
the_number = (random.randint(1,9))
print(the_number)

# have the user input a number inclusive of 1 through 9
the_guess = int(input('hey user...guess the number I generated...(it is a number between 1 and 9:'))
print(the_guess)

# here's the logic for if the guess is close to the number (or IS the generated number
if the_guess > the_number:
    print('you guessed too high!')
elif the_guess < the_number:
    print('you guessed too low!')
else:
    print('you guessed the correct number!')

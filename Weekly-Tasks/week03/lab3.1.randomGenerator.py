# Weekly Task 3
# Program that prints a random number between 1 and 10
# Author: Martynas Ramonas

# random is a module that contains functions for generating random numbers.
# import it before we can use it.
import random

number = random.randint(1, 10)
print('Here is a random number: {}'.format(number))
# Weekly Task 3
# Program that prints a random number between 1 and 10
# Author: Martynas Ramonas

# random is a module that contains functions for generating random numbers.
# import it before we can use it.
import random

number = random.randint(1, 10)
print('Here is a random number: {}'.format(number))

# Modify the program so the user inputs the range of the random number.
# Get the range from the user
lowest_number = int(input('Enter the lowest number: '))
highest_number = int(input('Enter the highest number: '))

# randint() takes two arguments: the lowest number and the highest number. It returns a random integer between those two numbers (inclusive).
random_number = random.randint(lowest_number, highest_number)

# Prefer this formatting style over the one above. It is more readable and easier to write.
print(f'Here is a random number from {lowest_number} to {highest_number}: {random_number}') 
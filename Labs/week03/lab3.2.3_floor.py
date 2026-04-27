# Weekly Task 3
# Program that takes in a float and outputs and int rounded down, will need the math module math.floor()
# Author: Martynas Ramonas

# import the math module to use the floor function, module is a collection of functions and variables that can be used in your program, 
# need to import it before you can use it
import math

# Get the number from the user
number_to_floor = float(input('Enter a float number: '))

# Use the math.floor() function to round the number down to the nearest integer, 
# math.floor() function takes a single argument and returns the largest integer less than or equal to the argument. 
# For example, math.floor(3.7) will return 3, and math.floor(-3.7) will return -4.
floored_number = math.floor(number_to_floor)

# Print the floored number
print(f'{number_to_floor} floored is {floored_number}')
# Weekly Task 3
# Program that takes in a float and the output is rounded to the nearest even number.
# This is called "bankers rounding" and it is used in financial calculations to avoid bias in rounding. 
# 4.5 rounds to 4, 5.5 rounds to 6, so do not use it accuracy is essential
# Author: Martynas Ramonas

# Get the number from the user
number_to_round = float(input('Enter a float number: '))

# Use the round() function to round a number to the nearest whole number.
rounded_number = round(number_to_round)

# Print the rounded number
print(f'{number_to_round} rounded to the nearest whole number is {rounded_number}')


# Weekly Task 4
# Program that asks the user to input any positive integer and output the successive valus of the followong calculation.
# At each step calculate the next value by taking the current value and , if it's even, divide by 2, but if it's odd, multiply by 3 and add 1.
# The program ends if the current value is 1.
# Author: Martynas Ramonas

# Get the user to enter a number.
number = int(input('Enter a positive integer: '))

# Check if the number is positive.
# If the number is 0 or negative, ask the user to enter a positive integer until they do.
while number <= 0:
    print('Please enter a positive integer.')
    number = int(input('Enter a positive integer: '))

# Print the initial number.
print(f'Current value: {number}')

# Loop until the current value is 1.
while number != 1:
    # If the number is even divide it by 2.
    if number % 2 == 0:
        number = number // 2

    # If the number is odd, multiply it by 3 and add 1.
    else:
        number = number * 3 + 1

    # Print out the number after each calculation.
    print(f'Current value: {number}')
# Weekly Task 3
# Program that reads 2 numbers and divides the first one by the second one
# Author: Martynas Ramonas

# Get the numbers from the user
first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the number you want to divide by: '))

# Divide the first number by the second number
# We use // to get the integer result of the division.
answer = first_number // second_number

# We use % to get the remainder of the division.
remainder = first_number % second_number

# Print the answer
print('{} divided by {} is {} with a remainder of {}'.format(first_number, second_number, answer, remainder))

#Test
#print(f'{first_number} divided by {second_number} is {answer} with a remainder of {remainder}')

#Weekly Task 3
# Program that reads 2 numbers and subtract the first one from the second one
#Author: Martynas Ramonas

# Input reads in a string so we need to convert it into an integer using the int() function
# So we can perform mathemathical operations.
# Get the numbers from the user
first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))

# Subtract the first number from the second number
answer = first_number - second_number

# Print the answer
print('{} minus {} is {}'.format(first_number, second_number, answer))

#Test
#print(f'{first_number} minus {second_number} is {answer}')
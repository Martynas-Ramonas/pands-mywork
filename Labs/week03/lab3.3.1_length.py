# Weekly Task 3
# Program that reads a string and outputs how long it is
# Author: Martynas Ramonas

# Get the string from the user
input_string = input('Enter a string: ')

# Use the len() function to get the length of the string, the len() function returns the number of characters in a string, 
# including spaces and punctuation.
length_of_string = len(input_string)

# Print the length of the string
print(f'The length of the string is: {length_of_string}')

#Simple program creating and outputing a string

# The \t is a tab character, which adds a horizontal space in the string. 
# The \n is a newline character, which moves the cursor to the next line when printing the string.
message = 'John said\t"Hi"\nI said\t\t "Bye'
print(message)
# Weekly Task 3
# Program that reads a string and strips any leading or trailing spaces
# Program also converts the string to lower case
# Program outputs the length of the input and output strings
# Author: Martynas Ramonas

# Get the string from the user
raw_input = input('Enter a string with leading and trailing spaces: ')

# Use the strip() method to remove leading and trailing spaces from the string
# The strip() method returns a new string with the leading and trailing spaces removed
# Use the lower() method to convert the string to lower case. The lower() method returns
normalised_string = raw_input.strip().lower()

# Get the length of the input and output strings using the len() function, 
# which returns the number of characters in a string, including spaces and punctuation
length_of_raw_input = len(raw_input)
length_of_normalised_string = len(normalised_string)

# Print the length of the input and output strings
print(f'The string normalised is: {normalised_string}')
print(f'We reduced the input from {length_of_raw_input} to {length_of_normalised_string} characters')
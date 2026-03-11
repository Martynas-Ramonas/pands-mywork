# Weekly Task 3
# Program that reads 10 character account number and outputs the account number with only the last 4 digits showing
# and the first 6 digits replaced with Xs
# Author: Martynas Ramonas

# Get the account number from the user
account_number = input('Enter a 10 digit account number: ')

# Use string slicing to get the last 4 digits of the account number good tutorial on W3Schools https://www.w3schools.com/python/python_strings_slicing.asp
last_four = account_number[6:]

# Create the masked account number by concatenating Xs with the last 4 digits
masked_account_number = 'XXXXXX' + last_four

# Print the masked account number
print(f'The last 4 digits of your account are: {masked_account_number}')

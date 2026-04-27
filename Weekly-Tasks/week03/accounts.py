# Weekly Task 3
# Program that reads 10 character account number and outputs the account number with only the last 4 digits showing
# and the first 6 digits replaced with Xs
# Author: Martynas Ramonas

# Get the account number from the user
account_number = input('Enter any number of digits for the account number: ')

# Use string slicing to get the last 4 digits of the account number good tutorial on W3Schools https://www.w3schools.com/python/python_strings_slicing.asp
# "X" * (len(account_number) - 4) creates enough X characters to hide all but the last 4 digits
# account_number[-4:] slices the string to get the last 4 characters of the account number
# The two parts are joined together using + to form the masked account number
masked_account_number = 'X' * (len(account_number) - 4) + account_number[-4:]

# Print the masked account number
print(f'The last 4 digits of your account are: {masked_account_number}')

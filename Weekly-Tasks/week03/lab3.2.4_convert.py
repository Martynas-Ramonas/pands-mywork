# Weekly task 3 Extra
# Program to take in a float in the form of dollars and output the amount in cents
# Author: Martynas Ramonas

# Get the amount of money from the user
money = float(input('Enter the amount of money in dollars: '))

# Convert the amount to cents
# To convert dollars to cents, multiply the amount in dollars by 100, since there are 100 cents in a dollar.
cents = int(money * 100)

# Print the amount in cents
print(f'The amount in cents is {cents}')
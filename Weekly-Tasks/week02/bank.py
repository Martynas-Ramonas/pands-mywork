# Weekly Tasks 2
# Promt the user and read in two money amounts (in cents)
# Add the two amounts, and store the total as an interger
# Print out the answer in a human readable forma with a euro sign and decimal point between the euro and cent of the amount
# Author: Martynas Ramonas

# Get the user's input for the two amounts in cents
amount1 = int(input('Please enter the first amount in cents: '))
amount2 = int(input('Please enter the second amount in cents: '))

# Add the two amounts and store the total as an integer
total = amount1 + amount2

# Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount.
# The total is divided by 100 to convert cents to euros, and formatted to 2 decimal places using :.2f
print(f'The total amount is €{total/100:.2f}')      
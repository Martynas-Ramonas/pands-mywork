# Weekly Task 3 Extra
# Fix the problem
# Author: Martynas Ramonas

#Why does this expression cause an error? How can you fix it? 
#message = 'I have eaten ' + 99 + ' burritos.'

# Turn hte number into a string using the str() function so it can be concatenated with the other strings.
# Could also use an f-string to format the message instead of concatenating strings together.
message = 'I have eaten ' + str(99) + ' burritos.'
message2 = f'I have eaten {99} burritos.'

print(message)
print(message2)

# Could also declate the number as a variable and use it in the message. But more work to do it this way. Unless you need to use the number in other places in the program.
buritos_eaten = 99

print(f'I have eaten {buritos_eaten} burritos.')
print('I have eaten {} burritos.'.format(buritos_eaten))



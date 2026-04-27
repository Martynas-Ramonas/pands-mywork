# Weekly Tasks 2
# Greeting the user with their name
# Author: Martynas Ramonas

name = input("Enter your name:")

# Needs a space after "Hello" to separate it from the name otherwise it's joined together
# The '\n' is a newline character that moves the next part of the message to a new line like 'Return'/'Enter' key on the keyboard
print("Hello " + name + '\nNice to meet you')

# Using an f-string(formated string) for the same output as above
#print(f'Hello {name}\nNice to meet you')  #Commented out so theres no double output


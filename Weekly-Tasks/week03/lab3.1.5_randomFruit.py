# Weekly Task 3
# Program that prints out a random fruit
# Author: Martynas Ramonas

# import the random module to use its functions for generating random numbers.
import random

fruits = ['Apple', 'Banana', 'Orange', 'Grape', 'Kiwi', 'Mango', 'Pineapple']

# We want a random number between 0 and length-1
index = random.randint(0, len(fruits) - 1)

# ???
fruit = fruits[index]
print(f'Here is a random fruit: {fruit}')

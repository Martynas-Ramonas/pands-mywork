# Program that takes a positive floating-point number as input and outputs an approximation of its square root.
# I will be using Newton's method. From what I found online Babylonian method is simillar but it seems to be the older version.
# Newton's method starts with a guess and improves it each time the loop runs.
# For square roots, it takes the average of the guess and number / guess.
# Repeating this makes the guess get closer to the real square root.
# Author: Martynas Ramonas

# Square root function using Newton's method.
def square_root(number):
    # Start with initial guess for the square root.
    guess = number / 2

    # Repeat the calculation a ficed number of times.
    # Each loop improves hte guess by averaging it with the result of dividing the original number by the guess.
    for i in range(20):
        guess = (guess + number / guess) / 2

    # Return the final guess as the approximation of the square root.
    return guess

# Get the user to enter a positive floating-point number.
number = float(input('Enter a positive floating-point number: '))

# Check if the number is positive.
while number <= 0:
    print('Please enter a positive floating-point number.')
    number = float(input('Enter a positive floating-point number: '))   

# Call our own square_root function and print the result.
answer = square_root(number)

# Print the approximation of the square root, hte actual square root using the built-in function, and the actual square root rounded to 1 decimal place.
print(f'The square root of {number} is approximately {answer}, and the actual square root is {number ** 0.5}, rounded to 1 decimal place is {round(number ** 0.5, 1)}')



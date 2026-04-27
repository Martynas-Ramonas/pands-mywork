# Program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.
# Found online https://realpython.com/read-write-files-python/ and https://realpython.com/python-command-line-arguments/ 
# Error handling was on docs.python.org/it/3.8/tutorial/errors.html
# I asked ChatGPT to generate 500 character long text file for testing, it should have 105 lowercase e's in it.
# Author: Martynas Ramonas

# Import the sys module so we can read command line arguments.
import sys

# Define function called count_es.
# Takes a filename as an argument and returns the number of lowercase e's in that file.
def count_es(filename):
    """Count the number of lowercase e's in a text file."""

    # Open the file in read mode, shown by "r".
    with open(filename, "r") as file:
        # Read the entire contents of the file into a string called text.
        text = file.read()

    # Count how many times lowercase "e" appears in the text.
    return text.count("e")


# Check if the user gave a filename, it needs to be at least 2 arguments, 
# The first one is the script name and the second one is the filename. Eg, "python es.py example.txt"
if len(sys.argv) < 2:
    print("Error: Please provide a filename.")
    print("Example: python es.py example.txt")

     # Stop the program because it cant continue without a filename.
    sys.exit(1)

# Store the filename from the command line in a variable.
filename = sys.argv[1]


# Try to count the e's in the file.
# This code might cause an error if the file does not exist,
# Isnt readable, or isbt a normal text file.
try:
    number_of_es = count_es(filename)

    # Print the number of e's in the file.
    print(f"The file '{filename}' contains {number_of_es} lowercase 'e's.")

# This runs if the filename doesnt exist.
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")

# This runs if Python cannot read the file as text. Eg, if hte file is a pdf, image, or some other file.
except UnicodeDecodeError:
    print(f"Error: The file '{filename}' does not appear to be a text file.")

# This runs if the file exists but the user doesn't have permission to read it.
except PermissionError:
    print(f"Error: You do not have permission to read '{filename}'.")
# Program that outputs whether or not today is a weekday.
# Found on https://www.w3schools.com/python/python_datetime.asp
# Author: Martynas Ramonas

# Import the datetime module to work with dates and times
from datetime import datetime

# Get today's date and time
today = datetime.today()

# The weekday() function is a built-in method of the datetime.date class in Python. It returns the day of the week as an integer, 
# where Monday is 0 and Sunday is 6. This method is useful when you want to determine the day of the week for a given date.
# https://www.geeksforgeeks.org/python/weekday-function-of-datetime-date-class-in-python/  I'm ading these links and commnets for 
# myself because I'm probably going to forget how this works and I want to be able to find it easily in the future.
day_number = today.weekday()

# 0 = Monday to 4 = Friday are weekdays
# 5 = Saturday and 6 = Sunday are not weekdays
if day_number < 5:
    print("Yes, today is a weekday.")
else:
    print("No, today is not a weekday.")
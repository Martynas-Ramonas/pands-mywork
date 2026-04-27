# Program that displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10, 
# Author: Martynas Ramonas

# Sorry for the heavy comments, I'll forget waht this does in the future so I want to make sure I understand it when I look back at it.


# Import numpy.
# numpy is used here to create random numbers and x values.
import numpy as numpy

# Import matplotlib.
# pyplot is used to create and display the plot.
import matplotlib.pyplot as plot


# Create 1000 random numbers from a normal distribution.
# The average value is around 5.
# The standard deviation is 2, which controls how spread out the values are.
data = numpy.random.normal(5, 2, 1000)

# Create 100 evenly spaced x values between 0 and 10.
# The 100 is the number of points, not the maximum value.
# More points make the line plot look smoother.
x = numpy.linspace(0, 10, 100)

# Calculate h(x) = x^3 for each x value.
# The ** operator means "to the power of".
h = x ** 3

# Create the figure and set its size.
plot.figure(figsize=(10, 6))

# Create a histogram from the normal distribution data.
# bins=30 means the data is grouped into 30 bars.
# alpha=0.6 makes the bars slightly transparent.
# label is the text that will appear in the legend.
plot.hist(
    data,
    bins=30,
    alpha=0.6,
    label="Normal distribution: mean = 5, std dev = 2"
)

# Plot the function h(x) = x^3 as a line.
# linewidth=2 makes the line thicker and easier to see.
plot.plot(
    x,
    h,
    linewidth=2,
    label="h(x) = x³"
)

# Add title and labels.
plot.title("Normal Distribution Histogram and h(x) = x³")
plot.xlabel("x values")
plot.ylabel("Frequency / h(x) value")

# Add a legend and grid to make the plot clearer.
plot.legend()
plot.grid(True, alpha=0.3)

# Save the plot as a PNG file.
plot.savefig("plottask.png")

# Display the plot.
plot.show()
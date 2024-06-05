# Import the arcsin function and the constant pi from the math module
from math import asin, pi

# Number of divisions
n = 10

# Generate a list of x values from 0 to 1 with n divisions
x_list = [i * 1.0 / n for i in range(n + 1)]

# Print a line of hyphens to serve as the table heading separator
print('------------------')

# Print column headers for x and arcsin(x)
print('%-3s %13s ' % ('x', 'arcsin(x)'))

# Iterate over each x value in the list
for x in x_list:
    # Calculate the arcsin(x) in degrees and print the result
    print('%-3.2f %12.2f' % (x, asin(x) * 180 / pi))

# Print a line of hyphens to mark the end of the table
print('------------------')

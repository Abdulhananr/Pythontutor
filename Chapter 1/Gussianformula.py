from math import pi, exp, sqrt

# Define the parameters
mean = 0  # mean of the Gaussian distribution
std_dev = 2.0  # standard deviation of the Gaussian distribution
x_value = 1.0  # x value to evaluate the Gaussian function

# Calculate the Gaussian function
gaussian_function = 1 / (sqrt(2 * pi) * std_dev) * exp(-0.5 * ((x_value - mean) / std_dev) ** 2)
print(gaussian_function)  # print the result

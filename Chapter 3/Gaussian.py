from math import sqrt, exp, pi

def gaussian_distribution(x, mean=0, std_dev=1):
    """
    Calculate the value of the Gaussian distribution (normal distribution) at a given point.
    
    Parameters:
    x (float): The point at which to evaluate the distribution.
    mean (float): The mean (average) value of the distribution (default is 0).
    std_dev (float): The standard deviation of the distribution (default is 1).
    
    Returns:
    float: The value of the Gaussian distribution at the given point.
    """
    gaussian = 1 / (sqrt(2 * pi) * std_dev) * exp(-0.5 * ((x - mean) / std_dev) ** 2)
    return gaussian

# Print header row with x values
print(f'{"x":>8}', end='')
for x in range(-5, 6):
    print(f'{x:>9}', end='')
print("\nGaussian", end='')

# Print values of the Gaussian distribution for each x value
for x in range(-5, 6):
    print(f'{gaussian_distribution(x):.7f}', end='')

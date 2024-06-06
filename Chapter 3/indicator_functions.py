def indicator_function_1(x, a, b):
    """
    Compute the indicator function for the interval [a, b].

    Parameters:
    x (int): The value to check.
    a (int): The lower bound of the interval.
    b (int): The upper bound of the interval.

    Returns:
    int: 1 if x is within the interval [a, b], otherwise 0.
    """
    if a <= x <= b:
        return 1
    else:
        return 0


def heaviside_step_function(x):
    """
    Compute the Heaviside step function.

    Parameters:
    x (float): The input value.

    Returns:
    int: 0 if x is negative, 1 if x is non-negative.
    """
    if x < 0:
        return 0
    elif x >= 0:
        return 1


def indicator_function_2(x, a, b):
    """
    Compute the indicator function for the interval [a, b] using the Heaviside step function.

    Parameters:
    x (int): The value to check.
    a (int): The lower bound of the interval.
    b (int): The upper bound of the interval.

    Returns:
    int: 1 if x is within the interval [a, b], otherwise 0.
    """
    return heaviside_step_function(x - a) * heaviside_step_function(b - x)

# Define interval bounds
lower_bound = -1
upper_bound = 2

# Check the equality of indicator functions for different x values
for x in range(-3, 4):
    print(indicator_function_1(x, lower_bound, upper_bound) == indicator_function_2(x, lower_bound, upper_bound))

"""
Sample run:
python indicator_functions.py
True
True
True
True
True
True
True
"""

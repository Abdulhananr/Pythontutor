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

print(heaviside_step_function(-0.5))
print(heaviside_step_function(0))
print(heaviside_step_function(10))

"""
Sample run:
python heaviside_step_function.py
0
1
1
"""

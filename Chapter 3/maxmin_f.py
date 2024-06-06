def maxmin(f, a, b, n=1000):
    """
    Find the maximum and minimum values of a function over a given interval.

    Parameters:
    f (function): The function to be evaluated.
    a (float): The lower bound of the interval.
    b (float): The upper bound of the interval.
    n (int): The number of points to sample within the interval (default is 1000).

    Returns:
    tuple: A tuple containing the maximum and minimum values of the function.
    """
    max_f = max(f(a + i * (b - a) / 100) for i in range(n + 1))
    min_f = min(f(a + i * (b - a) / 100) for i in range(n + 1))
    return max_f, min_f

from math import cos, pi

# Test the function with the cosine function over the interval [-pi/2, 2*pi]
print(maxmin(cos, -pi / 2, 2 * pi, 1000001))

"""
Sample run:
python maxmin_function.py
(1.0, -1.0)
"""

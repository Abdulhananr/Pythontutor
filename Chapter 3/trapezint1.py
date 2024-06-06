# Exercise 3.5
# Author: Noah Waterfield Price

from scipy.integrate import quad
from scipy import exp, pi, cos, sin, log


def trapezoidal_integral(f, a, b):
    """
    Compute the approximate integral of a function using the trapezoidal rule.

    Parameters:
        f (function): The function to integrate.
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.

    Returns:
        float: The approximate value of the integral.
    """
    return (b - a) / 2.0 * (f(a) + f(b))

# Define the functions to integrate and their respective intervals
f1 = [exp, 0, log(3)]
f2 = (cos, 0, pi)
f3 = (sin, 0, pi)
f4 = (sin, 0, pi / 2)

# List of functions and their intervals
functions = [f1, f2, f3, f4]


def verify_integral(f, a, b):
    """
    Verify the accuracy of the trapezoidal rule approximation by comparing with the exact integral.

    Parameters:
        f (function): The function to integrate.
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.

    """
    exact_integral, _ = quad(f, a, b)  # Compute the exact integral using scipy's quad function
    approx_integral = trapezoidal_integral(f, a, b)  # Compute the approximate integral using the trapezoidal rule
    error = abs(exact_integral - approx_integral)  # Calculate the error
    print('The exact integral of {} between {:.5f} and {:.5f} is {:.5f}.'
          ' The approximate answer is {:.5f} giving an error of {:.5f}'
          .format(f.__name__, a, b, exact_integral, approx_integral, error))

# Verify the integrals for each function in the list
for f in functions:
    verify_integral(f[0], f[1], f[2])

"""
Sample run:
python trapezint1.py
The exact integral of exp between 0.00000 and 1.09861 is 2.00000. The approximate answer is 2.19722 giving an error of 0.19722
The exact integral of cos between 0.00000 and 3.14159 is 0.00000. The approximate answer is 0.00000 giving an error of 0.00000
The exact integral of sin between 0.00000 and 3.14159 is 2.00000. The approximate answer is 0.00000 giving an error of 2.00000
The exact integral of sin between 0.00000 and 1.57080 is 1.00000. The approximate answer is 0.78540 giving an error of 0.21460
"""

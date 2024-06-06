def numerical_derivative(f, x, h=1E-6):
    """
    Calculate the numerical derivative of a function using the central difference method.
    
    Parameters:
    f (function): The function for which to calculate the derivative.
    x (float): The point at which to calculate the derivative.
    h (float): The step size for the central difference calculation (default is 1E-6).
    
    Returns:
    float: The numerical derivative of the function at the given point.
    """
    return 1 / (2 * h) * (f(x + h) - f(x - h))

from math import exp, cos, sin, pi, log

# Define the functions and their exact derivatives
functions = [
    (lambda x: exp(x), lambda x: exp(x), 'exp(x)'),
    (lambda x: exp(-2 * x ** 2), lambda x: -4 * x * exp(-2 * x ** 2), 'exp(-2x^2)'),
    (lambda x: cos(x), lambda x: -sin(x), 'cos(x)'),
    (lambda x: log(x), lambda x: 1 / x, 'ln(x)')
]

# Values at which to evaluate the derivatives
values = [0, 0, 2 * pi, 1]

print('{:>10} {:>8} {:>8} {:>8}'.format('Function', 'Exact', 'Approx', 'Error'))

# Calculate and print the exact and approximate derivatives
for (f, df, name), x in zip(functions, values):
    exact = df(x)
    approx = numerical_derivative(f, x, h=0.01)
    error = abs(exact - approx)
    print('{:>10} {:>8.6f} {:>8.6f} {:>8.6f}'.format(name, exact, approx, error))

"""
Sample run:
python numerical_derivative.py
  Function    Exact   Approx    Error
    exp(x) 1.000000 1.000017 0.000017
exp(-2x^2) 0.000000 0.000000 0.000000
    cos(x) 0.000000 0.000000 0.000000
     ln(x) 1.000000 1.000033 0.000033
"""

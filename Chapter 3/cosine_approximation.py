def cosine_approximation(x, n):
    """
    Calculate the cosine approximation using a truncated Maclaurin series.
    
    The series used is:
    cos(x) ≈ Σ (-1)^k * (x^(2k) / (2k)!) for k = 0 to n
    
    Parameters:
    x (float): The value at which to approximate the cosine.
    n (int): The number of terms to include in the approximation.
    
    Returns:
    float: The approximation of the cosine of x.
    """
    term = 1
    approximation_sum = term
    for j in range(1, n + 1):
        term *= -x ** 2 / (2. * j * (2. * j - 1.))
        approximation_sum += term
    return approximation_sum


def generate_error_table(x_values):
    """
    Generate and print a table of errors for cosine approximations using different numbers of terms.
    
    The table compares the error between the true value of cos(x) and the approximation
    for various x values and different numbers of terms (n).
    
    Parameters:
    x_values (list of floats): A list of x values for which to calculate the approximation errors.
    """
    from math import cos
    print('{:>7} {:>9} {:>9} {:>9} {:>9} {:>9}'.format('x', 'n=5', 'n=25', 'n=50', 'n=100', 'n=200'))
    for x in x_values:
        errors = [x]
        for n in [5, 25, 50, 100, 200]:
            error = cos(x) - cosine_approximation(x, n)
            errors.append(error)
        print('{:7.4f} {:9.2e} {:9.2e} {:9.2e} {:9.2e} {:9.2e}'.format(*errors))


# Define the x values for which to calculate the cosine approximations
from math import pi
x_values = [4 * pi, 6 * pi, 8 * pi, 10 * pi]

# Generate and print the error table
generate_error_table(x_values)

"""
Sample run:
python cosine_approximation.py
      x       n=5      n=25      n=50     n=100     n=200 
12.5664  1.61e+04  1.45e-11 -2.44e-12 -2.44e-12 -2.44e-12
18.8496  1.22e+06  2.28e-02  2.34e-10  2.34e-10  2.34e-10
25.1327  2.41e+07  6.58e+04 -2.40e-08 -2.40e-08 -2.40e-08
31.4159  2.36e+08  6.52e+09 -1.20e-04 -1.20e-04 -1.20e-04
"""

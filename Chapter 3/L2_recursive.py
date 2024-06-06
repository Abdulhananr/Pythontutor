def L(x, n):
    """
    Compute the approximation of ln(1+x) using the third Laguerre polynomial.

    Parameters:
    x (float): The value at which to evaluate the function.
    n (int): The number of terms in the series.

    Returns:
    tuple: A tuple containing the value of the sum, the next term, and the exact error.
    """
    term = x / (1. + x)
    s = term
    for i in range(2, n + 1):
        # Recursive relation between c(i) and c(i-1)
        term *= (i - 1.) / i * x / (1. + x)
        s += term
    value_of_sum = s
    first_neglected_term = term * n / (n + 1.) * x / (1. + x)
    from math import log
    exact_error = log(1 + x) - value_of_sum
    return value_of_sum, first_neglected_term, exact_error


def table(x):
    """
    Print a table of results for different values of n.

    Parameters:
    x (float): The value at which to evaluate the function.
    """
    from math import log
    print('\nx=%g, ln(1+x)=%g' % (x, log(1 + x)))
    for n in [1, 2, 10, 100, 500]:
        value, next_term, error = L(x, n)
        print('n=%-4d %-10g  (next term: %8.2e  error: %8.2e)' % (n, value, next_term, error))

table(10)
table(100)
table(1000)


def L2(x, epsilon=1.0E-6):
    """
    Compute the approximation of ln(1+x) using the third Laguerre polynomial until the desired accuracy is reached.

    Parameters:
    x (float): The value at which to evaluate the function.
    epsilon (float): The desired accuracy.

    Returns:
    tuple: A tuple containing the approximation and the number of terms used.
    """
    term = x / (1. + x)
    s = term
    i = 1
    while abs(term) > epsilon:
        i += 1
        # Recursive relation between c(i) and c(i-1)
        term *= (i - 1.) / i * x / (1. + x)
        s += term
    return s, i

print('\n\n')
from math import log
x = 10
for k in range(4, 14, 2):
    epsilon = 10 ** (-k)
    approx, n = L2(x, epsilon=epsilon)
    exact = log(1 + x)
    exact_error = exact - approx
    print('epsilon: %5.0e, exact error: %8.2e, n=%d' % (epsilon, exact_error, n))

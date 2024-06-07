import sys
import math


def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    Returns 1 if n is 0 or 1, otherwise computes the factorial iteratively.
    """
    return math.factorial(n)


def binomial(x, n, p):
    """
    Calculate the binomial probability of having exactly x successes
    in n trials with a probability of success p in each trial.

    The binomial probability formula is:
    B(x; n, p) = (n! / (x! * (n - x)!)) * p^x * (1 - p)^(n - x)
    """
    B = float(factorial(n)) / (factorial(x) * factorial(n - x)) * p ** x * (1 - p) ** (n - x)
    return B

if __name__ == "__main__":
    try:
        # Read command line arguments
        x = int(sys.argv[1])
        n = int(sys.argv[2])
        p = float(sys.argv[3])
    except IndexError:
        # Handle case where not enough arguments are provided
        print('x, n, and p must be supplied on the command line')
        sys.exit(1)
    except ValueError:
        # Handle case where arguments cannot be converted to required types
        print('x and n must be integers and p must be a real number')
        sys.exit(1)

    # Print the calculated binomial probability
    print(binomial(x, n, p))

"""
Sample run:
python binomial_distribution.py 3 3 0.5
0.125
python binomial_distribution.py 2 5 0.5
0.3125
"""


from math import *
import sys
import random

# Store the filename and usage information
_filename = sys.argv[0]
_usage = """
Usage: python %s exp(a+b) exp(a)*exp(b) -100 100 500
Takes two equivalent expressions involving a and b and
tests their equivalence. Returning the percentage of
failures.
""" % _filename


def equal(expr1, expr2, A, B, n=500):
    failures = n
    # Loop for 'n' iterations
    for _ in range(n):
        a = random.uniform(A, B)
        b = random.uniform(A, B)
        # Evaluate both expressions and compare
        if eval(expr1) == eval(expr2):
            failures -= 1
    failure_rate = (failures / n) * 100
    return failure_rate


if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 5:
        print(_usage)
        raise IndexError('Two expressions involving a and b and range limits '
                         'must be given on the command-line. Number '
                         'of repetitions may also be given.')
    # Read command line arguments
    expr1 = sys.argv[1]
    expr2 = sys.argv[2]
    A = float(sys.argv[3])
    B = float(sys.argv[4])

    if len(sys.argv) == 6:
        n = int(sys.argv[5])
        failure_rate = equal(expr1, expr2, A, B, n)
    else:
        failure_rate = equal(expr1, expr2, A, B)

    # Print the failure rate
    print(f"{expr1} and {expr2} - Failure rate = {failure_rate:.2f}%")

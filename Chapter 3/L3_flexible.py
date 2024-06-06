def L3(x, n=None, epsilon=None, return_n=False):
    """
    Compute the third Laguerre polynomial using either the number of terms (n) or the desired accuracy (epsilon).

    Parameters:
    x (float): The value at which to evaluate the polynomial.
    n (int): The number of terms to compute (optional).
    epsilon (float): The desired accuracy (optional).
    return_n (bool): If True, return the number of terms used (optional).

    Returns:
    float or tuple: The value of the third Laguerre polynomial or a tuple containing the value and the number of terms used.
    """
    if (n is None and epsilon is None) or (n is not None and epsilon is not None):
        print("Error: Either n or epsilon must be given (not both)")
        return None

    term = x / (1. + x)
    s = term

    if n is not None:
        for i in range(2, n + 1):
            # recursive relation between ci and c(i-1)
            term *= (i - 1.) / i * x / (1. + x)
            s += term
        return (s, n) if return_n else s

    elif epsilon is not None:
        i = 1
        while abs(term) > epsilon:
            i += 1
            # recursive relation between ci and c(i-1)
            term *= (i - 1.) / i * x / (1. + x)
            s += term
        return (s, i) if return_n else s

# Test the function with different parameters
print(L3(10, n=100))
print(L3(10, n=1000, return_n=True))
print(L3(10, epsilon=1e-10))
print(L3(10, epsilon=1e-10, return_n=True))

"""
Sample run:
python L3_flexible.py
2.39788868474
(2.397895272798365, 1000)
2.39789527188
(2.397895271877886, 187)
"""

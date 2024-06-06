def factorial(n):
    """
    Calculate the factorial of a given number.
    
    Parameters:
    n (int): The number for which to calculate the factorial.
    
    Returns:
    int: The factorial of the given number.
    """
    result = 1
    if n == 0 or n == 1:
        return result
    else:
        while n > 0:
            result *= n
            n -= 1
    return result

print(factorial(5))

"""
Sample run:
python factorial.py
120
"""

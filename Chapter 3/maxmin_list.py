def my_max(a):
    """
    Find the maximum element in a list.

    Parameters:
    a (list): The list of numbers.

    Returns:
    int: The maximum element in the list.
    """
    max_elem = a[0]
    for elem in a:
        if elem > max_elem:
            max_elem = elem
    return max_elem


def my_min(a):
    """
    Find the minimum element in a list.

    Parameters:
    a (list): The list of numbers.

    Returns:
    int: The minimum element in the list.
    """
    min_elem = a[0]
    for elem in a:
        if elem < min_elem:
            min_elem = elem
    return min_elem

# Test the functions with sample lists
print(my_max([1, 5, 6, -2, 4, -7, -4, 2, 6, 5, 11, 3, 5]))
print(my_min([1, 5, 6, -2, 4, -7, -4, 2, 6, 5, 11, 3, 5]))

"""
Sample run:
python maxmin_list.py
11
-7
"""

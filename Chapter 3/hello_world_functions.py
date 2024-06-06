def hello_world_return():
    """
    Return the string 'Hello, World!'.

    Returns:
    str: The string 'Hello, World!'.
    """
    return 'Hello, World!'


def hello_world_print():
    """
    Print the string 'Hello, World!'.
    """
    print('Hello, World!')


def hello_world_with_strings(s1, s2):
    """
    Print a combination of two strings.

    Parameters:
    s1 (str): The first string.
    s2 (str): The second string.
    """
    print(s1 + ', ' + s2)


# Call the functions and demonstrate their behavior
print(hello_world_return())  # Call function 1 and print the returned string
hello_world_print()  # Call function 2 to print the string directly
hello_world_with_strings('Hello', 'World!')  # Call function 3 with two strings

"""
Sample run:
python hello_world_functions.py
Hello, World!
Hello, World!
Hello, World!
"""

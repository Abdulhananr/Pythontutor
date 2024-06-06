def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.
    
    Returns:
    float or str: Temperature in Celsius if conversion is accurate, otherwise 'Error'.
    """
    celsius = (5.0 / 9) * (fahrenheit - 32)
    fahrenheit_check = (9.0 / 5) * celsius + 32
    return celsius if abs(fahrenheit_check - fahrenheit) < 1E-12 else 'Error'

# Example conversion
print(fahrenheit_to_celsius(30))

"""
Sample run:
python fahrenheit_to_celsius.py
-1.11111111111
"""

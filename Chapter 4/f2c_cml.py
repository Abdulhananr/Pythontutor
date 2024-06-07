import sys

# Read the Fahrenheit temperature from the command line argument
F = float(sys.argv[1])

# Convert Fahrenheit to Celsius
C = 5 / 9 * (F - 32)

# Print the result
print(f"{F} Fahrenheit = {C} Celsius")

"""
Sample run:
python f2c_cml.py 243
243 Fahrenheit = 117.222 Celsius
"""

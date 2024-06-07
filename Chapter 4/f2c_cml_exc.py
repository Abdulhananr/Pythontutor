import sys

try:
    # Read the temperature in Fahrenheit from the command line arguments
    F = float(sys.argv[1])
except IndexError:
    # Handle case where no temperature is provided
    print('You failed to provide a temperature in Fahrenheit as input on the command line!')
    sys.exit(1)  # abort the program
except ValueError:
    # Handle case where the provided value is not a valid float
    print('The provided temperature must be a valid number.')
    sys.exit(1)  # abort the program

# Convert the temperature from Fahrenheit to Celsius
C = 5.0 / 9 * (F - 32)

# Print the result
print(f"{F} Fahrenheit = {C} Celsius")

"""
Sample run:
python f2c_cml_exc.py
You failed to provide a temperature in Fahrenheit as input on the command line!
python f2c_cml_exc.py 243
243 Fahrenheit = 117.222 Celsius
"""

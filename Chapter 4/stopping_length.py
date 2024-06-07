import sys

# Define the acceleration due to gravity (in m/s^2)
g = 9.81  

try:
    # Convert initial velocity from km/h to m/s
    v0 = (1000. / 3600) * float(sys.argv[1])
    mu = float(sys.argv[2])  # coefficient of friction
except IndexError:
    # Prompt user for input if command-line arguments are missing
    print('Both v0 (in km/h) and mu must be supplied on the command line')
    v0 = (1000. / 3600) * float(input('v0 = ?\n'))
    mu = float(input('mu = ?\n'))
except ValueError:
    # Handle invalid input values
    print('v0 and mu must be pure numbers')
    sys.exit(1)

# Compute the stopping distance using the formula: d = 0.5 * v0^2 / mu / g
d = 0.5 * v0 ** 2 / mu / g
print(d)

"""
Sample run:
python stopping_length.py 120 0.3
188.771850342
python stopping_length.py 50 0.3
32.7728906843
"""

# Explanation:
# 1. The code calculates the stopping distance of a vehicle given the initial velocity (v0) and the coefficient of friction (mu).
# 2. The acceleration due to gravity (g) is defined as 9.81 m/s^2.
# 3. Command-line arguments are parsed for v0 (in km/h) and mu.
# 4. If command-line arguments are missing or invalid, the code prompts the user for input.
# 5. The stopping distance (d) is computed using the formula d = 0.5 * v0^2 / mu / g.
# 6. The result is printed to the console.
# 7. Sample runs demonstrate how to use the script with different initial velocities and coefficients of friction.

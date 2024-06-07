import sys

# Gravitational constant in meters per second squared
g = 9.81

try:
    # Read command line arguments
    v0 = float(sys.argv[1])
    t = float(sys.argv[2])
except IndexError:
    # Handle case where not enough arguments are provided
    print('Both v0 and t must be supplied on the command line')
    # Prompt user for input if arguments are not provided
    v0 = float(input('v0 = ?\n'))
    t = float(input('t = ?\n'))
except ValueError:
    # Handle case where arguments cannot be converted to required types
    print('v0 and t must be pure numbers')
    sys.exit(1)

# Calculate the position y of the ball at time t
y = v0 * t - 0.5 * g * t ** 2

# Print the calculated position
print(y)

"""
Sample run:
python ball_cml_qa.py
Both v0 and t must be supplied on the command line
v0 = ?
6
t = ?
4
-54.48
python ball_cml_qa.py 3 fw
v0 and t must be pure numbers
python ball_cml_qa.py 6 4
-54.48
"""

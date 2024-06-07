

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

# Check if the provided time t is within the physical bounds
if t < 0 or t > 2 * v0 / g:
    raise ValueError(f't={t} is a non-physical value. Must be between 0 and 2v0/g')
    sys.exit(1)

# Calculate the position y of the ball at time t
y = v0 * t - 0.5 * g * t ** 2

# Print the calculated position
print(y)

"""
Sample run:
python ball_cml_errorcheck.py
Both v0 and t must be supplied on the command line
v0 = ?
6
t = ?
3
Traceback (most recent call last):
  File "ball_cml_errorcheck.py", line 16, in <module>
    'must be between 0 and 2v0/g' % t)
ValueError: t=3 is a non-physical value. Must be between 0 and 2v0/g
python ball_cml_qa.py 3 fw
v0 and t must be pure numbers
python ball_cml_qa.py 6 1
1.095
"""

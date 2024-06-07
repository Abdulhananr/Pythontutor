

import argparse

# Gravitational constant in meters per second squared
g = 9.81

# Initialize the argument parser
parser = argparse.ArgumentParser(description="Calculate the position of a ball in free fall.")

# Add arguments for initial velocity (v0) and time (t)
parser.add_argument('--v0', '--initial_velocity', type=float,
                    default=0.0, help='initial velocity', metavar='v')
parser.add_argument('--t', '--time', type=float, default=1.0,
                    help='time', metavar='t')

# Parse the arguments
args = parser.parse_args()

# Calculate the position y of the ball at time t
y = args.v0 * args.t - 0.5 * g * args.t ** 2

# Print the calculated position
print(y)

"""
Sample run:
python ball_cml.py --v0 10 --t 4
-38.48
"""


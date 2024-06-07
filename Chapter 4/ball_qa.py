# Gravitational constant in meters per second squared
g = 9.81

# Prompt user for initial velocity and time, and convert inputs to float
v0 = float(input('v0 = ?\n'))
t = float(input('t = ?\n'))

# Calculate the position y of the ball at time t
y = v0 * t - 0.5 * g * t ** 2

# Print the calculated position
print(y)

"""
Sample run:
python ball_qa.py
v0 = ?
10
t = ?
4
-38.48
"""

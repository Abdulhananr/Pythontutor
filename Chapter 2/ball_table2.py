# Initial velocity (m/s)
initial_velocity = 10

# Acceleration due to gravity (m/s^2)
gravity = 9.81

# Number of time intervals
num_intervals = 81

# Time step size (s)
time_step = 2 * initial_velocity / gravity / (num_intervals - 1)

# List of time values
time_values = [i * time_step for i in range(num_intervals)]

# List of position values
position_values = [initial_velocity * time_values[i] - 0.5 * gravity * time_values[i] ** 2 for i in range(num_intervals)]

# Print the header of the table
print(f'{"t":>6} {"y":>6}')

# Loop over time and position values and print them
for tval, yval in zip(time_values, position_values):
    print(f'{tval:6.3f} {yval:6.3f}')

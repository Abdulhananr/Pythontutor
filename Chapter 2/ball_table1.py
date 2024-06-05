# Initial velocity (m/s)
initial_velocity = 1

# Acceleration due to gravity (m/s^2)
gravity = 9.81

# Number of time intervals
num_intervals = 11

# Time step size (s)
time_step = 2 * initial_velocity / gravity / (num_intervals - 1)

# Print the header of the table
print(f'{"t":>6} {"y":>6}')

# Loop over the number of intervals
for interval in range(num_intervals):
    # Calculate the time at the current interval
    time = interval * time_step
    
    # Calculate the position at the current time
    position = initial_velocity * time - 0.5 * gravity * time ** 2
    
    # Print the time and position, formatted to 3 decimal places
    print(f'{time:6.3f} {position:6.3f}')

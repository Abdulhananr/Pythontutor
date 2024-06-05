from math import pi

# Define the drag coefficient
drag_coefficient = 0.2

# Define the density of air (kg/m^3)
air_density = 1.2

# Calculate the football cross-sectional area (m^2)
football_area = pi * 0.11 ** 2

# Define the football mass (kg)
football_mass = 0.43

# Define the gravitational acceleration (m/s^2)
gravity = 9.81

# Calculate the gravitational force (N)
gravitational_force = football_mass * gravity

# Define the speed conversion factor (km/h to m/s)
speed_conversion_factor = 1000.0 / 3600

# Define the hard kick velocity (m/s)
hard_kick_velocity = 120 * speed_conversion_factor

# Calculate the drag force for a hard kick (N)
hard_kick_drag_force = 0.5 * drag_coefficient * air_density * football_area * hard_kick_velocity ** 2

print(f'For a hard kick (v = {hard_kick_velocity:.4f}), the gravitational force is {gravitational_force:.4f} and the drag force is {hard_kick_drag_force:.4f}')

# Define the soft kick velocity (m/s)
soft_kick_velocity = 10 * speed_conversion_factor

# Calculate the drag force for a soft kick (N)
soft_kick_drag_force = 0.5 * drag_coefficient * air_density * football_area * soft_kick_velocity ** 2

print(f'For a soft kick (v = {soft_kick_velocity:.4f}), the gravitational force is {gravitational_force:.4f} and the drag force is {soft_kick_drag_force:.4f}')


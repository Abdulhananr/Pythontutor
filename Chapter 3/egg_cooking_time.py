from math import log, pi

def egg_cooking_time(mass, initial_temp, desired_temp):
    """
    Calculate the cooking time for an egg based on its mass, initial temperature, and desired temperature.
    
    Parameters:
    mass (float): The mass of the egg in kilograms.
    initial_temp (float): The initial temperature of the egg in Kelvin.
    desired_temp (float): The desired temperature of the egg in Kelvin.
    
    Returns:
    float: The cooking time in seconds.
    """
    egg_density = 1.038 * 1000  # Egg density (kg/m^3)
    specific_heat_capacity = 3.7 * 1000  # Specific heat capacity (J/kg/K)
    thermal_conductivity = 0.54  # Thermal conductivity (W/m/K)
    boiling_water_temp = 373.15  # Boiling water temperature (K)
    
    cooking_time = (mass ** (2.0 / 3) * specific_heat_capacity * egg_density ** (1.0 / 3) /
                    (thermal_conductivity * pi ** 2 * (4 * pi / 3) ** (2.0 / 3)) *
                    log(0.76 * (initial_temp - boiling_water_temp) / 
                        (desired_temp - boiling_water_temp)))
    return cooking_time

# Egg from fridge
initial_temp_fridge = 277.15
# Soft boiled
desired_temp_soft = 63 + 273.15
# Small egg
mass_small_egg = 0.047
cooking_time_small_soft_fridge = egg_cooking_time(mass_small_egg, initial_temp_fridge, desired_temp_soft)
# Large egg
mass_large_egg = 0.067
cooking_time_large_soft_fridge = egg_cooking_time(mass_large_egg, initial_temp_fridge, desired_temp_soft)
print(f'From the fridge: to soft boil a small egg cook for {cooking_time_small_soft_fridge / 60:.2f} minutes '
      f'and a large egg for {cooking_time_large_soft_fridge / 60:.2f} minutes.')

# Hard boiled
desired_temp_hard = 70 + 273.15
# Small egg
cooking_time_small_hard_fridge = egg_cooking_time(mass_small_egg, initial_temp_fridge, desired_temp_hard)
# Large egg
cooking_time_large_hard_fridge = egg_cooking_time(mass_large_egg, initial_temp_fridge, desired_temp_hard)
print(f'From the fridge: to hard boil a small egg cook for {cooking_time_small_hard_fridge / 60:.2f} minutes '
      f'and a large egg for {cooking_time_large_hard_fridge / 60:.2f} minutes.')

# Egg at room temperature
initial_temp_room = 293.15
# Soft boiled
cooking_time_small_soft_room = egg_cooking_time(mass_small_egg, initial_temp_room, desired_temp_soft)
cooking_time_large_soft_room = egg_cooking_time(mass_large_egg, initial_temp_room, desired_temp_soft)
print(f'At room temperature: to soft boil a small egg cook for {cooking_time_small_soft_room / 60:.2f} minutes '
      f'and a large egg for {cooking_time_large_soft_room / 60:.2f} minutes.')

# Hard boiled
cooking_time_small_hard_room = egg_cooking_time(mass_small_egg, initial_temp_room, desired_temp_hard)
cooking_time_large_hard_room = egg_cooking_time(mass_large_egg, initial_temp_room, desired_temp_hard)
print(f'At room temperature: to hard boil a small egg cook for {cooking_time_small_hard_room / 60:.2f} minutes '
      f'and a large egg for {cooking_time_large_hard_room / 60:.2f} minutes.')

"""
Sample run:
python egg_cooking_time.py
From the fridge: to soft boil a small egg cook for 3.99 minutes and a large egg for 5.05 minutes.
From the fridge: to hard boil a small egg cook for 5.22 minutes and a large egg for 6.61 minutes.
At room temperature: to soft boil a small egg cook for 2.92 minutes and a large egg for 3.69 minutes.
At room temperature: to hard boil a small egg
"""
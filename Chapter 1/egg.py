from math import log, pi

# Constants
egg_density = 1.038 * 1000  # Egg density (kg/m^3)
specific_heat_capacity = 3.7 * 1000  # Specific heat capacity (J/kg*K)
thermal_conductivity = 0.54  # Thermal conductivity (W/m*K)
boiling_water_temperature = 373.15  # Boiling water temperature (K)
desired_yolk_temperature = 343.15  # Desired yolk temperature (K)

# Egg from fridge
initial_temperature = 277.15  # Initial temperature (K)
small_egg_mass = 0.047  # Mass of small egg (kg)
large_egg_mass = 0.067  # Mass of large egg (kg)

small_egg_cooking_time = (small_egg_mass ** (2.0 / 3) * specific_heat_capacity * egg_density ** (1.0 / 3) / 
                          (thermal_conductivity * pi ** 2 * (4 * pi / 3) ** (2.0 / 3)) * 
                          log(0.76 * (initial_temperature - boiling_water_temperature) / 
                              (desired_yolk_temperature - boiling_water_temperature)))

large_egg_cooking_time = (large_egg_mass ** (2.0 / 3) * specific_heat_capacity * egg_density ** (1.0 / 3) / 
                          (thermal_conductivity * pi ** 2 * (4 * pi / 3) ** (2.0 / 3)) * 
                          log(0.76 * (initial_temperature - boiling_water_temperature) / 
                              (desired_yolk_temperature - boiling_water_temperature)))

print('From the fridge: to hard boil a small egg cook for %.2f minutes and a large egg for %.2f minutes.' % 
      (small_egg_cooking_time / 60, large_egg_cooking_time / 60))

# Egg at room temperature
initial_temperature = 293.15  # Initial temperature (K)

small_egg_cooking_time = (small_egg_mass ** (2.0 / 3) * specific_heat_capacity * egg_density ** (1.0 / 3) / 
                          (thermal_conductivity * pi ** 2 * (4 * pi / 3) ** (2.0 / 3)) * 
                          log(0.76 * (initial_temperature - boiling_water_temperature) / 
                              (desired_yolk_temperature - boiling_water_temperature)))

large_egg_cooking_time = (large_egg_mass ** (2.0 / 3) * specific_heat_capacity * egg_density ** (1.0 / 3) / 
                          (thermal_conductivity * pi ** 2 * (4 * pi / 3) ** (2.0 / 3)) * 
                          log(0.76 * (initial_temperature - boiling_water_temperature) / 
                              (desired_yolk_temperature - boiling_water_temperature)))

print('At room temperature: to hard boil a small egg cook for %.2f minutes and a large egg for %.2f minutes.' % 
      (small_egg_cooking_time / 60, large_egg_cooking_time / 60))



# Define the densities in g/cm^3
iron_density_gcm3 = 7.8
air_density_gcm3 = 0.0012
gasoline_density_gcm3 = 0.67
ice_density_gcm3 = 0.9
human_body_density_gcm3 = 1.03
silver_density_gcm3 = 10.5
platinum_density_gcm3 = 21.4

# Define the volume of 1 liter in cm^3
liter_cm3 = 1000

# Calculate the weight of 1 liter of each substance in grams
iron_weight_grams = iron_density_gcm3 * liter_cm3
air_weight_grams = air_density_gcm3 * liter_cm3
gasoline_weight_grams = gasoline_density_gcm3 * liter_cm3
ice_weight_grams = ice_density_gcm3 * liter_cm3
human_body_weight_grams = human_body_density_gcm3 * liter_cm3
silver_weight_grams = silver_density_gcm3 * liter_cm3
platinum_weight_grams = platinum_density_gcm3 * liter_cm3

# Print the results
print(f'One liter of iron weighs {iron_weight_grams:.2f} grams')
print(f'One liter of air weighs {air_weight_grams:.2f} grams')
print(f'One liter of gasoline weighs {gasoline_weight_grams:.2f} grams')
print(f'One liter of ice weighs {ice_weight_grams:.2f} grams')
print(f'One liter of human body weighs {human_body_weight_grams:.2f} grams')
print(f'One liter of silver weighs {silver_weight_grams:.2f} grams')
print(f'One liter of platinum weighs {platinum_weight_grams:.2f} grams')


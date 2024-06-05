# Define the conversion factors
inch_to_meter = 0.0254
foot_to_meter = inch_to_meter * 12
yard_to_meter = foot_to_meter * 3
mile_to_meter = yard_to_meter * 1760

# Get the distance in meters from the user
distance_in_meters = float(input('Enter distance in meters to be converted to imperial units\n'))

# Calculate the equivalent distances
distance_in_inches = distance_in_meters / inch_to_meter
distance_in_feet = distance_in_meters / foot_to_meter
distance_in_yards = distance_in_meters / yard_to_meter
distance_in_miles = distance_in_meters / mile_to_meter

# Print the results
print('{m:.2f} meters is equivalent to {i:.2f} inches, {f:.2f} feet, {y:.2f} yards, {mi:.2f} miles.'.format(
	m=distance_in_meters, 
	i=distance_in_inches, 
	f=distance_in_feet, 
	y=distance_in_yards, 
	mi=distance_in_miles
))


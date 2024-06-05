# Step size
h = 0.01

# List to hold x values
x_values = []

# Generate x values from 1 to 2 with step size h
for i in range(101):
    x_values.append(1 + i * h)

# Print x values formatted to 2 decimal places
for x_val in x_values:
    print(f'{x_val:3.2f}', end=', ')

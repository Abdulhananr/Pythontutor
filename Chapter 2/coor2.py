# Step size
h = 0.01

# List comprehension to generate x values from 1 to 2 with step size h
x_values = [1 + i * h for i in range(101)]

# Print x values formatted to 2 decimal places
for x_val in x_values:
    print(f'{x_val:3.2f}', end=' ')

# Print a newline at the end for clean output
print()

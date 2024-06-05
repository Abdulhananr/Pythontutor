
# Calculate a and b
a = 1 / 947.0 * 947
b = 1

# Check if a is not equal to b using direct comparison
if a != b:
    print('Wrong result!')

# Recalculate a and b
a = 1 / 947.0 * 947
b = 1

# Check if the difference between a and b is greater than a small tolerance (1e-15)
if abs(a - b) > 1e-15:
    print('Wrong result!')
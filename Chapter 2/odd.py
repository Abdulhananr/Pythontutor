# Define the value of n
n = 12

# Initialize the counter variable i to 0
i = 0

# Iterate while i is less than half of n (rounded to the nearest integer)
while i < int(round(n / 2.)):
    # Print the odd numbers (2 * i + 1)
    print(2 * i + 1, end=' ')
    
    # Increment i by 1
    i += 1

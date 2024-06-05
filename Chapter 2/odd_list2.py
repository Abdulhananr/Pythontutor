# Define the value of n
n = 12

# Initialize the counter variable i to 0
i = 0

# Initialize an empty list to store the odd numbers
odd_nos = []

# Iterate while i is less than half of n (rounded to the nearest integer)
while i < int(round(n / 2.)):
    # Append the odd numbers (2 * i + 1) to the list odd_nos
    odd_nos.append(2 * i + 1)
    
    # Increment i by 1
    i += 1

# Iterate over each odd number in the list odd_nos and print them
for no in odd_nos:
    print(no, end=' ')

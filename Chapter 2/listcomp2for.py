# Initialize an empty list to store the values of r
r_list = []

# Generate values for r ranging from 10^0 to 10^4
for i in range(5):
    r_list.append(10 ** i)

# Initialize an empty list to store the square of each value of r
q1 = []

# Calculate the square of each value of r and append it to q1
for r in r_list:
    q1.append(r ** 2)

# Using list comprehension, create a list q2 containing the squares of values of r ranging from 10^0 to 10^4
q2 = [r ** 2 for r in [10 ** i for i in range(5)]]

# Compare q1 and q2 for equality
print(q1 == q2)

# Generate Fahrenheit values from 0 to 100 in steps of 10
F = [i for i in range(0, 110, 10)]

# Convert Fahrenheit to Celsius
C = [(5.0 / 9) * (F[i] - 32) for i in range(len(F))]

# Approximate conversion from Fahrenheit to Celsius
C_approx = [0.5 * (F[i] - 30) for i in range(len(F))]

# Combine F, C, and C_approx values into a single list
conversion = [[Fval, Cval, C_approxval] for Fval, Cval, C_approxval in zip(F, C, C_approx)]

# Print the table header
print('------------------------')
print(f'{"F":>6} {"C":>8} {"~C":>8}')  # column headers

# Print each row of the conversion table
for Fval, Cval, C_approxval in conversion:
    print(f'{Fval:6.2f} {Cval:8.2f} {C_approxval:8.2f}')
print('------------------------')

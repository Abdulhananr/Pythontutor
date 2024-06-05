# Print a line of hyphens to serve as the table heading separator
print('------------------------')

# Initial value for Fahrenheit
F = 0

# Increment value for Fahrenheit in the loop
dC = 10

# Print column headers for Fahrenheit, Celsius, and approximate Celsius
print('%6s %8s %8s' % ('F', 'C', '~C'))

# Loop until Fahrenheit reaches 100
while F <= 100:
    # Convert Fahrenheit to Celsius
    C = (5.0 / 9) * (F - 32)
    
    # Approximate Celsius using a simpler formula
    C_approx = 0.5 * (F - 30)
    
    # Print Fahrenheit, Celsius, and approximate Celsius values
    print('%6.2f %8.2f %8.2f' % (F, C, C_approx))
    
    # Increment Fahrenheit by dC
    F = F + dC

# Print a line of hyphens to mark the end of the table
print('------------------------')

from math import sqrt

# Iterate over a range of values for n from 1 to 59
for n in range(1, 60):
    # Initialize the value of r to 2.0
    r = 2.0
    
    # Perform square root operation 'n' times
    for i in range(n):
        r = sqrt(r)
    
    # Perform squaring operation 'n' times
    for i in range(n):
        r = r ** 2
    
    # Print the result after 'n' times of sqrt and **2 operations
    print('%d times sqrt and **2: %.16f' % (n, r))

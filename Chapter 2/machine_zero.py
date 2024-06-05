# Initialize the variable eps to 1.0
eps = 1.0

# Loop until the condition 1.0 != 1.0 + eps is no longer true
while 1.0 != 1.0 + eps:
    # Print the current value of eps
    print('...............', eps)
    
    # Divide eps by 2.0 in each iteration
    eps /= 2.0

# Print the final value of eps when the loop exits
print('final eps:', eps)

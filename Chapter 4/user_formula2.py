from scitools.StringFunction import StringFunction

# Prompt user to enter a formula involving x
formula = input('Write a formula involving x: ')

# Create a function object from the user-provided formula
f = StringFunction(formula)

# Initialize x
x = 0

# Continue evaluating the function until the user enters None
while x is not None:
    # Prompt user to enter the value of x
    x_input = input('Give x (None to quit): ')

    # Check if the user wants to quit
    if x_input.lower() == 'none':
        x = None
    else:
        # Evaluate the function at the provided value of x and print the result
        x = eval(x_input)
        print('f(%g)=%g' % (x, f(x)))

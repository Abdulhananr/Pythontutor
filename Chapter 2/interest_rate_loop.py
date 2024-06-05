# Initial amount of money
initial_amount = 100

# Interest rate
p = 5.5  # percentage interest rate

# Amount of money
amount = initial_amount

# Years counter
years = 0

# Loop until the amount of money reaches 1.5 times the initial amount
while amount <= 1.5 * initial_amount:
    # Increase the amount of money by the interest earned in one year
    amount += p / 100. * initial_amount
    
    # Increment the number of years
    years += 1

# Print the number of years it took for the amount of money to reach 1.5 times its initial value
print(years)

"""
This program calculated the amount of years it takes for an amount of money to reach 1.5
times its value, given and interest rate of p To solve the integer division error if p is an 
int, it was necessary to change p/100 to p/100.
"""

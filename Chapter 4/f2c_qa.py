# Prompt the user to enter a temperature in Fahrenheit
F = input("Enter a temperature in Fahrenheit:\n")

# Convert the input to a float
F = float(F)

# Convert Fahrenheit to Celsius
C = 5 / 9 * (F - 32)

# Print the result
print(f"{F} Fahrenheit = {C} Celsius")

"""
Sample run:
python f2c_qa.py
Enter a temperature in Fahrenheit:
243
243 Fahrenheit = 117.222 Celsius
"""

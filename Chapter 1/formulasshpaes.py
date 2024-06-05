from math import pi

# Define the dimensions
height = 5.0  # height of the parallelogram
base = 2.0  # base of the parallelogram and side of the square
radius = 1.5  # radius of the circle

# Calculate the area of the parallelogram
parallelogram_area = height * base
print(f'The area of the parallelogram is {parallelogram_area:.3f}')  # print with 3 decimal places

# Calculate the area of the square
square_area = base ** 2
print(f'The area of the square is {square_area:.0f}')  # print as an integer

# Calculate the area of the circle
circle_area = pi * radius ** 2
print(f'The area of the circle is {circle_area:.0f}')  # print as an integer

# Calculate the volume of the cone
cone_volume = 1.0 / 3 * pi * radius ** 2 * height
print(f'The volume of the cone is {cone_volume:.3f}')  # print with 3 decimal places


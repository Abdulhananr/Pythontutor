def calculate_triangle_area(vertices):
    """
    Calculate the area of a triangle given its vertices using the Shoelace formula.
    
    The Shoelace formula for a triangle with vertices (x1, y1), (x2, y2), (x3, y3) is:
    Area = 0.5 * abs(x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 - y3*x1)
    
    Parameters:
    vertices (list of tuples): A list containing three tuples, each representing the coordinates (x, y) of a vertex.
    
    Returns:
    float: The area of the triangle.
    """
    A = 0.5 * abs(vertices[0][0] * vertices[1][1] + 
                  vertices[1][0] * vertices[2][1] + 
                  vertices[2][0] * vertices[0][1] - 
                  vertices[1][0] * vertices[0][1] - 
                  vertices[2][0] * vertices[1][1] - 
                  vertices[0][0] * vertices[2][1])
    return A

# Define the vertices of the triangle
vertex1 = (0, 0)
vertex2 = (1, 0)
vertex3 = (0, 2)
triangle_vertices = [vertex1, vertex2, vertex3]

# Calculate the area of the triangle
triangle_area = calculate_triangle_area(triangle_vertices)

# Print the area of the triangle
print('Area of the triangle is %.2f' % triangle_area)

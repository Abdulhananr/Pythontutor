from math import sqrt


def pathlength(x, y):
    L = 0
    for i in range(1, len(x)):
        dL_squared = (x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2
        L += sqrt(dL_squared)
    return L

points = [(1, 1), (2, 1), (1, 2), (1, 1)]

x = [point[0] for point in points]
y = [point[1] for point in points]

print(pathlength(x, y))

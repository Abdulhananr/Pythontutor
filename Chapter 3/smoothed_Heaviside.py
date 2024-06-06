from math import sin, pi


def smoothed_Heaviside(x, e=1E-2):
    if x < -e:
        return 0
    elif -e <= x <= e:
        return 0.5 + x / (2 * e) + 1 / (2 * pi) * sin(pi * x / e)
    elif x > e:
        return 1

print(smoothed_Heaviside(-1))
print(smoothed_Heaviside(-0.01))
print(smoothed_Heaviside(-0.001))
print(smoothed_Heaviside(0.001))
print(smoothed_Heaviside(0.01))
print(smoothed_Heaviside(1))

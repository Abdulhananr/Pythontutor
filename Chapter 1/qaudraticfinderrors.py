from cmath import sqrt

a = 2
b = 1
c = 2
q = sqrt(b * b - 4 * a * c)
x1 = (-b + q) / (2 * a)
x2 = (-b - q) / (2 * a)

print(x1,"\n"+x2)
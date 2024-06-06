roots = [-1, 1, 2]


def poly(roots, x):
    p = 1
    for root in roots:
        p *= (x - root)
    return p

print(poly(roots, 3))

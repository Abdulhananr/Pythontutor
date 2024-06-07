from math import sin, pi

def S(t, n, T):
    # Compute the sine sum approximation
    s = 0
    for i in range(1, n + 1):
        s += 1.0 / (2 * i - 1) * sin(2 * (2 * i - 1) * pi * t / T)
    s *= 4 / pi
    return s

def f(t, T):
    # Define the piecewise constant function
    if 0 < t < T / 2:
        ans = 1
    elif abs(t - T / 2) < 1E-14:
        ans = 0
    elif T / 2 < t < T:
        ans = -1
    else:
        print('Error: t must be between 0 and T')
        ans = None
    return ans

def table(n_values, alpha_values, T):
    # Generate the comparison table
    t_list = [2 * alpha * T for alpha in alpha_values]
    for n in n_values:
        print('n = %d' % n)
        print('  Function t=%.2f*pi t=%.2f*pi t=%.2f*pi' % (0.01, 0.25, 0.49))
        print('%10s %.7f %.7f %.7f' % ('f(t, T)',
                                       f(t_list[0], T),
                                       f(t_list[1], T),
                                       f(t_list[2], T)))
        print('%10s %.7f %.7f %.7f' % ('S(t, n, T)',
                                       S(t_list[0], n, T),
                                       S(t_list[1], n, T),
                                       S(t_list[2], n, T)))
        print('%10s %.7f %.7f %.7f' % ('Error',
                                       abs(S(t_list[0], n, T) - f(t_list[0], T)),
                                       abs(S(t_list[1], n, T) - f(t_list[1], T)),
                                       abs(S(t_list[2], n, T) - f(t_list[2], T))))
        print('')

if __name__ == '__main__':
    # Parameters
    n_list = [1, 3, 5, 10, 30, 100]
    alpha_list = [0.01, 0.25, 0.49]
    T = 2 * pi
    # Generate and display the table
    table(n_list, alpha_list, T)

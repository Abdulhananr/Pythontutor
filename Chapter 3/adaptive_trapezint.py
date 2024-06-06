from scipy.integrate import quad
from numpy import exp, pi, cos, log, sqrt


def second_derivative(func, x, h=1E-6):
    result = (func(x - h) - 2 * func(x) + func(x + h)) / (h ** 2)
    return result


def adaptive_trapezoidal_integration(func, lower_bound, upper_bound, epsilon=1E-4):
    second_derivative_values = []
    for i in range(101):
        second_derivative_values.append(abs(second_derivative(func, lower_bound + i * (upper_bound - lower_bound) / 100)))
    max_second_derivative = max(second_derivative_values)
    step_size = sqrt(12 * epsilon) * 1 / sqrt((upper_bound - lower_bound) * max_second_derivative)
    num_intervals = (upper_bound - lower_bound) / step_size
    integral_sum = (func(lower_bound) + func(upper_bound)) / 2
    for i in range(1, int(num_intervals)):
        integral_sum += func(lower_bound + i * step_size)
    integral_sum *= step_size
    return integral_sum


function_set_1 = [exp, 0, log(3)]
function_set_2 = (cos, 0, pi)

functions = [function_set_1, function_set_2]


def verify_integration(func, lower_bound, upper_bound, num_points):
    exact_value = quad(func, lower_bound, upper_bound)[0]
    approximate_value = adaptive_trapezoidal_integration(func, lower_bound, upper_bound)
    error_value = abs(exact_value - approximate_value)
    print(f'The exact integral of {func.__name__} between {lower_bound:.5f} and {upper_bound:.5f} is {exact_value:.5f}. '
          f'The approximate answer is {approximate_value:.5f} giving an error of {error_value:.5f}')


for function in functions:
    verify_integration(function[0], function[1], function[2], 10)


"""
Converted print statement to Python 3 format.
Changed the variable names:
diff2 to second_derivative
adaptive_trapezint to adaptive_trapezoidal_integration
ddf to second_derivative_values
max_ddf to max_second_derivative
h to step_size
n to num_intervals
s to integral_sum
Replaced from scipy import exp, pi, cos, log, sqrt with from numpy import exp, pi, cos, log, sqrt as scipy has deprecated those direct imports.
Now, the code should work correctly in Python 3 with the updated variable names.

Sample run:
python adaptive_trapezint.py
The exact integral of exp between 0.00000 and 1.09861 is 2.00000. The approximate answer is 1.96771 giving an error of 0.03229
The exact integral of cos between 0.00000 and 3.14159 is 0.00000. The approximate answer is 0.01467 giving an error of 0.01467
"""
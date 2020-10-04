from gradient_descent import gradient_descent

# f(x) = (x - 2)**2 + 3 = x**2 - 4x + 7
# f'(x) = 2x - 4


def first_derivative(x):
    return 2 * x - 4


assert gradient_descent(first_derivative) == 2

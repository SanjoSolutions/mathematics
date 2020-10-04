from gradient_ascent import gradient_ascent

# f(x) = -(x - 2)**2 + 3 = -(x**2 - 4x + 4) + 3 = -x**2 + 4x - 4 + 3 = -x**2 + 4x - 1
# f'(x) = -2x + 4


def first_derivative(x):
    return -2 * x + 4


assert gradient_ascent(first_derivative) == 2

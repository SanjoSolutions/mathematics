from gradient_ascent import gradient_ascent

# f(x) = -(x - 2)**2 + 3 = -(x**2 - 4x + 4) + 3 = -x**2 + 4x - 4 + 3 = -x**2 + 4x - 1
# f'(x) = -2x + 4


def first_derivative(variables):
    return -2 * variables[0]['value'] + 4


variables = (
    {
        'first_derivative': first_derivative
    },
)


result = gradient_ascent(variables)
print('result', result)
assert result[0]['value'] == 2

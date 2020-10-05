from gradient_descent import gradient_descent

# f(x) = (x - 2)**2 + 3 = x**2 - 4x + 7
# f'(x) = 2x - 4


def first_derivative(variables):
    return 2 * variables[0]['value'] - 4


variables = (
    {
        'first_derivative': first_derivative
    },
)

result = gradient_descent(variables)
print('result', result)
assert result[0]['value'] == 2

# f(x) = mx + b

# b = 0
# f(x) = mx

# SUM of distances of points to line

# euclidean distance


import math
from gradient_descent import gradient_descent


def linear_regression(points):
    variables = (
        # m
        {
            'first_derivative': lambda variables: calculate_m_first_derivative_total_distance(variables, points),
            'alpha': 0.01,
            'epsilon': 0.000001,
            'initial_value': 0,
        },
        # b
        {
            'first_derivative': lambda variables: calculate_b_first_derivative_total_distance(variables, points),
            'alpha': 0.01,
            'epsilon': 0.000001,
            'initial_value': 0,
        }
    )
    return gradient_descent(
        variables,
        # max_steps=1000000,
        after_step=lambda variables: print('total distance', calculate_total_distance(variables, points))
    )


def calculate_total_distance(variables, points):
    total_distance = 0
    for point in points:
        total_distance += calculate_distance(variables, point)
    return total_distance


def calculate_distance(variables, point):
    m = variables[0]['value']
    b = variables[1]['value']
    x = point[0]
    y = point[1]
    h = m * x + b
    return (h - y) ** 2


def calculate_m_first_derivative_distance(variables, point):
    m = variables[0]['value']
    b = variables[1]['value']
    x = point[0]
    y = point[1]
    return 2 * x * (b + m * x - y)


def calculate_m_first_derivative_total_distance(variables, points):
    first_derivative_total_distance = 0
    for point in points:
        first_derivative_distance = calculate_m_first_derivative_distance(variables, point)
        first_derivative_total_distance += first_derivative_distance
    return first_derivative_total_distance / (2 * len(points))


def calculate_b_first_derivative_distance(variables, point):
    m = variables[0]['value']
    b = variables[1]['value']
    x = point[0]
    y = point[1]
    return 2 * (b + m * x - y)


def calculate_b_first_derivative_total_distance(variables, points):
    first_derivative_total_distance = 0
    for point in points:
        first_derivative_distance = calculate_b_first_derivative_distance(variables, point)
        first_derivative_total_distance += first_derivative_distance
    return first_derivative_total_distance / (2 * len(points))

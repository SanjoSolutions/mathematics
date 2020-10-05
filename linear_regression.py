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
            'alpha': 0.00001,
            'initial_value': 1,
        },
        # b
        {
            'first_derivative': lambda variables: calculate_b_first_derivative_total_distance(variables, points),
            'alpha': 0.00001,
            'initial_value': 0,
        }
    )
    return gradient_descent(
        variables,
        max_steps=1000000,
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
    c = point[0]
    d = point[1]
    # f(x) = mx + b
    if m == 0:
        distance_to_point = abs(d - b)
    else:
        # c = point_x
        # d = point_y
        # f2(x) = -1 / m * (x - c) + d

        # f = f2
        # <=> mx + b = -1 / m * (x - c) + d
        # <=> x = (-b m + c + d m)/(m^2 + 1) and m^2 + 1!=0 and m!=0
        # <=> x == (-b m + c + d m)/(1 + m^2) && 1 + m^2 != 0 && m != 0
        point_on_line_x = (-b * m + c + d * m) / (m ** 2 + 1)
        point_on_line_y = m * point_on_line_x + b  # f(x) = mx + b
        distance_to_point = math.sqrt((c - point_on_line_x) ** 2 + (d - point_on_line_y) ** 2)
    return distance_to_point


def calculate_m_first_derivative_distance(variables, point):
    m = variables[0]['value']
    b = variables[1]['value']
    c = point[0]
    d = point[1]
    # point_on_line_x = (-b * m + c + d * m) / (m ** 2 + 1)
    # point_on_line_y = m * point_on_line_x + b
    # distance_to_point = sqrt((c - (-b * m + c + d * m) / (m ** 2 + 1)) ** 2 + (d - m * (-b * m + c + d * m) / (m ** 2 + 1) + b) ** 2)
    denominator = (2 * math.sqrt(((b + d) ** 2 - 2 * c * (b + d) * m + (4 * b ** 2 + c ** 2) * m ** 2) / (1 + m ** 2)))
    if denominator == 0:
        return 0
    else:
        numerator = ((-2 * c * (b + d) + 2 * (4 * b ** 2 + c ** 2) * m) / (1 + m ** 2) - (2 * m * ((b + d) ** 2 - 2 * c * (b + d) * m + (4 * b ** 2 + c ** 2) * m ** 2)) / (1 + m ** 2) ** 2)
        return numerator / denominator


def calculate_m_first_derivative_total_distance(variables, points):
    first_derivative_total_distance = 0
    for point in points:
        first_derivative_distance = calculate_m_first_derivative_distance(variables, point)
        first_derivative_total_distance += first_derivative_distance
    return first_derivative_total_distance


def calculate_b_first_derivative_distance(variables, point):
    m = variables[0]['value']
    b = variables[1]['value']
    c = point[0]
    d = point[1]
    denominator = (2 * (1 + m ** 2) * math.sqrt(((b + d) ** 2 - 2 * c * (b + d) * m + (4 * b ** 2 + c ** 2) * m ** 2) / (1 + m ** 2)))
    if denominator == 0:
        return 0
    else:
        numerator = (2 * (b + d) - 2 * c * m + 8 * b * m ** 2)
        return numerator / denominator


def calculate_b_first_derivative_total_distance(variables, points):
    first_derivative_total_distance = 0
    for point in points:
        first_derivative_distance = calculate_b_first_derivative_distance(variables, point)
        first_derivative_total_distance += first_derivative_distance
    return first_derivative_total_distance

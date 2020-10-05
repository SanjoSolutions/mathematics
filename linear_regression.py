# f(x) = mx + b

# b = 0
# f(x) = mx

# SUM of distances of points to line

# euclidean distance


import math
from gradient_descent import gradient_descent


def linear_regression(points):
    variables = (
        {
            'first_derivative': lambda variables: calculate_first_derivative_total_distance(variables, points),
            'alpha': 0.00001,
            'initial_value': 1,
        },
    )
    return gradient_descent(
        variables,
        max_steps=132857,
        after_step=lambda variables: print('total distance', calculate_total_distance(variables, points))
    )


def calculate_total_distance(variables, points):
    slope = variables[0]['value']
    total_distance = 0
    for point in points:
        total_distance += calculate_distance(slope, point)
    return total_distance


def calculate_distance(slope, point):
    point_x = point[0]
    point_y = point[1]
    # f(x) = mx
    if slope == 0:
        distance_to_point = abs(point_y)
    else:
        # a = point_x
        # b = point_y
        # f2(x) = -1 / m * (x - a) + b

        # f = f2
        # <=> mx = -1 / m * (x - a) + b
        # <=> x = (a + b m)/(m^2 + 1) and m^2 + 1!=0 and m!=0
        # <=> x == (a + b m)/(1 + m^2) && 1 + m^2 != 0 && m != 0
        point_on_line_x = (point_x + point_y * slope) / (slope ** 2 + 1)
        point_on_line_y = slope * point_on_line_x  # f(x) = mx
        distance_to_point = math.sqrt((point_x - point_on_line_x) ** 2 + (point_y - point_on_line_y) ** 2)
    return distance_to_point
    # point_on_line_x = (1 / m * a + b) / (m + 1 / m)
    # point_on_line_y = m * (1 / m * a + b) / (m + 1 / m)
    # a = point_x
    # b = point_y
    # sqrt((a - (1 / m * a + b) / (m + 1 / m)) ** 2 + (b - m * (1 / m * a + b) / (m + 1 / m)) ** 2)
    # <=> sqrt((b - a m)^2/(1 + m^2))
    # f'(x) = -((a + b m) sgn(b - a m))/(m^2 + 1)^(3/2)


def calculate_first_derivative_distance(slope, point):
    point_x = point[0]
    point_y = point[1]
    a = point_x
    b = point_y
    m = slope
    # point_on_line_x = (a + b * m) / (m ** 2 + 1)
    # point_on_line_y = m * (a + b * m) / (m ** 2 + 1)
    # distance_to_point = sqrt((a - (a + b * m) / (m ** 2 + 1)) ** 2 + (b - m * (a + b * m) / (m ** 2 + 1)) ** 2)
    # Factor[Sqrt[(a - (a + b m)/(1 + m^2))^2 + (b - (m (a + b m))/(1 + m^2))^2]] = Sqrt[(b - a m)^2/(1 + m^2)]
    # d/dm(distance_to_point) = (-(2 m (b - a m)^2)/(1 + m^2)^2 - (2 a (b - a m))/(1 + m^2))/(2 sqrt((b - a m)^2/(1 + m^2)))
    denominator = (2 * math.sqrt((b - a * m) ** 2 / (1 + m ** 2)))
    if denominator == 0:
        return 0
    else:
        numerator = (-(2 * m * (b - a * m) ** 2) / (1 + m ** 2) ** 2 - (2 * a * (b - a * m)) / (1 + m ** 2))
        return numerator / denominator


def calculate_first_derivative_total_distance(variables, points):
    slope = variables[0]['value']
    first_derivative_total_distance = 0
    for point in points:
        first_derivative_distance = calculate_first_derivative_distance(slope, point)
        first_derivative_total_distance += first_derivative_distance
    return first_derivative_total_distance

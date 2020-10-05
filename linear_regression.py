# f(x) = mx + b

# b = 0
# f(x) = mx

# SUM of distances of points to line

# euclidean distance


from gradient_descent import gradient_descent


def linear_regression(points):
    variables = (
        # b
        {
            'alpha': 0.01,
            'epsilon': 0.000001,
            'initial_value': 0,
        },
        # m
        {
            'alpha': 0.01,
            'epsilon': 0.000001,
            'initial_value': 0,
        }
    )

    def calculate_slopes(variables):
        return calculate_first_derivative_total_distance(variables, points)

    return gradient_descent(
        variables,
        calculate_slopes,
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


def calculate_first_derivative_total_distance(variables, points):
    first_derivative_total_distance = [0] * len(variables)
    for point in points:
        first_derivative_of_b_distance = calculate_b_first_derivative_distance(variables, point)
        first_derivative_total_distance[0] += first_derivative_of_b_distance
        first_derivative_total_distance[1] += calculate_m_first_derivative_distance(
            first_derivative_of_b_distance,
            point
        )
    return tuple(
        _first_derivative_total_distance / (2 * len(points))
        for _first_derivative_total_distance in first_derivative_total_distance
    )


def calculate_m_first_derivative_distance(first_derivative_of_b_distance, point):
    x = point[0]
    return first_derivative_of_b_distance * x


def calculate_b_first_derivative_distance(variables, point):
    b = variables[0]['value']
    m = variables[1]['value']
    x = point[0]
    y = point[1]
    return 2 * (b + m * x - y)

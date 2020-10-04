def gradient_walk(first_derivative, update_x):
    alpha = 0.5
    x = 0
    slope = first_derivative(x)
    while slope != 0:
        x = update_x(x, alpha, slope)
        slope = first_derivative(x)
    return x

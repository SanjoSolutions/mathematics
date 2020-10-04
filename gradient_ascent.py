from gradient_walk import gradient_walk


def gradient_ascent(first_derivative):
    return gradient_walk(first_derivative, update_x)


def update_x(x, alpha, slope):
    return x + alpha * slope

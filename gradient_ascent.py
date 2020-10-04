from gradient_walk import gradient_walk
from no_op import no_op


def gradient_ascent(first_derivative, alpha=0.5, initial_value=0, after_step=no_op):
    return gradient_walk(first_derivative, update_x, alpha, initial_value, after_step)


def update_x(x, alpha, slope):
    return x + alpha * slope

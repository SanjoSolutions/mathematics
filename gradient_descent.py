from gradient_walk import gradient_walk
from no_op import no_op


def gradient_descent(first_derivative, alpha=0.5, initial_value=0, max_steps=None, after_step=no_op):
    return gradient_walk(first_derivative, update_x, alpha, initial_value, max_steps, after_step)


def update_x(x, alpha, slope):
    return x - alpha * slope

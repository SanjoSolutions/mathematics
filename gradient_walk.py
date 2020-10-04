from no_op import no_op


def gradient_walk(first_derivative, update_x, alpha=0.5, initial_value=0, after_step=no_op):
    x = initial_value
    after_step(x)
    slope = first_derivative(x)
    print('slope', slope)
    print('x', x)

    epsilon = 0.01
    while abs(slope) > epsilon:
        x = update_x(x, alpha, slope)
        after_step(x)
        slope = first_derivative(x)
        print('slope', slope)
        print('x', x)
    return x

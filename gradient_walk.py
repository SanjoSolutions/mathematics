from no_op import no_op


def gradient_walk(first_derivative, update_x, alpha=0.5, epsilon=0.01, initial_value=0, max_steps=None, after_step=no_op):
    x = initial_value
    slope = first_derivative(x)
    step = 1
    after_step(x)
    print('step ' + str(step) + ':')
    print('  slope', slope)
    print('  x', x)

    while (max_steps is None or step < max_steps) and abs(slope) > epsilon:
        x = update_x(x, alpha, slope)
        slope = first_derivative(x)
        step += 1
        after_step(x)
        print('step ' + str(step) + ':')
        print('  slope', slope)
        print('  x', x)

    return x

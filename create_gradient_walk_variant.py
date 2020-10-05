from gradient_walk import gradient_walk


def create_gradient_walk_variant(update):
    def gradient_walk_variant(variables, calculate_slopes, max_steps=None, after_step=None):
        variables = tuple(variable.copy() for variable in variables)
        for variable in variables:
            variable['update'] = update

        return gradient_walk(variables, calculate_slopes, max_steps, after_step)

    return gradient_walk_variant

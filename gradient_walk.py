# variables: tuple of dictionaries with items:
#   update, alpha, epsilon, initial_value
def gradient_walk(variables, calculate_slopes, max_steps=None, after_step=None):
    variables = tuple(variable.copy() for variable in variables)

    # Set defaults
    for variable in variables:
        if 'alpha' not in variable:
            variable['alpha'] = 0.5
        if 'epsilon' not in variable:
            variable['epsilon'] = 0.01
        if 'initial_value' not in variable:
            variable['initial_value'] = 0

    # Initialize values
    for variable in variables:
        variable['value'] = variable['initial_value']

    slopes = calculate_slopes(variables)
    for index in range(len(variables)):
        variables[index]['slope'] = slopes[index]

    step = 1
    if after_step is not None:
        after_step(tuple(variable.copy() for variable in variables))

    while (max_steps is None or step < max_steps) and are_any_variable_slopes_above_epsilon(variables):
        for variable in variables:
            variable['value'] = variable['update'](variable['value'], variable['alpha'], variable['slope'])

        slopes = calculate_slopes(variables)
        for index in range(len(variables)):
            variables[index]['slope'] = slopes[index]

        step += 1
        if after_step is not None:
            after_step(tuple(variable.copy() for variable in variables))

    return variables


def are_any_variable_slopes_above_epsilon(variables):
    return any(abs(variable['slope']) > variable['epsilon'] for variable in variables)

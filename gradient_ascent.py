from create_gradient_walk_variant import create_gradient_walk_variant


def update(x, alpha, slope):
    return x + alpha * slope


gradient_ascent = create_gradient_walk_variant(update)

from linear_regression import linear_regression, calculate_total_distance

points = (
    (1, 1),
    (2, 2),
    (3, 4)
)
# points = (
#     (1, 1),
# )

print('total distance for m = 1', calculate_total_distance(1, points))
print('total distance for m = 4 / 3', calculate_total_distance(4 / 3, points))

slope = linear_regression(points)
print('slope result', slope)

assert slope == 1

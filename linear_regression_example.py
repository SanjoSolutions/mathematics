from linear_regression import linear_regression, calculate_total_distance

points = (
    (1, 1),
    (2, 2),
    (3, 4)
)
# points = (
#     (1, 1),
# )

print('total distance for m = 1', calculate_total_distance(({'value': 1},), points))
print('total distance for m = 4 / 3', calculate_total_distance(({'value': 4 / 3},), points))

result = linear_regression(points)
print('result', result)
slope = result[0]['value']
print('slope result', slope)

assert abs(slope - 1.33) < 0.01

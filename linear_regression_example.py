from linear_regression import linear_regression, calculate_total_distance

# points = (
#     (1, 2),
# )
points = (
    (1, 2),
    (2, 2),
)

result = linear_regression(points)
print('result', result)
b = result[0]['value']
m = result[1]['value']
print('b result', b)
print('m result', m)

assert abs(m - 0) < 0.01
assert abs(b - 2) < 0.01

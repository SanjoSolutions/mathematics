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
m = result[0]['value']
b = result[1]['value']
print('slope result', m)
print('b result', b)

assert m == 0
assert b == 2

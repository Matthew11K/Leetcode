from collections import defaultdict
def is_reflected(points):
    point_count = defaultdict(int)
    left_point = 10000000000
    right_point = -1000000000

    for point in points:
        point_count[tuple(point)] += 1
        left_point = min(left_point, point[0])
        right_point = max(right_point, point[0])
    candidate_line = (left_point + right_point) / 2
    for point in points:
        reflected_point = (2*candidate_line - point[0], point[1])
        if point_count[reflected_point] != point_count[tuple(point)]:
            return False
    return True
points = [[1,1],[-1,-1]]

print(is_reflected(points))
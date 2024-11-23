import math

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def closest_pair(points_x, points_y):
    n = len(points_x)
    if n <= 3:
        return min(distance(points_x[i], points_x[j])
                   for i in range(n) for j in range(i + 1, n))

    mid = n // 2
    mid_x = points_x[mid][0]
    left_points = points_x[:mid]
    right_points = points_x[mid:]

    left_sorted_by_y = [p for p in points_y if p[0] <= mid_x]
    right_sorted_by_y = [p for p in points_y if p[0] > mid_x]

    min_dist = min(closest_pair(left_points, left_sorted_by_y),
                   closest_pair(right_points, right_sorted_by_y))

    strip = [p for p in points_y if abs(p[0] - mid_x) < min_dist]

    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            min_dist = min(min_dist, distance(strip[i], strip[j]))

    return min_dist


def find_closest_pair(points):
    points_x = sorted(points, key=lambda x: x[0])
    points_y = sorted(points, key=lambda y: y[1])
    return closest_pair(points_x, points_y)


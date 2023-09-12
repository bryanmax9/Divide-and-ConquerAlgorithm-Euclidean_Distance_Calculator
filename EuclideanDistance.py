import math
import ast

def parse_input(s):
    # Convert the string to a valid Python list of tuples using ast.literal_eval
    return ast.literal_eval(s.replace("{", "[").replace("}", "]"))

def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair(points_sorted_by_x, points_sorted_by_y):
    num_points = len(points_sorted_by_x)
    if num_points <= 3:
        return min(euclidean_dist(points_sorted_by_x[i], points_sorted_by_x[j])
                   for i in range(num_points) for j in range(i+1, num_points))
    middle = num_points // 2
    midpoint = points_sorted_by_x[middle]

    left_by_y = [point for point in points_sorted_by_y if point[0] <= midpoint[0]]
    right_by_y = [point for point in points_sorted_by_y if point[0] > midpoint[0]]

    closest_left = closest_pair(points_sorted_by_x[:middle], left_by_y)
    closest_right = closest_pair(points_sorted_by_x[middle:], right_by_y)
    closest_pair_dist = min(closest_left, closest_right)

    # Consider the vertical strip that is centered at midpoint.x with a width of 2*closest_pair_dist
    strip = [point for point in points_sorted_by_y if midpoint[0] - closest_pair_dist <= point[0] <= midpoint[0] + closest_pair_dist]

    # In this strip, a point only needs to be checked against its following 6 points to find the closest pair
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if strip[j][1] - strip[i][1] > closest_pair_dist:
                break
            closest_pair_dist = min(closest_pair_dist, euclidean_dist(strip[i], strip[j]))

    return closest_pair_dist

def closest_distance(points):
    points_sorted_by_x = sorted(points, key=lambda p: p[0])
    points_sorted_by_y = sorted(points, key=lambda p: p[1])
    return round(closest_pair(points_sorted_by_x, points_sorted_by_y), 3)

# Test
with open("10-3.txt", "r") as file:
    input_str = file.read()

points = parse_input(input_str)
print(closest_distance(points))
print("Finished!")

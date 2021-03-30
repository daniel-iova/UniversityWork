import math

# -------------------- EVERYTHING ABOUT READING DATA STARTS HERE ---------------------

def read_single_polygon() -> list:
    polygon = []
    number_of_points = int(input("Input number of points: "))
    for i in range(number_of_points):
        x, y = input(f"Give coordinates \"x y\" for point[{i}]:").split(" ")
        x = float(x)
        y = float(y)
        polygon.append([x, y])
    return polygon

# -------------------- EVERYTHING ABOUT READING DATA ENDS HERE -----------------------



# ------------------ EVERYTHING ABOUT OUTPUTTING DATA STARTS HERE --------------------

def print_polygon(polygon):
    i = 0
    for point in polygon:
        print(f"Point[{i}]\'s coordinates: {point[0]} {point[1]}")
        i += 1

# -------------------- EVERYTHING ABOUT OUTPUTTING DATA ENDS HERE --------------------



# -------------------- EVERYTHING ABOUT THE CONVEX HULL STARTS HERE ------------------

def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

def get_leftmost_point(polygon):
    left = 0
    for i in range(1, len(polygon)):
        if (polygon[i][0] < polygon[left][0]):
            left = i
    return left

def convex_hull(polygon):
    if (len(polygon) < 3):
        return []
    hull = []
    l = get_leftmost_point(polygon)
    p = l
    while(True):
        hull.append(polygon[p])
        q = (p+1)%len(polygon)
        for i in range(len(polygon)):
            if orientation(polygon[p], polygon[i], polygon[q]) < 0:
                q = i
        p = q
        if p == l:
            break
    return hull

def concatenate_two_polygons(polygon_1, polygon_2):
    point_reunion = polygon_1 + polygon_2
    return convex_hull(point_reunion)

# -------------------- EVERYTHING ABOUT THE CONVEX HULL ENDS HERE --------------------

# -------------------- EVERYTHING ABOUT POLYGON INFO STARTS HERE  --------------------

def polygon_area(polygon):
    area = 0.0
    for i in range(len(polygon)):
        j = (i + 1) % len(polygon)
        area += polygon[i][0] * polygon[j][1] - polygon[j][0] * polygon[i][1]
    area = math.fabs(area) / 2.0
    return area

def point_distance(point_1, point_2):
        return math.sqrt((point_2[0]-point_1[0])**2+(point_2[1]-point_1[1])**2)

def polygon_perimeter(polygon):
    perimeter = 0
    for i in range(len(polygon)):
        j = (i+1) % len(polygon)
        perimeter += point_distance(polygon[i], polygon[j])
    return perimeter

def polygon_gravity_center(polygon):
    c_x = 0
    c_y = 0
    if polygon_area(polygon) == 0:
        return []
    else:
        multiplier = 1/(6*polygon_area(polygon))
        for i in range(len(polygon)-1):
            j = i + 1
            shoelace = polygon[i][0] * polygon[j][1] - polygon[j][0] * polygon[i][1]
            c_x += (polygon[i][0] + polygon[j][0]) * shoelace
            c_y += (polygon[i][1] + polygon[j][1]) * shoelace
        return [round(c_x*multiplier, 3), round(c_y*multiplier, 3)]


def is_convex(polygon):
    initial_orientation = orientation(polygon[0], polygon[1], polygon[2])
    multiplier = 0
    if initial_orientation >= 0:
        multiplier = 1
    else:
        multiplier = -1
    for i in range(len(polygon)):
        p = polygon[i % len(polygon)]
        q = polygon[(i + 1) % len(polygon)]
        r = polygon[(i + 2) % len(polygon)]
        if multiplier*orientation(p, q, r) < 0:
            return False
    return True




def compare_polygons_by_area(polygon_1, polygon_2) -> bool:
    return polygon_area(polygon_1) > polygon_area(polygon_2)

# -------------------- EVERYTHING ABOUT POLYGON INFO ENDS HERE -----------------------

# -------------------- EVERYTHING ABOUT MINIMUM BOUNDING BOX STARTS HERE -------------

def minimum_area_rectangle(polygon):
    left_bottom = [min(point[0] for point in polygon), min(point[1] for point in polygon)]
    right_top = [max(point[0] for point in polygon), max(point[1] for point in polygon)]

    return [[left_bottom[0], right_top[1]], 
            [right_top[0], right_top[1]],
            [right_top[0], left_bottom[1]],
            [left_bottom[0], left_bottom[1]]
            ]
    
# -------------------- EVERYTHING ABOUT MINIMUM BOUNDING BOX ENDS HERE  --------------
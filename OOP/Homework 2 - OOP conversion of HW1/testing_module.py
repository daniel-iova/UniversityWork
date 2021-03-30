from polygon import polygon

def test_read():
    polygon_object = polygon([])
    polygon_object.read()
    if polygon_object.point_number == 0:
        while (polygon_object.point_number == 0):
            print("Invalid Input...try again")
            polygon_object.read_single_polygon()
    return polygon_object

def test_print(polygon_object):
    if polygon_object.point_number == 0:
        print("Invalid polygon")
    else:
        polygon_object.print_polygon()

def test_min_rect_area(polygon_object):
    if polygon_object.point_number < 2:
        print("Bounding box cannot be calculated")
    else:
        print("The bounding box is as follows:")
        test_print(polygon_object.minimum_area_rectangle())

def test_area(polygon_object):
    if polygon_object.point_number < 3:
        print("Area cannot be calculated")
    else:
        print(f"The polygon has an area of: {polygon_object.polygon_area()}")

def test_perimeter(polygon_object):
    if polygon_object.point_number < 2:
        print("Perimeter cannot be calculated")
    else:
        print(f"The polygon has a perimeter of: {polygon_object.polygon_perimeter()}")

def test_gravity_center(polygon_object):
    if polygon_object.point_number < 2:
        print("Centroid cannot be calculated")
    else:
        centroid = polygon_object.polygon_gravity_center()
        if centroid == []:
            print("Centroid cannot be calculated")
        else:
            print(f"The polygon has a centroid of coordinates: {polygon_object.polygon_gravity_center()}")

def test_convexity(polygon_object):
    if (polygon_object.point_number < 3):
        print("Cannot check convexity")
    else:
        if polygon_object.is_convex():
            print("The polygon is convex")
        else:
            print("The polygon is concave")

def test_area_comparison(polygon_object):
    print("Please input 2nd polygon:")
    polygon_2 = polygon([])
    polygon_2 = test_read()
    if polygon_object.compare_polygons_by_area(polygon_2):
        print("The first polygon has a greater area")
    else:
        print("The second polygon has a greater area")

def test_polygon_concatenation(polygon_object):
    print("Please input 2nd polygon:")
    polygon_2 = polygon([])
    polygon_2 = test_read()
    hull = polygon_object.concatenate_two_polygons(polygon_2)
    if hull.point_number == 0:
        print("Concatenation could not be executed.")
    else:
        print("The concatenation is : ")
        test_print(hull)
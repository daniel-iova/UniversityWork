import polygon_functions as pf

def test_read():
    polygon = pf.read_single_polygon()
    if len(polygon) == 0:
        while (len(polygon) == 0):
            print("Invalid Input...try again")
            polygon = pf.read_single_polygon()
    return polygon

def test_print(polygon):
    if len(polygon) == 0:
        print("Invalid polygon")
    else:
        pf.print_polygon(polygon)

def test_min_rect_area(polygon):
    if len(polygon) < 2:
        print("Bounding box cannot be calculated")
    else:
        print("The bounding box is as follows:")
        test_print(pf.minimum_area_rectangle(polygon))

def test_area(polygon):
    if len(polygon) < 3:
        print("Area cannot be calculated")
    else:
        print(f"The polygon has an area of: {pf.polygon_area(polygon)}")

def test_perimeter(polygon):
    if len(polygon) < 2:
        print("Perimeter cannot be calculated")
    else:
        print(f"The polygon has a perimeter of: {pf.polygon_perimeter(polygon)}")

def test_gravity_center(polygon):
    if len(polygon) < 2:
        print("Centroid cannot be calculated")
    else:
        centroid = pf.polygon_gravity_center(polygon)
        if centroid == []:
            print("Centroid cannot be calculated")
        else:
            print(f"The polygon has a centroid of coordinates: {pf.polygon_gravity_center(polygon)}")

def test_convexity(polygon):
    if (len(polygon) < 3):
        print("Cannot check convexity")
    else:
        if pf.is_convex(polygon):
            print("The polygon is convex")
        else:
            print("The polygon is concave")

def test_area_comparison(polygon):
    print("Please input 2nd polygon:")
    polygon_2 = test_read()
    if pf.compare_polygons_by_area(polygon, polygon_2):
        print("The first polygon has a greater area")
    else:
        print("The second polygon has a greater area")

def test_polygon_concatenation(polygon_1):
    print("Please input 2nd polygon:")
    polygon_2 = test_read()
    hull = pf.concatenate_two_polygons(polygon_1, polygon_2)
    if hull == []:
        print("Concatenation could not be executed.")
    else:
        test_print(hull)
        
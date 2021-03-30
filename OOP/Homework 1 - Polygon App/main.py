from testing_functions import *
import os

def menu(polygon):
    i = -1
    while i != 0:
        os.system('cls')
        print("1. Read Polygon")
        print("2. Print Polygon")
        print("3. Print minimum area rectangle")
        print("4. Print polygon area")
        print("5. Print polygon perimeter")
        print("6. Print polygon centroid")
        print("7. Determine if the polygon is convex")
        print("8. Compare polygons by area")
        print("9. Concatenate two polygons")
        i = int(input("Input option (0 to exit): "))
        if i == 1:
            os.system('cls')
            print("READING FUNCTION")
            polygon = test_read()
            input("Press Enter to continue...")
            os.system('cls')
        elif i == 2:
            os.system('cls')
            print("PRINTING FUNCTION")
            test_print(polygon)
            input("Press Enter to continue...")
            os.system('cls')
        elif i == 3:
            os.system('cls')
            print("MINIMUM AREA RECTANGLE FUNCTION")
            test_min_rect_area(polygon)
            input("Press Enter to continue...")
            os.system('cls')
        elif i == 4:
            os.system('cls')
            print("AREA FUNCTION")
            test_area(polygon)
            input("Press Enter to continue...")
            os.system('cls')
        elif i == 5:
            os.system('cls')
            print("PERIMETER FUNCTION")
            test_perimeter(polygon)
            input("Press Enter to continue...")
            os.system('cls')
        elif i == 6:
            os.system('cls')
            print("CENTROID FUNCTION")
            test_gravity_center(polygon)
            input("Press Enter to continue...")
            os.system('cls')
        elif i == 7:
            os.system('cls')
            print("CONVEXITY CHECK FUNCTION")
            test_convexity(polygon)
            input("Press Enter to continue...")
            os.system('cls')
        elif i == 8:
            os.system('cls')
            print("AREA COMPARISON FUNCTION")
            test_area_comparison(polygon)
            input("Press Enter to continue...")
            os.system('cls')
        elif i == 9:
            os.system('cls')
            print("POLYGON CONCATENATION FUNCTION")
            test_polygon_concatenation(polygon)
            input("Press Enter to continue...")
            os.system('cls')

if __name__ == "__main__":

    menu([])
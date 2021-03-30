import math
class polygon():
	
	def __init__(self, point_list):
		self.point_list = point_list
		self.point_number = len(point_list)

	def read(self):
		self.point_number = int(input("Input number of points: "))
		for i in range(self.point_number):
			x, y = input(f"Give coordinates \"x y\" for point[{i}]:").split(" ")
			x = float(x)
			y = float(y)
			self.point_list.append([x, y])

	def print_polygon(self):
		i = 0
		for point in self.point_list:
			print(f"Point[{i}]\'s coordinates: {point[0]} {point[1]}")
			i += 1
	
	def minimum_area_rectangle(self):
		left_bottom = [min(point[0] for point in self.point_list), min(point[1] for point in self.point_list)]
		right_top = [max(point[0] for point in self.point_list), max(point[1] for point in self.point_list)]

		return polygon([
				[left_bottom[0], right_top[1]], 
				[right_top[0], right_top[1]],
				[right_top[0], left_bottom[1]],
				[left_bottom[0], left_bottom[1]]
				])

	def orientation(self, p, q, r):
			return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
		
	def get_leftmost_point(self, point_list):
		left = 0
		for i in range(1, len(point_list)):
			if (point_list[i][0] < point_list[left][0]):
				left = i
		return left

	def convex_hull(self):
		if (self.point_number < 3):
			return polygon()
		hull = []
		l = self.get_leftmost_point(self.point_list)
		p = l
		while(True):
			hull.append(self.point_list[p])
			q = (p+1)%self.point_number
			for i in range(self.point_number):
				if self.orientation(self.point_list[p], self.point_list[i], self.point_list[q]) < 0:
					q = i
			p = q
			if p == l:
				break
		return polygon(hull)
	
	def concatenate_two_polygons(self, polygon_2):
		point_reunion = polygon(self.point_list + polygon_2.point_list)
		return point_reunion.convex_hull()
	
	def polygon_area(self):
		area = 0.0
		for i in range(self.point_number):
			j = (i + 1) % self.point_number
			area += self.point_list[i][0] * self.point_list[j][1] - self.point_list[j][0] * self.point_list[i][1]
		area = math.fabs(area) / 2.0
		return area

	def point_distance(self, point_1, point_2):
			return math.sqrt((point_2[0]-point_1[0])**2+(point_2[1]-point_1[1])**2)

	def polygon_perimeter(self):
		perimeter = 0
		for i in range(self.point_number):
			j = (i+1) % self.point_number
			perimeter += self.point_distance(self.point_list[i], self.point_list[j])
		return perimeter

	def polygon_gravity_center(self):
		c_x = 0
		c_y = 0
		if self.polygon_area() == 0:
			return []
		else:
			multiplier = 1/(6*self.polygon_area())
			for i in range(self.point_number-1):
				j = i + 1
				shoelace = self.point_list[i][0] * self.point_list[j][1] - self.point_list[j][0] * self.point_list[i][1]
				c_x += (self.point_list[i][0] + self.point_list[j][0]) * shoelace
				c_y += (self.point_list[i][1] + self.point_list[j][1]) * shoelace
			return [round(c_x*multiplier, 3), round(c_y*multiplier, 3)]

	def is_convex(self):
		initial_orientation = self.orientation(self.point_list[0], self.point_list[1], self.point_list[2])
		multiplier = 0
		if initial_orientation >= 0:
			multiplier = 1
		else:
			multiplier = -1
		for i in range(self.point_number):
			p = self.point_list[i % self.point_number]
			q = self.point_list[(i + 1) % self.point_number]
			r = self.point_list[(i + 2) % self.point_number]
			if multiplier*self.orientation(p, q, r) < 0:
				return False
		return True
	
	def compare_polygons_by_area(self, polygon_2):
		return self.polygon_area() > polygon_2.polygon_area()

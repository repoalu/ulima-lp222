from p11 import Point

class Polygon:
    def __init__(self):
        self.__points = []
    
    def add_point(self, point):
        self.__points.append(point)

    def get_perimeter(self):
        points = self.__points
        sum = 0
        for i in range(len(self.__points)):
            p1 = points[i]
            p2 = points[(i + 1) % len(points)]
            sum += Point.get_distance(p1, p2)
        return sum

if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    p3 = Point(3, 0)
    
    pol = Polygon()
    pol.add_point(p1)
    pol.add_point(p2)
    pol.add_point(p3)
    print(pol.get_perimeter())
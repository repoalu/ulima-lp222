class Point():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def is_origin(self):
        return self.__x == 0 and self.__y == 0
    
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def get_distance(p1, p2):
        return ((p2.get_y() - p1.get_y()) ** 2 + (p2.get_x() - p1.get_x()) ** 2) ** 0.5

if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    print(Point.get_distance(p1, p2))
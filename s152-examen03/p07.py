class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
    
    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

    def get_area(self):
        return self.__width * self.__height
    
    def is_square(self):
        return self.__width == self.__height
    
    def compare(self, rectangle2):        
        area1 = rectangle2.get_area()
        area2 = self.get_area()
        if area1 > area2:
            return 1
        elif area1 < area2:
            return 2
        else:
            return 3
    
    def __str__(self):
        return f"Rectangulo de lados {self.__height} y {self.__width}"

if __name__ == "__main__":
    r1 = Rectangle(4, 5)
    print(r1.get_perimeter(), r1.get_area(), r1.is_square())
    r2 = Rectangle(6, 6)
    print(r2.get_perimeter(), r2.get_area(), r2.is_square())
    print(r1)
    print(r1.compare(r2), r2.compare(r1), r1.compare(r1))

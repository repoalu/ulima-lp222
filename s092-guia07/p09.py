class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side

if __name__ == "__main__":
    r1 = Rectangle(3, 5)
    print(r1.get_area())

    s1 = Square(4)
    print(s1.get_area())

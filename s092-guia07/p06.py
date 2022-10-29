class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        p = self.perimeter() / 2
        area = (p * (p - self.a) * (p - self.b) * (p - self.c) ) ** 0.5
        return area
    
    def triangle_type(self):
        if self.a == self.b == self.c:
            print("Equilatero")
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            print("Isosceles")
        else:
            print("Escaleno")

    def __str__(self):
        ans = "Triangulo"
        ans += f"\nLados: a={self.a}, b={self.b}, c={self.c}"
        return ans

if __name__ == "__main__":
    t1 = Triangle(3, 4, 5)
    t2 = Triangle(5, 5, 5)
    print(t1)
    print(t2)
    print("El perimetro es:", t1.perimeter())
    print("El area es:", t1.area())
    t1.triangle_type()
    t2.triangle_type()
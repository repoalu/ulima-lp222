class Triangle:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__perimeter = self.__a + self.__b + self.__c
        p = self.__perimeter / 2
        self.__area = (p * (p - self.__a) * (p - self.__b) * (p - self.__c) ) ** 0.5 

    def get_perimeter(self):
        return self.__perimeter
    
    def get_area(self):        
        return self.__area
    
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
    t1.perimeter = 1000
    print(t1.get_perimeter())
    print(t1.get_area())
''''
Implemente una clase que represente un numero complejo. Considere las
operaciones:
    - crear
    - imprimir
    - esReal
    - esImaginario
'''
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.__real = real
        self.__imaginary = imaginary
    
    def is_real(self):
        return self.__imaginary == 0

    def is_imaginary(self):
        return self.__real == 0

    def __str__(self):
        return f"{self.__real} + {self.__imaginary}i"

if __name__ == "__main__":
    n1 = ComplexNumber(5, 0)
    n2 = ComplexNumber(4, 3)
    print(n1, n2)
    
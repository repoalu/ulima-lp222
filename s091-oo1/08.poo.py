#Definicion de la clase
class Student:
    #Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #Metodo de instancia    
    def greet(self):
        print(f"Hola. Soy {self.name} y tengo {self.age} anios")
    
    def greet_general():
        print("Hola mundo")

if __name__ == "__main__":
    student1 = Student("Juan Perez", 22)
    student2 = Student("Maria Alvarez", 18)
    student1.greet()
    student2.greet()
    Student.greet_general()

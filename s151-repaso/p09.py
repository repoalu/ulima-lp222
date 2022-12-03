class Person:
    def __init__(self, code, name, address):
        self._code = code
        self._name = name
        self._address = address

class Student(Person):
    def __init__(self, code, name, address, department, period):
        super().__init__(code, name, address)
        self._department = department
        self._period = period
        
    def study(self):
        print(f"{self._name} esta estudiando")

    def take_test(self):
        print(f"{self._name} esta rindiendo un examen")


class Teacher(Person):
    def __init__(self, code, name, address, school, month_salary):
        super().__init__(code, name, address)
        self._school = school
        self._month_salary = month_salary
        
    def teach(self):
        print(f"{self._name} esta dictando clases")
    
    def grade_test(self):
        print(f"{self._name} esta corrigiendo examenes")
                

if __name__ == "__main__":
    s1 = Student(100, "Juan Perez", "Av. Brasil 949", "Computer Science", 4)
    s1.study()
    s1.take_test()

    t1 = Teacher(200, "Ana Valera", "Av. Bolivar 635", "Ingenieria Industrial", 9000)
    t1.teach()
    t1.grade_test()
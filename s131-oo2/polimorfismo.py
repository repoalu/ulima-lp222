class Student:
    def __init__(self, name):
        self.__name = name
    
    def __str__(self):
        return f"Estudiante: {self.__name}"        

class HighSchoolStudent(Student):
    def __init__(self, name, schoolName, grade):
        self.__name = name
        self.__schoolName = schoolName
        self.__grade = grade

    def __str__(self):
        return f"Estudiante: {self.__name}. Colegio: {self.__schoolName}"

class CollegeStudent(Student):
    def __init__(self, name, universityName, period):
        self.__name = name
        self.__universityName =  universityName
        self.__period = period

    def __str__(self):
        return f"Estudiante: {self.__name}. Universidad: {self.__universityName}"

class SelfTaughtStudent(Student):
    def read():
        print("Leyendo material")
    

def show_students(student_list):
    for student in student_list:
        print(student)

if __name__ == "__main__":
    s1 = Student("Juan Perez")
    s2 = HighSchoolStudent("Maria Vargas", "San Agustin", 4)
    s3 = CollegeStudent("Cesar Palacios", "U de Lima", 2)
    s4 = SelfTaughtStudent("Valeria Nogales")
    student_list = [s1, s2, s3, s4]
    show_students(student_list)

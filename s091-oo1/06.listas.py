#No son homogeneas
grades = [1, "dos", 3]
grades = [10, 20, 30, 999]

#No son estaticas
grades.append(4)
print(grades)

grades.extend([5, 6, 7])
print(grades)

#Otros operadores
print(grades * 2)
print(grades + [4, 5, 6])

#Acceso
print(grades[0], grades[1])

#Slicing
print(grades[2:4])
print(grades[:4])
print(grades[3:])

#Modificaciones
print(grades) 
grades.pop()
grades.insert(3, 999)
print(grades)
grades.remove(999)
print(grades)

#Ordenar
grades.sort()
print(grades)

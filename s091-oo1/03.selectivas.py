grade = 18
if grade >= 11:
    print("Alumno aprobado")
    if grade > 15:
        print("Tiene muy buena nota")

'''
[0, 11>: Debajo del promedio
[11, 14>: Rendimiento promedio
[14, 20]: Por encima del promedio
Mayor que 20: fuera de rango
'''
print("Comparacion con la seccion...")

if grade < 11:
    print("Rendimiento debajo del promedio")
elif grade < 14:
    print("Rendimiento dentro del promedio")
elif grade <= 20:
    print("Rendimiento por encima del promedio")
else:
    print("Valor de nota fuera de rango")
    

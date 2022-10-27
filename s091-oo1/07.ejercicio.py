'''
Implemente un programa que reciba dos listas L1 y L2 que representan las notas
de dos secciones diferentes. Su programa debe realizar lo siguiente:

1. Eliminar de L1 y L2 los valores invalidos (menores que cero y mayores que 20)
2. Concatenar los resultados en una nueva lista y retornarla
'''

def merge_filtered(L1, L2):
    ans = []
    for element in L1:
        if 0 <= element <= 20:
            ans.append(element) 
    for element in L2:
         if 0 <= element <= 20:
            ans.append(element) 
    return ans

if __name__ == "__main__":
    L1 = [10, 12, 33, -5, 18, 11]
    L2 = [18, 15, -5, 33, 40, 8]
    print(merge_filtered(L1, L2))
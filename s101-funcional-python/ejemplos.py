#Funciones como variables
def my_function(x, y):
    return x + y

def square(x):
    return x * x

f1 = my_function
f2 = my_function
print(f1(2, 4))
print(f2(10, 20))

#Funciones Lambda
square_lambda = lambda x: x * x
print(square_lambda(7))
print(square(7))

get_perimeter = lambda a, b, c: a + b + c
print(get_perimeter(4, 4, 6))

#Uso de map y filter
def greater_3(x):
    if x > 3:
        return True
    else:
        return False

#Una version mas simple
def greater_3(x):
    return x > 3

list1 = [1, 2, 3, 4, 5]
print("Map - Def:", list(map(square, list1)))
print("Map - Lambda:",list(map(lambda x: 2 * x, list1)))

print("Filter - Def", list(filter(greater_3, list1)))
print("Filter - Lambda:",list(filter(lambda x: x % 2 == 0, list1)))

names = ["Jose Carlos", "Maria Alejandra", "John", "Mariana", "Ana"]
sorted_names = sorted(names, key = len)
print(sorted_names)

sorted_names_desc = sorted(names, key = lambda text: -1 * len(text))
print(sorted_names_desc)

#Recursividad
def get_sum(values):
    if values == []:
        return 0
    else:
        return values[0] + get_sum(values[1:])

print(get_sum([1, 2, 3]))

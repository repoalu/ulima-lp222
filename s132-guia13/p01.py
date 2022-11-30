#Asumimos que las posiciones de los elementos inician en 1
class CustomList:
    def __init__(self):
        self.__elements = []
    
    def add(self, element, position):
        self.__elements.insert(position - 1, element)

    def remove(self, position):
        self.__elements.pop(position - 1)

    def get(self, position):
        return self.__elements[position - 1]

    def count(self):
        return len(self.__elements)

    def __str__(self):
        return str(self.__elements)

if __name__ == "__main__":
    my_list = CustomList()
    my_list.add(12, 1)
    my_list.add(16, 2)
    my_list.add(18, 3)
    my_list.add(25, 2)
    print("Lista:", my_list)
    print("Cantidad de elementos:", my_list.count())
    print("Tercer elemento:", my_list.get(3))
    my_list.remove(3)
    print(my_list)

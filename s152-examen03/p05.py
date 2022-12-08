class Order:
    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.__product_count = 0
        self.__total_cost = 0
    
    def add_product(self, quantity, product_price):
        self.__product_count += quantity
        self.__total_cost += product_price * quantity
    
    def __str__(self):
        return f"Pedido para {self.__customer_name}.\n" +\
               f"Son {self.__product_count} productos.\n" +\
               f"Monto total: {self.__total_cost}"

if __name__ == "__main__":
    order1 = Order("Juan Perez")
    print(order1)
    order1.add_product(3, 5)
    print(order1)
    order1.add_product(5, 3.5)
    print(order1)
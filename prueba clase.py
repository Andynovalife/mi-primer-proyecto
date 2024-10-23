class Restaurant: 

    def __init__(self, nombre, categoria, precio): #se elimina el metodo de abajo
        self.nombre = nombre #atributo
        self.categoria = categoria
        self.__precio = precio 

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')

# GETTERS Y SETTERS - GET = Obtiene un valor, SET = Agrega o modifica un valor

    def get_precio(self): #poner get_atributo
        print(self.__precio)

restaurant = Restaurant('Pizzeria Mexico', 'Comida Italiana', 50) 
restaurant.mostrar_informacion() 
restaurant.get_precio()

restaurant2 = Restaurant('Hamburguesas Python', 'Comida Casual', 20 ) 
restaurant2.mostrar_informacion() 
restaurant2.get_precio()
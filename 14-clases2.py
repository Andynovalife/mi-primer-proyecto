class Restaurant: 
#abstraccion que datos son necesarios en la clase y en los objetos
    def __init__(self, nombre, categoria, precio): #se elimina el metodo de abajo
        self.nombre = nombre #atributo
        self.categoria = categoria
        self.precio = precio

    # def agregar_restaurant(self, nombre):
    #     self.nombre = nombre 

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')

restaurant = Restaurant('Pizzeria Mexico', 'Comida Italiana', 50) 
restaurant.mostrar_informacion() 

restaurant2 = Restaurant('Hamburguesas Python', 'Comida Casual', 20 ) 
restaurant2.mostrar_informacion() 

# un constructor es una funcion que se ejecuta automaticamente al crear un nuevo objeto a traves de una clase

class Restaurant: 
#abstraccion que datos son necesarios en la clase y en los objetos
    def __init__(self, nombre, categoria, precio): #se elimina el metodo de abajo
        self.nombre = nombre #atributo
        self.categoria = categoria
        self.__precio = precio # Default: Public (se puede modificar en cualquier lado del programa), PROTECTED (se debe agregar un guion bajo a la par del atributo, es decir pasa de self.precio a self._precio
# PROTECTED, igual puede ser modificado dentro de la misma clase, pero PRIVATE se logra con doble guion bajo, ctrl D selecciona todo lo que yo selecciono y agrega doble guion bajo a precio

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')

# GETTERS Y SETTERS - GET = Obtiene un valor, SET = Agrega o modifica un valor

    def get_precio(self): #poner get_atributo
        print(self.__precio)

    def set_precio(self, precio):
        self.__precio = precio

restaurant = Restaurant('Pizzeria Mexico', 'Comida Italiana', 50) 

#print(restaurant.__precio) #si le pongo print, imprime el precio y si luego cambio el precio, y pido mostrar todo cambia el 50 por 80
# restaurant.__precio = 80 #se puede encapsular para que esto no pase, no se puede modificar con private __
#private solo se puede modificar con metodos
restaurant.mostrar_informacion() 
restaurant.set_precio(80)
restaurant.get_precio()

restaurant2 = Restaurant('Hamburguesas Python', 'Comida Casual', 20 ) 
#print(restaurant2.__precio)
# restaurant2.__precio = 40
restaurant2.mostrar_informacion() 
restaurant2.set_precio(40)
restaurant2.get_precio()


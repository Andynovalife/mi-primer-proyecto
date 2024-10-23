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


# Crear una clase hijo de restaurant (heredar)
class Hotel(Restaurant):
     def __init__(self, nombre, categoria, precio):
         super().__init__(nombre, categoria, precio) # con super hacemos referencia a la clase padre

hotel = Hotel('Hotel P00', '5 estrellas', 200)
hotel.mostrar_informacion()


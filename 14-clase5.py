class Restaurant: 
#abstraccion que datos son necesarios en la clase y en los objetos
    def __init__(self, nombre, categoria, precio): #se elimina el metodo de abajo
        self.nombre = nombre #atributo
        self.categoria = categoria
        self.precio = precio 

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')

# GETTERS Y SETTERS - GET = Obtiene un valor, SET = Agrega o modifica un valor

    def get_precio(self): #poner get_atributo
        print(self.__precio)

    def set_precio(self, precio):
        self.__precio = precio


# Crear una clase hijo de restaurant (heredar)
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca): #constructor
        super().__init__(nombre, categoria, precio) # con super hacemos referencia a la clase padre
        self.alberca = alberca

#rescribir un metodo (debe llamarse igual)
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, {self.alberca}')

    # agregar un metodo que solo exita en hotel (polimorfismo)
    def get_alberca(self):
        return self.alberca

# polimorfismo, cuando deseo cambiar en el hijo como se muestra alguna informacion, quitar o poner
hotel = Hotel('Hotel P00', '5 estrellas', 200, 'si')
hotel.mostrar_informacion()
alberca = hotel.get_alberca()
print(alberca)

# mismo metodo con diferente informacion (poliformismo), rescribir un metodo

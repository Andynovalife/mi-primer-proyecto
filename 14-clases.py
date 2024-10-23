class Restaurant: # la clase tiene un nombre, que la primera letra debe ser en mayuscula
#self es invisible, se pasa automaticamente cuando uno llama a la funcion, se necesita para que guarde la informacion a la par (atributo)
    def agregar_restaurant(self, nombre): #esto es una funcion que cuanto esta dentro de una clase se le conoce como metodo, y es parecida a clase, y ambas se deben mandar a llamar
        self.nombre = nombre # Atributo

# otro metodo
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')
# Instanciar la clase (llamar la clase)
restaurant = Restaurant() # debe venir en minuscula (objeto) al inicio pq si no interrumpe con la clase
restaurant.agregar_restaurant('Pizzeria Mexico')  #asi se manda a llamar el metodo (objeto.metodo)
restaurant.mostrar_informacion()

restaurant2 = Restaurant() #cada objeto tiene su propia informacion, self es una forma de referirse al objeto que se esta ejecutando
restaurant2.agregar_restaurant('Hamburguesas Python')  
restaurant2.mostrar_informacion()

# la clase da los metodos, y los objetos llaman esos metodos, pero tienen diferente informacion


#Mostrar la informacion
print(f'Nombre Restaurant: {restaurant.nombre}')
print(f'Nombre Restaurant: {restaurant2.nombre}')

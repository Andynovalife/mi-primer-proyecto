lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

print(lenguajes)
# los arrays *list( comienzan en la posicion 0
print(lenguajes[0]) # python

#Ordenar los elementos
lenguajes.sort()
print(lenguajes)

#Acceder a un elemento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

# Modificando valores de un arreglo
lenguajes[2] = 'PHP'
print(lenguajes)

#Agregar elementos a un arreglo (list)
lenguajes.append('Ruby')
print(lenguajes)

# Eliminar de un arreglo (list)
del lenguajes[1]
print(lenguajes)

# eliminar de un list, elimina el ultimo elemento
lenguajes.pop()
print(lenguajes)

# Eliminar con pop una posicion en especifico
lenguajes.pop(0)
print(lenguajes)

# Eliminar por nombre
lenguajes.remove('PHP')
print(lenguajes)



#creando un diccionario simple
cancion = {
    'artista' : 'Metalica', # llave y valor
    'cancion' : 'Enter Sandman',
    'lanzamiento' : '1992',
    'likes' : 3000
}
#acceder a los elementos del diccionario
print(cancion['artista'])
print(cancion['lanzamiento'])

#mezclar con un string
#Si pongo esto va a salir un error, entonces debo hacerlo diferente
#print(f'Estoy escuchando {artista})

artista = cancion['artista'] #pongo la parte de los corchetes y se asigna a una variable
print(f'Estoy escuchando {artista}')

print(cancion)

#agregar nuevos valores
cancion['playlist'] = 'Heavy Metal'
print(cancion)

#reemplazar valor existente (si esta lo cambia, si no esta lo agrega)
cancion['cancion'] = 'Seek & Destroy'
print(cancion)

#Eliminar un valor
del cancion['lanzamiento']
print(cancion)


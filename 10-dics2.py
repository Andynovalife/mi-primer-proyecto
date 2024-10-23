#Iniciar un diccionario vacio, digamos que creamos un videojuego desde 0
jugador = {}
print(jugador)

# se une un jugador
jugador['nombre'] = 'Juan' #cuando el objeto o diccionario esta vacio y deseo agregar valores no va con punto si no con igual
jugador['puntaje'] = 0
print(jugador)

# Incrementando el puntaje
jugador['puntaje'] = 100
print(jugador)

# Incrementando el puntaje
jugador['puntaje'] = 200
print(jugador)

# Acceder a un valor, si no aparece sale none, pero se le puede poner como segundo valor no existente
print(jugador.get('consola', 'No existe ese valor'))

#iterar en el dicionario
for llave, valor in jugador.items():
    print(llave)
    print(valor)

#iterar en el dicionario y si solo quiero uno pongo uno
for llave, valor in jugador.items():
    print(valor)

# eliminar jugador y puntaje
del jugador['puntaje']
del jugador['nombre']
print(jugador)

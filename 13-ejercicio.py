# crear una playlist y luego agregar canciones, cuando creas una aplicacion mas real lo ideal es tener una funcion principal

playlist = {} #Diccionario vacio, lo pongo fuera de la app pq si hago otras apps
playlist['canciones'] = [] # lista vacia de canciones, asi se van a ir agregando a playlist y canciones

#funcion principal, la que mande a llamar a las otras
def app():
    #Agregar playlist
    agregar_playlist = True #mientras ponga un nombre para y si no pongo nada deja de correr, pero hasta que ponga False despues
    while agregar_playlist:
        nombre_playlist = input('Como deseas nombrar el playlist?\r\n')
        if nombre_playlist:
             playlist['nombre'] = nombre_playlist #playlist['nombre'] es una variable
             # ya tenemos un nombre, desactivar el true
             agregar_playlist = False #cuando se pone true y luego false se conoce como banderas

             #Mandar llamar la funcion para agregar canciones
             agregar_canciones() # para continuar el programa se debe mandar a llamar la funcion cuando se termina un programa
    
def agregar_canciones():
    # utilice print para probar el codigo y no seguir avanzando para saber que ya hay partes que sirven, print('Agregar canciones...')
    #Bandera para agregar canciones
    agregar_cancion = True

    while agregar_cancion:
        #preguntar al usuario que cancion desea agregar
        nombre_playlist = playlist['nombre']
        # pregunta es una variable 
        pregunta = f'\r\n Agrega canciones para la playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones \r\n'

        cancion = input(pregunta)
        if cancion == 'X':
            # Dejar de agregar canciones
            agregar_cancion = False # se deja de ejecutar el while

            #mostrar resumen de la playlist
            mostrar_resumen()  # esto es una funcion
        else:
            # Agregar las canciones a la playlist, para agregar canciones a la lista se usa append()
            playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre'] #nombre_playlist es una variable
    print(f'Playlist: {nombre_playlist} \r\n')    
    print('Canciones: \r\n')
    for cancion in playlist['canciones']:
        print(cancion)

app()

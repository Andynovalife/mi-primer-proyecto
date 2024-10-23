def app():

    with open('archivo.txt') as archivo:  # por default se abre en lectura, si fuera escritura porngo w y si no, no pongo nada
            # si pongo as nombre, entonces queda como un alias
        for contenido in archivo:
            print(contenido.rstrip()) # rstrip quita el espacio

app()
def app():
    # Crear el archivo
    archivo = open('archivo.txt', 'w') # w es escritirua y si no existe lo creara
    # los bancos lo hacen para los estados de cuenta

    # Generar numeros en archivo
    for i in range(0, 20): # iterador i para indexar en el rango de 0 a 20
        archivo.write('Esta es la linea ' + str(i)+ "\r\n") # write es el metodo para escribir en un archivo
        # con el + str(i) +  defino que i es un texto
    # cerrar el archivo (cuando abra un archivo cierrerlo, es buena practica), para que el programa no se le quite tanta memoria
    archivo.close()


app()
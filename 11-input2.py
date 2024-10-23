pregunta = 'Agrega un numero y te dir[e si es par o impar \r\n'
pregunta += ' (escribe "cerrar" para salir de la aplicacion) \r\n' #se puede agregar otra variable y concatenar con el simbolo +=, se ponen comillas dobles no sinples dentro del parentesis

preguntar = True

while preguntar: #Todo dentro del iterador debe ir indentado

    numero = input(pregunta) #se va a colocar lo que puse arriba que es pregunta

    if numero == 'cerrar':
        preguntar = False #cuando la condicion ya no es verdadera dejara de preguntar
    else:
        numero = int(numero)

        if numero % 2 == 0: 
             print(f'El numero {numero} es par')
        else:
             print(f'El numero {numero} es impar')

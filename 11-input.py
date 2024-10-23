nombre = input("Cual es tu nombre: \r\n ") #\r\n es un salto de linea

print(f'Hola {nombre}')


# Leer datos que seran numeros
edad = input('Cual es tu edad?')
#convertir edad (string) a int (entero)

edad = int(edad) #si se va a trabajar con numeros hay que convertirlos

if edad >= 18:
    print('Ya puedes votar')

else:
    print('Aun no puedes votar')


# hacer un juego, mezclarlo con operadores

numero = input('Agrega un numero y te dire si es par o no \r\n')

numero = int(numero)

# print( 2 % 2), da el resultado de un residuo, si hay decimales no es par y si no hay si es par

if numero % 2 == 0: # (se puede poner asi con el signo de porcentaje como operador, que es un modulo)
    print(f'El numero {numero} es par')
else:
     print(f'El numero {numero} es impar')


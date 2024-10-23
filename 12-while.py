numero = 0 #si se deja asi sigue corriendo en 0, pq no se agrega incremento

# while numero <= 10:
#     print(numero)
#     numero += 1 #incremento para envitar un loop infinito
# si seleccionas las lineas y luego pones ctrl K y luego ctrl c, pones todas las lineas en texto

# IF DENTRO DEL WHILE, interrumpir el while con if
while numero <= 10:
    if numero == 5:
        break # detiene la ejecucion del codigo, tb le podemos poner print('CINCOOOOOO!!!'), imprime cinco en letra y continua el codigo normal
    else:
        print(numero)
    numero += 1



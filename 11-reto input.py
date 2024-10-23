print('Conteste las respuestas siguientes con si o no:')
pregunta = input("Los caballos pueden nacer con piel celeste?: \r\n ") 
numero = 0
pregunta = str(pregunta)

if pregunta == "no":
    numero += 1
else:
    numero = 0

pregunta = input("Los pulpos se comen?: \r\n ") 

if pregunta == "si":
    numero += 1
else:
    numero = 0

pregunta = input("Tener educacion es importante?: \r\n ") 

if pregunta == "si":
    numero += 1
else:
    numero = 0

print(f'Tu calificacion final es de {numero} puntos')
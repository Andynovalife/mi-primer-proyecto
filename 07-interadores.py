lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

print(lenguajes[0])
print(lenguajes[1])
print(lenguajes[2])
print(lenguajes[3])

#en lugar de ese codigo, se usa un iterador, como esta en singular y plural va ir dando cada uno 
for lenguaje in lenguajes:
    print(lenguaje) #siempre con identacion
    print(f'Estoy aprendiendo {lenguaje}') # recorre cada elemento

print('Texto de muestra') # si no esta indentado, se muestra hasta que deje de correr el iterador for

# For que escriba numeros
for numero in range(0, 10): #range tiene un valor inicial y uno final, recordar que el valor inicial siempre va a ser 0
    print(numero)

for numero in range(0, 20, 3): #range, si le pongo un tercer numero, va a correr de 3 en 3
    print(numero)
    



# Revisar si una condicion es mayor a 
balance = 0
if balance > 0: #siempre que se ponen : en python se debe dejar una indentacion
    print('Puedes pagar')

else:
    print('No tienes saldo') #else siempre corre cuando la condicion de arriba no se cumple

#Likes
likes = 200
if likes == 200: #se usa doble signo de igual para comparar el like de abajo con el de arriba
    print('Excelente, 200 Likes')


#Likes
likes = 200
if likes == 199: #se puede usar != diferente a, >= mayor o igual, <= menor o igual, > mayor, < menor q
    print('Excelente, 200 Likes')

else:
    print('Casi llegas a 200 likes')

#IF con texto
lenguaje = 'PHP'
if not lenguaje == 'Python': # if not es lo mismo que diferente a !=
    print('Excelente decision')

# Evalular un Boolena
usuario_autenticado = True

if usuario_autenticado: # generalmente se pondria if usuario_autenticado == True:, pero como esta usando un Booleano no es necesario agregar el True
    print('Acceso al sistema')
else:
    print('Debes iniciar sesion')

#Evaluar un elemento en una lista
lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript', 'PHP']

if 'PHP' in lenguajes:
    print('PHP Si existe') #esto sirve como por ejemplo cuando alguien compra y quiere ver si hay algo en descuento y si hay que se aplique el descuento

else:
    print('El articulo no se encuentra')

#anidados
usuario_autenticado = False
usuario_admin = False

if usuario_autenticado: 
    if usuario_admin:
        print('Acceso TOTAL')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciar sesion')


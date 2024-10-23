#Ejemplo con elif
ocupacion = 'Estudiante'
numero = 0

if ocupacion == 'jubilado':
    numero += 1
    print(f'Tienes 50% de descuento {numero}')
elif ocupacion == 'Jubilado':
    print('Tienes 75% de descuento') #se pueden agregar multiples elif
elif ocupacion == 'Desempleado':
    print('Tienes un 10% de descuento')
else:
    print('Debes pagar el 100%')
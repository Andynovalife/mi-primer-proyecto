def mensaje():
    print('Bienvenido')

mensaje()

def mensaje(nombre):
    print(f'Bienvenido {nombre}')

mensaje('Juan')

def mensaje(nombre):
    print(f'Bienvenido {nombre}')
    return nombre

reto = mensaje('Juan')
print(reto)


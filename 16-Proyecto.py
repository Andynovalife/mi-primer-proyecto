# importar liberria
import os

CARPETA = 'contactos/' # cuando se pone en mayuscula, es para que otros programadores vean que es una constante y que no hay que modificarla
EXTENSION = '.txt' # Extension de archivos
ORDENES = 'ordenes/'
PLATILLOS = 'platillos/'

class Platillo:
    def __init__(self, nombre, descripcion, precio): # contstructor
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

class Orden:
    def __init__(self, nombre, platillo, bebida, observaciones): # contstructor
        self.nombre = nombre
        self.platillo = platillo
        self.bebida = bebida
        self.observaciones = observaciones


def app():
    # REVISA SI LA CARPETA EXISTE O NO
    crear_directorio()

    # Muestra el menu de opciones

    mostrar_menu()

    # Preguntar al usuario la accion a realizar

    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion: \r\n')
        opcion = int(opcion) # convertimos un string dentro que sea entero

        # Ejecutar las opciones 
        if opcion == 1:
            agregar_platillo() # estas son funciones
            preguntar = False
        elif opcion == 2:
            editar_platillo()
            preguntar = False
        elif opcion == 3: 
            mostrar_platillo()
            preguntar = False
        elif opcion == 4:
            agregar_orden()
            preguntar = False
        elif opcion == 5:
            eliminar_platillo()
            preguntar = False
        else:
            print('Opcion no valida, intente de nuevo')

def mostrar_menu():
    print('Seleccione del Menu lo que desea hacer:')
    print('1) Agregar un nuevo platillo')
    print('2) Edita un platillo')
    print('3) Ver Menu')
    print('4) Agregar una nueva orden')
    print('5) Eliminar platillo')

def agregar_platillo():
    print('Escribe los datos para agregar el nuevo Platillo') #probar cada paso, para saber donde esta el error
    nombre_platillo = input('Nombre del Platillo: \r\n')

    # Revisar si el archivo ya existe antes de crearlo
    existe = existe_platillo(nombre_platillo)

    if not existe:
        with open(PLATILLOS + nombre_platillo + EXTENSION, 'w') as archivo:  #LOS + concatenan, es decir agregar cosas en una misma linea, solo variables
       
       # resto de los campos
            descripcion_platillo = input('Agrega la descripcion del platillo: \r\n')
            precio_platillo = input('Precio del platillo: \r\n')

        # Instanciar la clase
            platillo = Platillo(nombre_platillo, descripcion_platillo, precio_platillo) # contacto es el objeto

        # Escribir en el archivo
            archivo.write('Nombre:' + platillo.nombre  + '\r\n') # como se quiere escribir, se le pone w, que es permiso de escritura, y cuando se poner as archivo, es para que toda lo que se pide, se refiera a archivo
        # se pone objeto. y los valores de la clase, en este caso contacto es el objeto y nombre parte de la clase
            archivo.write('Descripcion:' + platillo.descripcion  + '\r\n')
            archivo.write('Precio:' + platillo.precio  + '\r\n')

        # Mostrar un mensaje de exito
            print('\r\n El platillo fue creado correctamente \r\n')
    else:
        print('Ese platillo ya existe')

    # Reiniciar el app
    app()

def editar_platillo():
    print('Escribe el nombre del platillo que desea editar')
    nombre_anterior = input('Nombre del platillo que desea editar: \r\n')
    # Revisar si el archivo antes de editarlo
    existe = existe_platillo(nombre_anterior) #revisa el return y si es verdadero se devuelve a existe

    if existe:
        with open(PLATILLOS + nombre_anterior + EXTENSION, 'w') as archivo:

            # Resto de campos
            nombre_platillo = input('Agrega el Nuevo Nombre del Platillo: \r\n')
            descripcion_platillo = input('Agrega la Nueva Descripcion: \r\n')
            precio_platillo = input('Agrega el Nuevo Precio: \r\n')

            # instanciar
            platillo = Platillo(nombre_platillo, descripcion_platillo, precio_platillo)

            #Escribir en el archivo
            archivo.write('Nombre:' + platillo.nombre  + '\r\n')
            archivo.write('Descripcion:' + platillo.descripcion  + '\r\n')
            archivo.write('Precio:' + platillo.precio  + '\r\n')

            # Renombrar el archivo  si pongo punto y luego algo, es un metodo
        os.rename(PLATILLOS + nombre_anterior + EXTENSION, PLATILLOS + nombre_platillo + EXTENSION)

            # Mostrar mensaje de exito
        print('\r\n Contacto editado Correctamente \r\n')           

    else:
        print('Ese contacto no existe')

     # Reiniciar la aplicacion

    app()

def mostrar_platillo():
    archivos = os.listdir(PLATILLOS)  #listdir es un metodo que nos permite listar los archivos de un directorio

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)] # solo los archivos txt son los que se deben leer, primero revisa si termina en txt y luego lo agrega a la lista, solo lee txt en miniscula, si esta en mayuscula no

    for archivo in archivos_txt:
        with open(PLATILLOS + archivo) as platillo:
            for linea in platillo:
                # imprime los platillos
                print(linea.rstrip()) # eliminar espacios
            # imprime un separador entre platillos
            print('\r\n')

def agregar_orden():
    print('Escribe los datos para agregar la nueva orden') #probar cada paso, para saber donde esta el error
    nombre_orden = input('Nombre de la persona de la orden: \r\n')

    # Revisar si el archivo ya existe antes de crearlo
    existe = existe_orden(nombre_orden)

    if not existe:
        with open(ORDENES + nombre_orden + EXTENSION, 'w') as archivo:  #LOS + concatenan, es decir agregar cosas en una misma linea, solo variables
       
       # resto de los campos
            platillo_orden = input('Cual es la platillo del cliente: \r\n')
            bebida_orden = input('Agrega la bebida del cliente: \r\n')
            observaciones_orden = input('Alguna observacion en la orden: \r\n')

        # Instanciar la clase
            orden = Orden(nombre_orden, platillo_orden, bebida_orden, observaciones_orden) # contacto es el objeto

        # Escribir en el archivo
            archivo.write('Nombre de la persona de la orden:' + orden.nombre  + '\r\n') # como se quiere escribir, se le pone w, que es permiso de escritura, y cuando se poner as archivo, es para que toda lo que se pide, se refiera a archivo
        # se pone objeto. y los valores de la clase, en este caso contacto es el objeto y nombre parte de la clase
            archivo.write('Nombre del platillo:' + orden.platillo  + '\r\n')
            archivo.write('Bebida:' + orden.bebida  + '\r\n')
            archivo.write('Observaciones:' + orden.observaciones  + '\r\n')

        # Mostrar un mensaje de exito
            print('\r\n La orden fue creada correctamente \r\n')
    else:
        print('Ese nombre de persona ya existe')

    # Reiniciar el app
    app()

def eliminar_platillo():
    nombre = input('Seleccione el Platillo que desea eliminar: \r\n')

    try:
        os.remove(PLATILLOS + nombre + EXTENSION)
        print('Eliminado Correctamente')
    except IOError:
        print('No existe ese contacto')
        print(IOError)

    # reiniciar el app

    app()


def existe_orden(nombre):
    return os.path.isfile(ORDENES + nombre + EXTENSION)

def existe_platillo(nombre):
    return os.path.isfile(PLATILLOS + nombre + EXTENSION) # va a revisar si existe o no y nos va a retornar true o false en el existe

def crear_directorio():
    if not os.path.exists(PLATILLOS): #si una carpeta existe, y como lo estamos negando, quiere decir que si la carpeta no existe, crear la carpeta
        # crear la carpeta
        os.makedirs(PLATILLOS)   # se cambia 'conctactos/' por la constante CARPETA
  # se puede agregar un else 
    #else:
       #print('La carpeta ya existe')

    if not os.path.exists(ORDENES): #si una carpeta existe, y como lo estamos negando, quiere decir que si la carpeta no existe, crear la carpeta
        # crear la carpeta
        os.makedirs(ORDENES)   # se cambia 'conctactos/' por la constante CARPETA
  # se puede agregar un else 
    #else:
       #print('La carpeta ya existe')


app()
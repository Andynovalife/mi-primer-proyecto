# importar liberria
import os

CARPETA = 'contactos/' # cuando se pone en mayuscula, es para que otros programadores vean que es una constante y que no hay que modificarla
EXTENSION = '.txt' # Extension de archivos

# Contacto:
class Contacto:
    def __init__(self, nombre, telefono, categoria): # contstructor
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

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
            agregar_contacto() # estas son funciones
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3: 
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no valida, intente de nuevo')

def eliminar_contacto():
    nombre = input('Seleccione el Contacto que desea eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Eliminado Correctamente')
    except IOError:
        print('No existe ese contacto')
        print(IOError)

    # reiniciar el app

    app()

def buscar_contacto():
    nombre = input('Seleccione el Contacto que desea buscar: \r\n')

    #excepciones en programacion
    try:  # solo utilicelo donde puede que marque un error
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del Contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:   # Da informacion detallada del error, si hay un error se ejecuta automaticamente
        print('El archivo no existe')
        print(IOError)

    app ()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)  #listdir es un metodo que nos permite listar los archivos de un directorio

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)] # solo los archivos txt son los que se deben leer, primero revisa si termina en txt y luego lo agrega a la lista, solo lee txt en miniscula, si esta en mayuscula no

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                # imprime los contactos
                print(linea.rstrip()) # eliminar espacios
            # imprime un separador entre contactos
            print('\r\n')


def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')
    # Revisar si el archivo antes de editarlo
    existe = existe_contacto(nombre_anterior) #revisa el return y si es verdadero se devuelve a existe

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            # Resto de campos
            nombre_contacto = input('Agrega el Nuevo Nombre: \r\n')
            telefono_contacto = input('Agrega el Nuevo Telefono: \r\n')
            categoria_contacto = input('Agrega la Nueva Categoria: \r\n')

            # instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archivo
            archivo.write('Nombre:' + contacto.nombre  + '\r\n')
            archivo.write('Telefono:' + contacto.telefono  + '\r\n')
            archivo.write('Categoria:' + contacto.categoria  + '\r\n')

            # Renombrar el archivo  si pongo punto y luego algo, es un metodo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            # Mostrar mensaje de exito
        print('\r\n Contacto editado Correctamente \r\n')           

    else:
        print('Ese contacto no existe')

     # Reiniciar la aplicacion

    app()


def agregar_contacto():
    print('Escribe los datos para agregar el nuevo Contacto') #probar cada paso, para saber donde esta el error
    nombre_contacto = input('Nombre del Contacto: \r\n')

    # Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)

    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:  #LOS + concatenan, es decir agregar cosas en una misma linea, solo variables
       
       # resto de los campos
            telefono_contacto = input('Agrega el Telefono: \r\n')
            categoria_contacto = input('Categoria Contacto: \r\n')

        # Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto) # contacto es el objeto

        # Escribir en el archivo
            archivo.write('Nombre:' + contacto.nombre  + '\r\n') # como se quiere escribir, se le pone w, que es permiso de escritura, y cuando se poner as archivo, es para que toda lo que se pide, se refiera a archivo
        # se pone objeto. y los valores de la clase, en este caso contacto es el objeto y nombre parte de la clase
            archivo.write('Telefono:' + contacto.telefono  + '\r\n')
            archivo.write('Categoria:' + contacto.categoria  + '\r\n')

        # Mostrar un mensaje de exito
            print('\r\n Contacto creado Correctamente \r\n')
    else:
        print('Ese contacto ya existe')

    # Reiniciar el app
    app()

   


def mostrar_menu():
    print('Seleccione del Menu lo que desea hacer:')
    print('1) Agregar Nuevo Conctacto')
    print('2) Editar Conctacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Conctacto')


def crear_directorio():
    if not os.path.exists(CARPETA): #si una carpeta existe, y como lo estamos negando, quiere decir que si la carpeta no existe, crear la carpeta
        # crear la carpeta
        os.makedirs(CARPETA)   # se cambia 'conctactos/' por la constante CARPETA
  # se puede agregar un else 
   # else:
       # print('La carpeta ya existe')

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION) # va a revisar si existe o no y nos va a retornar true o false en el existe


app()
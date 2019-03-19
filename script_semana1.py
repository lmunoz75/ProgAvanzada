## Funciones
# Las funciones son codigos autónomos que implementan soluciones puntuales.
# Son parte del rompecabezas que puede ser un proyecto de programación final.
# Consisten en un bloque de codigo que toma valores de entrada (parametros) 
# para ser parte del proceso y retornar un valor o varios como resultado

def factores_primos(n):
    # Se tienen condiciones iniciales
    div = 2
    factores = []
    # Lazo que encuentra los divisores del numero (factores)
    while n is not 1:
        # Si se tiene un factor, se guarda en la lista de salida
        if n % div == 0:
            factores.append(div)
            n //=  div
        else:
            # ...de lo contrario se pasa a considerar el siguiente posible divisor
            div += 1
            
    return factores
        
factores_primos(65535)

# En la documentacion de Python se puede observar un par de parametros que pueden
# ser desconocidos: `*args` y `**kwargs`. Estos nombres son estandar de facto para 
# especificar un numero aleatorio de argumentos y los argumentos que tengas un 
# "keyword" asociado

def lista_pares(*args, **kwargs):
    options = args     # Tupla con los argumentos
    keywords = kwargs  # Diccionario con los keywords: valores
    lista = []
    
    if len(options) == 2:
        fin = options[1]
        if options[0] % 2 == 0:
            ini = options[0]
        else:
            ini = options[0] + 1
    elif len(options) == 1:
            ini = 0
            fin = options[0]
            
    if keywords.get('endpoint', False):
        fin += 1
            
    for n in range(ini, fin, 2):
        lista.append(n)
    
    return lista
    
print(lista_pares(15))
print(lista_pares(1, 16))
print(lista_pares(1, 16, endpoint=True))

## enumerate
# Instrucción de Python que retorna una lista enumerada que puede ser desempaquetada 
# por medio de un iterador (como un lazo for)

import random

listado_numeros = []

for n in range(10):
    listado_numeros.append(random.randrange(1, 101))
    
print("LISTADO DE NUMEROS ENTRE 1 Y 100")
print("-" * 32)
for idx, num in enumerate(listado_numeros):
    print(f"{idx+1:2}: {num}")
	
## zip
# Instrucción que permite desempaquetar los valores de varios contenedores 
#(listas, tuplas) en diferentes variables. Los contenedores deben de tener el 
# mismo número de elementos (en caso contrario, se obtendrá el número de elementos 
# igual al contenedor más pequeño).

import random

l1 = []
l2 = []
l3 = []

for n in range(5):
    l1.append(random.uniform(1, 10))
    l2.append(random.uniform(1, 10))
    l3.append(random.uniform(1, 10))

for col1, col2, col3 in zip(l1, l2, l3):
    print(f"{col1:.2f} | {col2:.2f} | {col3:.2f}")
	
## List comprehension
# Permite crear listas de forma resumida con instrucciones empaquetadas siguiendo 
# las reglas de la "programacion funcional". Esto permite que aunque no sea una 
# estructura visualmente natural si sea gramaticalmente simple

ABC = [chr(char) for char in range(ord('A'), ord('Z') + 1)]
abc = [chr(char).lower() for char in range(ord('A'), ord('Z') + 1)]

for LETTER, letter in zip(ABC, abc):
    print("{} - {}".format(letter, LETTER))
	
## Map, Filter y Lambda Expresions
# La instruccion map permite procesar los elementos de una lista por una función 
# que realice alguna operación aritmética. La instruccion filter hace lo mismo pero 
# utilizando una función que realiza alguna operación lógica. Para ambos casos, 
# la definición de la función puede ser "anónima", lo que se conoce como funciones "lambda".

from random import randrange

notas = [randrange(5, 18) for i in range(12)]
notas_curva = list(map(lambda x: x + 2, notas))
num_aprobados = len(list(filter(lambda x: x > 10, notas_curva)))

for nota, nota_curva in zip(notas, notas_curva):
    print(f"{nota:0>2} -> {nota_curva:0>2}")
    
print(f"\nNumero de aprobados: {num_aprobados}")

## yield
# La instruccion `yield` permite generar "iteradores". Estos son de utilidad si 
# se quieren generar una gran cantidad de datos para luego ser procesados por un 
# lazo for (iterador) sin tener que ocupar grandes porciones de memoria.

def genera_letras(case='upper'):
    if case == 'upper':
        letter_ini = 'A'
    elif case == 'lower':
        letter_ini = 'a'
        
    for alpha in range(ord(letter_ini), ord(letter_ini) + 26):
        yield chr(alpha)
		
	genera_letras()

###	
iterador = genera_letras(case='lower')

###
for letra in iterador:
    print(letra)
	
## Archivos
# Se pueden escribir o leer archivos de texto en Python para almacenar 
# información en forma de texto.

# Generamos un archivo de texto
from random import randrange

nombres = ['Juan', 'Pedro', 'Maria', 'Cecilia', 'Renato', 'Cesar', 'Ana', 'Roberto', 'Maria']
apellidos = ['Perez', 'Quispe', 'Palomino', 'Quezada', 'Ramos', 'Salas', 'Porras', 'Gomez', 'Gonzalez']
contactos = set()
num_iteraciones = 12

for i in range(num_iteraciones):
    contactos.add(nombres[randrange(len(nombres))] + ' ' + apellidos[randrange(len(apellidos))])

with open("contactos.txt", mode='w') as f: 
    for contacto in contactos:
        f.write(contacto + '\n')

        
# Leemos el archivo de texto
f = open("contactos.txt")
lista_contactos = f.readlines()
f.close()

lista_contactos.sort()
for idx, contacto in enumerate(lista_contactos):
    print(f"{idx+1:2}: {contacto.strip()}")
	
# También se puede registrar texto con algún formato de intercambio, 
# como un archivo CSV, donde los datos estan separados por algún 
# caracter especial ("," o ";")

import csv
from random import randrange

nombres = ['Juan', 'Pedro', 'Maria', 'Cecilia', 'Renato', 'Cesar', 'Ana', 'Roberto', 'Maria']
apellidos = ['Perez', 'Quispe', 'Palomino', 'Quezada', 'Ramos', 'Salas', 'Porras', 'Gomez', 'Gonzalez']
contactos = set()
num_iteraciones = 12

for i in range(num_iteraciones):
    contactos.add(nombres[randrange(len(nombres))] + ';' + apellidos[randrange(len(apellidos))])

# Se genera un archivo CSV (separado por ";")
with open("contactos.csv", mode='w') as f: 
    f.write("NOMBRE; APELLIDO\n")
    for contacto in contactos:
        f.write(contacto + '\n')

# Se lee el contenido del archivo CSV
with open("contactos.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=";")
    next(reader)
    for nombre, apellido in reader:
        print(apellido + ", " + nombre)
		
# Otro formato muy popular en el intercambio de datos es el JSON (JavaScript 
# Object Notation) en donde los datos se registran en un formato par llave-valor 
# (un diccionario) lo que hace que la información tenga un formato y sea legible.

import json
from random import randrange

nombres = ['Juan', 'Pedro', 'Maria', 'Cecilia', 'Renato', 'Cesar', 'Ana', 'Roberto', 'Maria']
apellidos = ['Perez', 'Quispe', 'Palomino', 'Quezada', 'Ramos', 'Salas', 'Porras', 'Gomez', 'Gonzalez']
num_iteraciones = 4

# Se genera un diccionario con una llave contactos y un lista como valor con un diccionario con
# la informacion de contacto (nombre, apellido)
data = dict(contactos=[])

for i in range(num_iteraciones):
    data['contactos'].append({'nombre': nombres[randrange(len(nombres))],
                            'apellido': apellidos[randrange(len(apellidos))]
                           })
    
with open("data.json", mode='w') as json_file:
    json.dump(data, json_file)

# Se lee el archivo JSON para obtener los datos en forma de diccionario
with open("data.json") as json_file:
    data = json.load(json_file)

for idx, contactos in enumerate(data['contactos']):
    print(f"Contacto {idx+1:2}:")
    for k, v in contactos.items():
        print(f"\t{k.capitalize()}: {v.capitalize()}")
    else:
        print()
		
# Otra forma de leer barrer un registro JSON en utilizando json.dumps y especificando
# el numero de espacios para la indentancion con el keyword "indent"
with open("data.json") as json_file:
    data = json.load(json_file)
    
print(json.dumps(data, indent=4))

## Programacion Orientada a Objetos (OOP)
# Es un paradigma de programacion en el que se crea una entidad llamada "clase" 
# que encapsula en una sola estructura propiedades (variables) y funciones (métodos) 
# asociados a un "objeto". Luego, estos objetos pueden ser "instanciados" a partir de 
# una clase que sirve como plantilla.
class _Persona:
    def __init__(self, nombre='', apellido='', ID=''):
        self.nombre = nombre
        self.apellido = apellido
        self.ID = ID
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, val):
        if isinstance(val, str):
            self.__nombre = val
        else:
            raise TypeError("El campo 'nombre' debe ser tipo 'str'")
    
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, val):
        if isinstance(val, str):
            self.__apellido = val
        else:
            raise TypeError("El campo 'apellido' debe ser tipo 'str'")
    
    @property
    def ID(self):
        return self.__ID
    
    @ID.setter
    def ID(self, val):
        if isinstance(val, str):
            self.__ID = val
        else:
            raise TypeError("El campo 'ID' debe ser tipo 'str'")

###			
class Contacto(_Persona):
    def __init__(self, nombre, apellido, ID, telefono=''):
        super().__init__(nombre, apellido, ID)
        self.__mail = self.__set_mail()
        self.telefono = telefono
     
    def __set_mail(self):
        return self.nombre[0].lower() + self.apellido[1:8]+ "@mail.com"
    
    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self,val):
        if isinstance(val,str):
            if val[0] == '9':
                self.__telefono = val
            else:
                raise ValueError("El dato 'telefono' debe ser un numero celular valido")
        else:
            raise TypeError("El dato 'telefono' debe ser un 'str'")
    
    
    def __repr__(self):
        str_out = "Contacto:\n"
        str_out += "\tNombre: {}\n".format(self.nombre)
        str_out += "\tApellido: {}\n".format(self.apellido)
        str_out += "\tID: {}\n".format(self.ID)
        str_out += "\tMail: {}\n".format(self.__mail)
        str_out += "\tTelefono: {}\n".format(self.telefono)
        return str_out
        
p1 = Contacto(nombre='Juan', apellido='Perez', ID='1029282', telefono='987-876-987')
print(p1)

###
dir(p1)

## Tiempo en Python - `time`
# El tiempo es un objeto medible en Python, gracias a la libreria `time`
import time

time_now = time.localtime()

print("Hora:", time_now.tm_hour)
print("Minuto:", time_now.tm_min)
print("Segundo:", time_now.tm_sec)
print()
print("Dia:", time_now.tm_mday)
print("Mes:", time_now.tm_mon)
print("Año:", time_now.tm_year)
print()
print("Dia del año:", time_now.tm_yday)
print()
print(time.asctime())

# time.time() retorna el numero de segundos desde el UNIX epoch (1/1/1970)
# time.ctime() toma el UNIX time y lo retorna en formato impreso
time_now = time.time() 

print(time_now)
print(time.ctime(time_now))

# strftime(format_string) permite formtear el tiempo utilizando un struct_time
time_now = time.localtime()

print("Fecha y Hora:", time.strftime("%d/%m/%Y %H:%M:%S %p", time_now))

## Tiempo en Python - `datetime`
# La fecha y hora tambien son objetos que pueden ser manipulados en Python, 
# utilizando la librería `datetime`
import datetime

fecha = datetime.datetime.now()
print("'fecha' es un objeto --->", type(fecha))
print()
print("Hora:", fecha.hour)
print("Minuto:", fecha.minute)
print("Dia:", fecha.day)
print("Mes:", fecha.month)
print("Año:", fecha.year)
print()
print(fecha.strftime("%A %d/%m/%Y %H:%m %p"))

###
fecha_nac = datetime.datetime(1975, 2, 28, 23, 45, 0)
fecha_hoy = datetime.datetime.now()

# Cuando se suman o restan dos objetos clase datetime, lo que se obtiene es un timedelta
delta_tiempo = fecha_hoy - fecha_nac
print(type(delta_tiempo))
print(delta_tiempo)

###
# Cuanto tiempo de vida me queda...
dd_nac, mm_nac, yy_nac = input("Ingrese su fecha de nacimiento [dd/mm/yyyy]: ").split("/")
fecha_nac = datetime.datetime(int(yy_nac), int(mm_nac), int(dd_nac), 0, 0, 0)

n_anios = int(input("Cuantos años espera vivir?: "))
delta_anios = datetime.timedelta(days=365 * n_anios)

fecha_fin = fecha_nac + delta_anios
dias_restantes = fecha_fin - datetime.datetime.now()

print(f"Aun le quedan {dias_restantes.days} dias en este mundo. Disfrutelos...")
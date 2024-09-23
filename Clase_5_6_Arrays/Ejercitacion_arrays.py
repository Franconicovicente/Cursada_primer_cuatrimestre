import random
'''
Ejercitación Clase 8 (Arreglos Unidimensionales)

1. Escribir una función que reciba como parámetro una lista de str y cuente la cantidad de elementos con más de cinco caracteres.
Para contar los caracteres de un string también se usa la función len

2. Escribir una función que reciba como parámetro una lista de str y retorne una nueva lista con los elementos de más de cinco caracteres.

3. Escribir una función que me permita ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Retornar una lista con el/los nombres de la personas con el nombre más corto (tener en cuenta más de un mínimo)

4. Escribir una función que reciba una lista de apellidos comunes como esta:
apellidos_comunes = [“López”, “Gómez”, “Fernández”, “Pérez”, “Martínez” ]
Ingresar 10 apellidos y guardarlos en otra lista. Contar cuantas veces se repiten los apellidos comunes.

Ejemplo
López se repite 2 veces
Gómez se repite 0 veces
Fernández se repite 1 vez
Pérez se repite 0 veces
Martínez se repite 3 veces

5.Escribir un programa que me permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años). Utilizar listas paralelas.
(Hacer dos funciones, una para la carga de productos y otra para mostrarlos)

6. Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Mostrar la cantidad de productos que tienen un precio mayor al primer producto ingresado.
(Hacer dos funciones, una para la carga de productos y otra para mostrarlos)

7. La utn fra necesita un sistema saber la nota promedio más alta entre 5 alumnos de la Materia Programación I. 
Para eso debemos guardar.

Nombre (Ingresa usuario)
Apellido (Ingresa usuario)
Legajo (Ingresa usuario entre 10000 y 99999)
Nota primer parcial (Número aleatorio entre 1 y 10)
Nota segundo parcial (Número aleatorio entre 1 y 10)

Aparte de saber cuál fue esa nota debemos mostrar cuál fue el alumno, en caso de haber más de un alumno con la misma nota promedio mostrar a los dos.
'''

# 1. Escribir una función que reciba como parámetro una lista de str y cuente la cantidad de elementos con más de cinco caracteres.
# Para contar los caracteres de un string también se usa la función len

lista_de_strings = ["Perro", "Gato", "Loro", "Conejo", "Fenrir", "Skadi", "Ratatoskr", "Lancelot"]

def recibir_string (lista_de_strings:list):
    '''
    Recibe una lista con strings
    Devuelve aquellos elementos que tengan mas de cinco caracteres
    '''
    contador_elementos = 0
    for elementos in lista_de_strings:
        if len(elementos) > 5:
            contador_elementos += 1

    return f"Los elementos con mas de cinco caracteres en la lista son igual a {contador_elementos}"

print(recibir_string(lista_de_strings))

# # 2. Escribir una función que reciba como parámetro una lista de str y retorne una nueva lista con los elementos de más de cinco caracteres

lista_de_strings = ["Perro", "Gato", "Loro", "Conejo", "Fenrir", "Skadi", "Ratatoskr", "Lancelot"]

def retornar_nueva_lista(lista_de_strings:list):
    '''
    Se le da una lista con nombres
    Retorna una nueva lista, con elementos de mas de cinco caracteres
    '''
    contador_elementos = 0
    lista_cinco_caracteres = []
    for elementos in lista_de_strings:
        if len(elementos) > 5:
            contador_elementos += 1
            lista_cinco_caracteres.append(elementos)

    return lista_cinco_caracteres

respuesta = retornar_nueva_lista(lista_de_strings)

for elementos in respuesta:
    print(elementos)

# 3. Escribir una función que me permita ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Retornar una lista con el/los nombres de la personas con el nombre más corto (tener en cuenta más de un mínimo)
lista_nombres = []
lista_nombres_cortos = []
def ingresar_nombres():
    '''
    Se le ingresa nombres a una lista
    Luego filtra por los nombres mas cortos, y retorna una nueva lista con esos nombres
    '''
    nombre_minimo = None
    bandera = True

    for i in range(5):
        nombre_auxiliar = input("Ingrese el nombre que desee: ")
        lista_nombres.append(nombre_auxiliar)
        if bandera == True or len(nombre_auxiliar) < nombre_minimo:
            nombre_minimo = (len(nombre_auxiliar))
            bandera = False
    
    for i in range (len(lista_nombres)):
        if len(lista_nombres[i]) == nombre_minimo:
            lista_nombres_cortos.append(lista_nombres[i])
    
    return lista_nombres_cortos

resultado = ingresar_nombres()

for resultado in lista_nombres_cortos:
    print(resultado)

# 4. Escribir una función que reciba una lista de apellidos comunes como esta:
# apellidos_comunes = [“López”, “Gómez”, “Fernández”, “Pérez”, “Martínez” ]
# Ingresar 10 apellidos y guardarlos en otra lista. Contar cuantas veces se repiten los apellidos comunes.

# Ejemplo
# López se repite 2 veces
# Gómez se repite 0 veces
# Fernández se repite 1 vez
# Pérez se repite 0 veces
# Martínez se repite 3 veces

apellidos_comunes = ["Lopez", "Gomez", "Fernandez", "Perez", "Martinez"]


def guardar_apellidos (apellidos_comunes:list):
    '''
    A los apellidos que agrega el usuario, se los agrega en una lista y se los compara con los comunes ya dados.
    Si coinciden, se cuenta cuantas veces coincidio con cada apellido y retorna un mensaje con esa informacion 
    '''
    apellidos_otra_lista = []

    for i in range(10):
        apellido_aux = input("Ingrese el apellido: ")
        apellidos_otra_lista.append(apellido_aux)

    for apellido_comun in apellidos_comunes:
        contador = 0
        for apellido_ingresado in apellidos_otra_lista:
            if apellido_comun == apellido_ingresado:
                contador += 1
        if contador == 1:
            print(f"{apellido_comun} se repitio {contador} vez")
        else:
            print(f"{apellido_comun} se repitio {contador} veces")

guardar_apellidos(apellidos_comunes)


# 5.Escribir un programa que me permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años). Utilizar listas paralelas.
# (Hacer dos funciones, una para la carga de productos y otra para mostrarlos)
lista_nombres = []
lista_edades = []

def cargar_nombre_edad ():
    '''
    El usuario ingresa un nombre y una edad.
    Si la edad es mayor o igual a 18, se guarda en la lista de nombres
    '''
    for i in range(5):
        nombre_aux = input("Ingrese el nombre: ")  
        edad_aux = int(input("Ingrese la edad: "))

        lista_edades.append(edad_aux)
        if edad_aux >= 18:
            lista_nombres.append(nombre_aux)
    
    return lista_nombres

def mostrar_resultado():
    '''
    Los nombres de la funcion cargar_nombre_edad se muestran
    '''
    resultado = cargar_nombre_edad()
    for resultado in lista_nombres:
        print(resultado)

mostrar_resultado()

# 6. Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Mostrar la cantidad de productos que tienen un precio mayor al primer producto ingresado.
# (Hacer dos funciones, una para la carga de productos y otra para mostrarlos)

nombres_productos = []
precios_productos = []
lista_productos_mayor = []

def cargar_productos () -> list:
    '''
    El usuario carga un producto y un precio.
    Se guarda el primer precio y se hace una comparacion con los siguientes. Si es mayor, se guarda en una lista y se imprime
    '''
    for i in range(3):
        producto = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))

        nombres_productos.append(producto)
        precios_productos.append(precio)

    precio_minimo = precios_productos[0]
    print(f"El primer producto es {nombres_productos[0]} con un precio de {precio_minimo}")

    for i in range(1, len(precios_productos)):
        if precios_productos[i] > precio_minimo:
            lista_productos_mayor.append(nombres_productos[i])
    
    


    print("Nombre de los productos que superaron el precio mínimo: ", end="")
    for producto in lista_productos_mayor:
        print(producto, end=" ")

cargar_productos()

# 7. La utn fra necesita un sistema saber la nota promedio más alta entre 5 alumnos de la Materia Programación I. 
# Para eso debemos guardar.

# Nombre (Ingresa usuario)
# Apellido (Ingresa usuario)
# Legajo (Ingresa usuario entre 10000 y 99999)
# Nota primer parcial (Número aleatorio entre 1 y 10)
# Nota segundo parcial (Número aleatorio entre 1 y 10)

# Aparte de saber cuál fue esa nota debemos mostrar cuál fue el alumno, en caso de haber más de un alumno con la misma nota promedio mostrar a los dos.
lista_nombre = []
lista_apellido = []
lista_legajo = []
lista_primer_parcial = []
lista_segundo_parcial = []
lista_promedios = []
bandera_notas = True


def cargar_datos_utn():
    '''
    Carga de datos del usuario
    ''' 
    for i in range(5):
        nombre = input("Ingrese el nombre: ")
        apellido = (input("Ingrese el apellido: "))
        legajo = int(input("Ingrese el legajo: "))
        while legajo < 9999 or legajo > 100000:
            legajo = int(input("Ingrese legajo valido: "))

        nota_primer_parcial = random.randint(1, 10)
        nota_segundo_parcial = random.randint(1, 10)

        promedio = (nota_primer_parcial + nota_segundo_parcial) / 2

        lista_nombre.append(nombre)
        lista_apellido.append(apellido)
        lista_legajo.append(legajo)
        lista_primer_parcial.append(nota_primer_parcial)
        lista_segundo_parcial.append(nota_segundo_parcial)  
        lista_promedios.append(promedio)


def mostrar_mejor_promedio():
    '''
    Se calcula el promedio de la lista promedios, 
    luego si el numero del indice coincide con el mejor promedio, se muestran los datos del estudiante
    '''
    mejor_promedio = lista_promedios[0]

    for promedio in lista_promedios:
        if promedio > mejor_promedio:
            mejor_promedio = promedio

    for i in range(5):
        if lista_promedios[i] == mejor_promedio:
            print(f"Alumno: {lista_nombre[i]} {lista_apellido[i]}")
            print(f"Legajo: {lista_legajo[i]}")
            print(f"Nota promedio de: {lista_promedios[i]}")

cargar_datos_utn()
mostrar_mejor_promedio()
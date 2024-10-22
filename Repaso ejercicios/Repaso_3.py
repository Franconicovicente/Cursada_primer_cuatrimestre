import random
'''

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

# Aparte de saber cuál fue esa nota debemos mostrar cuál fue el alumno, en caso de haber más de un alumno con la misma nota promedio mostrar a los dos.

# '''
def validar_str (texto:str):
    '''
    
    '''
    while not texto.isalpha():
        texto = input("Ingrese nuevamente el dato: ")
    
    return texto

# # 1. Escribir una función que reciba como parámetro una lista de str y cuente la cantidad de elementos con más de cinco caracteres.
# # Para contar los caracteres de un string también se usa la función len
# lista_str = ["Pepe","",""]

# def contar_elementos(lista:list) -> int:
#     '''
    
#     '''
#     contador_elementos = 0
#     for i in range(len(lista)):
#         if len(lista[i]) > 5:
#             contador_elementos += 1
#             resultado = f"Hay un total de {contador_elementos} elementos que superan los 5 caracteres"
#         else:
#             resultado = "Ningun elemento superó 5 caracteres"

#     return resultado


# # print(contar_elementos(lista_str))

# # 2. Escribir una función que reciba como parámetro una lista de str y retorne una nueva lista con los elementos de más de cinco caracteres.

# def retornar_nueva_lista(lista:list) -> int:
#     '''
    
#     '''
#     lista_aux = []
#     for i in range(len(lista)):
#         if len(lista[i]) > 5:
#             lista_aux.append(lista[i])

#     return lista_aux

# # resultado = retornar_nueva_lista(lista_str)
# # print("Nombres que superan los cinco caracteres:")

# # for i in range(len(resultado)):
# #         print(resultado[i])

# # 3. Escribir una función que me permita ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Retornar una lista con el/los nombres de la personas con el nombre más corto (tener en cuenta más de un mínimo)
# lista_vacia = []
# def ingresar_nombres(lista:list) -> str:
#     '''
    
#     '''
#     bandera_nombres = True
#     lista_mas_cortos = []
#     for i in range(5):
#         nombre = input("Ingrese el nombre a cargar:")
#         lista.append(nombre)
#         nombre_mas_corto = lista[0]
#         if len(nombre) < len(nombre_mas_corto) or bandera_nombres == True:
#             nombre_mas_corto = lista[i]
#             lista_mas_cortos.append(nombre_mas_corto)
#             bandera_nombres = False

#         elif len(nombre) == len(nombre_mas_corto):
#             lista_mas_cortos.append(nombre)

#     return lista_mas_cortos

# # print(ingresar_nombres(lista_vacia))


# # 4. Escribir una función que reciba una lista de apellidos comunes como esta:
# # apellidos_comunes = [“López”, “Gómez”, “Fernández”, “Pérez”, “Martínez” ]
# # Ingresar 10 apellidos y guardarlos en otra lista. Contar cuantas veces se repiten los apellidos comunes.

# # Ejemplo
# # López se repite 2 veces
# # Gómez se repite 0 veces
# # Fernández se repite 1 vez
# # Pérez se repite 0 veces
# # Martínez se repite 3 veces

# apellidos_comunes = ["lopez", "gomez", "fernandez", "perez", "martinez"]
# lista_apellidos = []
# def contar_apellidos_repetidos (lista:list) -> int:
#     '''
    
#     '''
#     nueva_lista = []
#     for i in range(10):
#         apellido = input("Ingrese un apellido: ")
#         validar_str(apellido)
#         nueva_lista.append(apellido)

#     for apellido_comun in lista:
#         contador = 0
#         for apellido_ingresado in nueva_lista:
#             if apellido_comun == apellido_ingresado:
#                 contador += 1
        
#         if contador == 1:
#             print(f"El apellido {apellido_comun} se repitio 1 vez.")
#         else:
#             print(f"El apellido {apellido_comun} se repitio {contador} veces.")


# contar_apellidos_repetidos(apellidos_comunes)
# 5.Escribir un programa que me permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años). Utilizar listas paralelas.
# (Hacer dos funciones, una para la carga de productos y otra para mostrarlos)

# lista_nombres = []
# lista_edades = []

# def cargar_nombres_y_edades ():
#     '''
    
#     '''

#     for i in range(5):

#         nombre = input("Ingrese el nombre: ")
        
#         edad = int(input("Ingrese la edad: "))
#         while edad < 0 or edad > 120:
#             edad = int(input("ERROR, reingrese edad: "))
        
#         lista_edades.append(edad)

#         if edad >= 18:
#             lista_nombres.append(nombre)

    
#     return lista_nombres


# def mostrar_nombres():
#     '''
    
#     '''
#     resultado = cargar_nombres_y_edades()

#     for resultado in lista_nombres:
#         print(resultado)

# mostrar_nombres()

# 6. Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Mostrar la cantidad de productos que tienen un precio mayor al primer producto ingresado.
# (Hacer dos funciones, una para la carga de productos y otra para mostrarlos)

# lista_productos = []
# lista_precios = []


# def cargar_productos ():
#     '''
    
#     '''
#     for i in range(5):

#         nombre_producto = input("Ingrese el nombre del producto: ")
#         precio_producto = float(input("Ingrese el precio del producto: "))

#         lista_productos.append(nombre_producto)
#         lista_precios.append(precio_producto)

#     contador_productos = 0
#     precio_primer_producto = lista_precios[0]

#     for precio in lista_precios:
#         if precio > precio_primer_producto:
#             contador_productos += 1
    

#     return contador_productos

# def mostrar_productos():
#     '''
    
#     '''
    
#     resultado = cargar_productos()

#     print(f"Cantidad de productos que superan el primer precio = {resultado}")

# mostrar_productos()

# 7. La utn fra necesita un sistema saber la nota promedio más alta entre 5 alumnos de la Materia Programación I. 
# Para eso debemos guardar.

# Nombre (Ingresa usuario)
# Apellido (Ingresa usuario)
# Legajo (Ingresa usuario entre 10000 y 99999)
# Nota primer parcial (Número aleatorio entre 1 y 10)
# Nota segundo parcial (Número aleatorio entre 1 y 10)

# Aparte de saber cuál fue esa nota debemos mostrar cuál fue el alumno, en caso de haber más de un alumno con la misma nota promedio mostrar a los dos.

lista_nombre_alumno = []
lista_apellido_alumno = []
lista_legajo = []
lista_promedios = []
lista_primer_parcial = []
lista_segundo_parcial = []

def cargar_alumnos ():
    '''
    
    '''
    for i in range(3):

        nota_primer_parcial = random.randint(1,10)
        nota_segundo_parcial = random.randint(1,10)

        nombre = input("Ingrese nombre del alumno: ")

        apellido = input("Ingrese apellido del alumno: ")

        legajo = int(input("Ingrese legajo del alumno: "))
        while legajo < 10000 or legajo > 99999:
            legajo = int(input("ERROR, reingrese legajo: "))

        promedio_nota = (nota_primer_parcial + nota_segundo_parcial) / 2
        print(f"promedio nota: {promedio_nota}")

        lista_promedios.append(promedio_nota)
        lista_legajo.append(legajo)
        lista_apellido_alumno.append(apellido)
        lista_segundo_parcial.append(nota_segundo_parcial)
        lista_nombre_alumno.append(nombre)
        lista_primer_parcial.append(nota_primer_parcial)

def mostrar_alumnos():
    '''
    
    '''
    mejor_promedio = lista_promedios[0]

    for promedio in lista_promedios:
        if promedio > mejor_promedio:
            mejor_promedio = promedio

    for i in range(3):
        if lista_promedios[i] == mejor_promedio:
            print(f"Mejor alumno : {lista_nombre_alumno[i]} {lista_apellido_alumno[i]}")
            print(f"Nota: {mejor_promedio}")


cargar_alumnos()
mostrar_alumnos()
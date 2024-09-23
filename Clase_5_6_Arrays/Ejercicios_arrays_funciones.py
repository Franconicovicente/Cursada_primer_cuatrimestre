import random
# Ejercitación Clase 7 (Arreglos Unidimensionales)

# 1. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.
lista_enteros = [0,0,0,0,0]

def recibir_lista_enteros(lista_enteros):
    suma_enteros = 0
    if len(lista_enteros) == 0:
        print ("No se puede dividir por 0")
    else:
        for i in range (len(lista_enteros)):
            numero_entero = int(input("Ingrese un numero entero: "))
            suma_enteros += numero_entero
    
    promedio_numeros_enteros = suma_enteros / len(lista_enteros)
    return promedio_numeros_enteros


print(recibir_lista_enteros(lista_enteros))
# 2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos. En caso de no haber números positivos validar división por cero

def lista_positivos (lista_nums_positivos):
    positivos = []
    suma_positivos = 0
    for i in range (len(lista_nums_positivos)):
        numero = int(input("Ingrese un numero positivo: "))
        if numero > 0:
            positivos.append(numero)
            suma_positivos += numero
    if len(positivos) > 0:
        promedio_numeros_positivos = suma_positivos / len(positivos)
        return promedio_numeros_positivos
    else:
        return "Error: no se ingresaron numeros positivos"



lista_nums_positivos = [0, 0, 0, 0, 0,]

print(lista_positivos(lista_nums_positivos))

# 3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro

def calcular_producto (lista_producto:list):
    producto_numeros = 1
    for i in range (len(lista_producto)):
        numero = int(input("Ingrese su numero: "))
        producto_numeros *= numero

    return producto_numeros

lista_producto = [0, 0, 0, 0, 0]

print(calcular_producto(lista_producto))

# 4.Escribir una función que reciba como parámetros una lista de enteros y retorne el índice del valor máximo encontrado (retornar un sólo índice, en caso de que haya más de un máximo el primero)

lista_indice_enteros = [0,0,0,0,0]

def retornar_indice (lista_indice_enteros:list):
    maximo = lista_indice_enteros[0]
    indice = 0
    for i in range (len(lista_indice_enteros)):
        numero = int(input("Ingrese un numero: "))
        lista_indice_enteros[i] = numero
        if lista_indice_enteros[i] > maximo:
            maximo = lista_indice_enteros[i]
            indice = i

    return f"El numero maximo encontrado fue en el indice numero {indice}"
            
print(retornar_indice(lista_indice_enteros))

# Ejemplo [2,5,5,3,1] -> Retorna el índice 1

# 5. Escribir una función que reciba como parámetros una lista de enteros y muestre el índice del valor máximo encontrado (no se tienen en cuenta si hay más de un máximo) Reutilizar la función anterior.

# Ejemplo [2,5,5,3,1] -> Imprime el índice  1
lista_indice_enteros = [0,0,0,0,0]

def retornar_indice (lista_indice_enteros:list):
    maximo = lista_indice_enteros[0]
    indice = 0
    for i in range (len(lista_indice_enteros)):
        numero = int(input("Ingrese un numero: "))
        lista_indice_enteros[i] = numero
        if lista_indice_enteros[i] > maximo:
            maximo = lista_indice_enteros[i]
            indice = i

    return f"El numero maximo encontrado fue en el indice numero {indice}"

print(retornar_indice(lista_indice_enteros))
# 6.Escribir una función que reciba como parámetros una lista de enteros y retorne todos los índices del valor máximo encontrado (Puede haber más de uno)

# Ejemplo [2,5,5,3,1] -> Retorna el índice [1,2]
lista_indice_enteros = [0,0,0,0,0]

def retornar_indice (lista_indice_enteros:list):
    maximo = lista_indice_enteros[0]
    indices_maximos = []
    for i in range (len(lista_indice_enteros)):
        numero = int(input("Ingrese un numero: "))
        lista_indice_enteros[i] = numero
        if numero > maximo:
            maximo = numero
    for i in range (len(lista_indice_enteros)):
        if lista_indice_enteros[i] == maximo:
            indices_maximos.append(i)
    
    
    


    return f"El numero maximo es {maximo} y se encuentra en los indices {indices_maximos}"
            
print(retornar_indice(lista_indice_enteros))


# 7. Escribir una función que reciba como parámetros una lista de enteros y muestre la posición del valor máximo encontrado. Reutilizar la función anterior.

# Ejemplo [2,5,5,3,1] -> Muestra tanto el índice 1 como el 2
lista_indice_enteros = [0,0,0,0,0]

def retornar_indice (lista_indice_enteros:list):
    maximo = lista_indice_enteros[0]
    indices_maximos = []
    for i in range (len(lista_indice_enteros)):
        numero = int(input("Ingrese un numero: "))
        lista_indice_enteros[i] = numero
        if numero > maximo:
            maximo = numero
    for i in range (len(lista_indice_enteros)):
        if lista_indice_enteros[i] == maximo:
            indices_maximos.append(i)
    
    
    


    return f"El numero maximo es {maximo} y se encuentra en los indices {indices_maximos}"

print(retornar_indice(lista_indice_enteros))

# 8. Definir y cargar una lista con 10 sueldos enteros aleatorios (utilizar random), entre ARS 350.000 y ARS 1.250.000. 
# Calcular el porcentaje de personas que superan el salario promedio de estos mismos.
def calcular_sueldos():

    lista_sueldos = []
    acumulador_sueldos = 0
    contador_superan_sueldo = 0

    for i in range(10):
        sueldo_random = random.randint(350000, 12500000)
        acumulador_sueldos += sueldo_random
        lista_sueldos.append(sueldo_random)

    promedio = round(acumulador_sueldos / len(lista_sueldos), 2)

    for sueldo in lista_sueldos:
        if sueldo > promedio:
            contador_superan_sueldo += 1

    porcentaje_superan_sueldo_promedio = round((contador_superan_sueldo / (len(lista_sueldos))) * 100, 2)

    return(f"La lista de los sueldos es = {lista_sueldos}\nEl promedio de los sueldos es = {promedio}\nEl porcentaje de personas que superan ese sueldo es de un {porcentaje_superan_sueldo_promedio}%")

print(calcular_sueldos())
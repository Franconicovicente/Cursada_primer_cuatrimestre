'''
1. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.

2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos. En caso de no haber números positivos validar división por cero

3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro

4.Escribir una función que reciba como parámetros una lista de enteros y retorne el índice del valor máximo encontrado (retornar un sólo índice, en caso de que haya más de un máximo el primero)

Ejemplo [2,5,5,3,1] -> Retorna el índice 1

5. Escribir una función que reciba como parámetros una lista de enteros y muestre el índice del valor máximo encontrado (no se tienen en cuenta si hay más de un máximo) Reutilizar la función anterior.

Ejemplo [2,5,5,3,1] -> Imprime el índice  1 y su valor


6.Escribir una función que reciba como parámetros una lista de enteros y retorne todos los índices del del valor máximo encontrado (Puede haber más de uno)

Ejemplo [2,5,5,3,1] -> Retorna el índice [1,2]


7. Escribir una función que reciba como parámetros una lista de enteros y muestre la posición del valor máximo encontrado. Reutilizar la función anterior.

Ejemplo [2,5,5,3,1] -> Muestra tanto el índice 1 como el 2 y sus valores

8. Definir y cargar una lista con 10 sueldos enteros aleatorios (utilizar random), entre ARS 350.000 y ARS 1.250.000. Calcular el porcentaje de personas que superan el salario promedio de estos mismos.
'''

# 1. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.
# lista = [5,3,2,-1]
def recibir_enteros_devolver_promedio(lista_enteros:list) -> int:
    '''
    
    '''
    lista_numeros = []
    suma_enteros = 0
    for i in range(len(lista_enteros)):
        numero = int(input("Ingrese su numero: "))
        lista_numeros.append(numero)
        suma_enteros += numero

    promedio_numeros = suma_enteros / len(lista_numeros)

    return promedio_numeros
lista = [0,0,0,0,0]

# resultado = recibir_enteros_devolver_promedio(lista)

# print(f"El promedio de la suma es {resultado}")

# 2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos. En caso de no haber números positivos validar división por cero

def recibir_enteros_devolver_promedio_positivos(lista_enteros:list) -> int:
    '''
    
    '''
    positivos = []
    suma_numeros = 0
    for i in range (len(lista_enteros)):
        numero = int(input("Ingrese su numero: "))
        if numero > 0:
            suma_numeros += numero
            positivos.append(numero)
            promedio_suma_numeros = suma_numeros / len(positivos) 
            resultado = f"El resultado es = {promedio_suma_numeros}"
        elif numero < 0:
            resultado = "No se ingresaron numeros positivos"
    return resultado
lista_nums_positivos = [0,0,0,0,0]

# resultado = recibir_enteros_devolver_promedio_positivos(lista_nums_positivos)

# print(f"{resultado}")

# 3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro

def calcular_producto(lista:list) -> int:
    '''
    
    '''
    lista_aux = []
    producto = 1
    for i in range(len(lista)):
        numero = int(input("Ingrese numeros que quiere multiplicar: "))
        lista_aux.append(numero)
        producto *= numero

    return producto
# lista_aux = [0,0,0,0,0]

# print(calcular_producto(lista_aux))

# 4.Escribir una función que reciba como parámetros una lista de enteros y retorne el índice del valor máximo encontrado (retornar un sólo índice, en caso de que haya más de un máximo el primero)

# Ejemplo [2,5,5,3,1] -> Retorna el índice 1

def retornar_indice_valor_maximo(lista:list) -> int:
    '''
    
    '''
    num_max = lista[0]
    indice = 0
    for i in range(len(lista)):
        numero = int(input("Ingrese un numero para su funcion: "))
        lista[i] = numero
        
        if lista[i] > num_max:
            num_max = lista[i]
            indice = [i]
    
    resultado = f"El numero max. se encontró en el indice = {indice}"
    
    return resultado


lista_aux = [0,0,0,0,0]

print(retornar_indice_valor_maximo(lista_aux))
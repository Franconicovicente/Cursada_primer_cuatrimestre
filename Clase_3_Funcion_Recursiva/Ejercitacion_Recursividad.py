'''
Ejercitación Clase 5 (Recursividad)

'''

# 1. Realizar una función recursiva que calcule la suma de los primeros números naturales:

def sumar_naturales (numero:int) -> int:
    '''
    El usuario pone dos numeros, y si son mayores que 0 se suman
    Se retorna el resultado
    '''
    if numero > 0:
        resultado = numero + sumar_naturales(numero - 1)

    else:
        resultado = 0
    

    return resultado

numero_uno = int(input("Ingrese su numero natural:"))
print(sumar_naturales(numero_uno))

# # 2. Realizar una función recursiva que calcule la potencia de un número:

def calcular_potencia (base:int , exponente:int) -> int:
    '''
    El usuario da un numero de base y un exponente
    Si el exponente no es 0, hace la potencia y muestra un mensaje
    retorna el resultado
    '''
    if exponente == 0:
        resultado = 1

    else:
        resultado = base * calcular_potencia(base, exponente - 1)

    return resultado

numero_base = int(input("Ingrese su numero de base:"))
numero_exponente = int(input("Ingrese su exponente:"))
resultado = calcular_potencia(numero_base, numero_exponente)

print(f"Base {numero_base} elevado a {numero_exponente} = {resultado}")


# 3. Realizar una función para calcular el número de Fibonacci (investigar que es) de un número ingresado por consola. La función deberá seguir el siguiente prototipo:
# La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de los dos anteriores:

def calcular_fibonacci (numero:int) -> int:
    if numero == 0:
        return 0
    elif numero == 1:
        return 1    
    else:
        resultado = calcular_fibonacci(numero - 1) + calcular_fibonacci (numero - 2)
        
    return resultado

numero = int(input("Ingrese un numero: "))

resultado = calcular_fibonacci(numero)

print(f"El numero Fibonacci es {resultado}")


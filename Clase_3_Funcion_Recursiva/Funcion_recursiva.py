# def funcion_recursiva(repetir):
#     retorno = 1

#     print(repetir)

#     if repetir > 1:
#         retorno = funcion_recursiva(repetir - 1) #RECURSIVIDAD, LA FUNCION SE LLAMA A SI MISMA

#     return retorno

# numero_a = int(input("Ingrese un numero:"))
# funcion_recursiva(numero_a)


def calcular_factorial (numero:int) -> int:
    '''
    Funcion que calcula si un numero es factorial 
    Recibe un numero entero positivo 
    Retorna el resultado de ese factorial
    '''
    if numero > 1:
        resultado = numero * calcular_factorial(numero - 1)
        #Aca hay que hacer algoritmo recursivo
    elif numero < 0:
        return "Solo se puede ingresar numeros positivos"
    else:
        resultado = 1 #Por defecto el factorial de 0 y 1 es 1.
        #No haria falta un algoritmo recursivo

    return resultado

numero_a = int(input("Ingrese un numero:"))
factorial = calcular_factorial(numero_a)
print(f"El factorial de {numero_a} es {factorial}")
'''
TAREA. 

Realizar una función que me permita sumar dos números de las cuatro maneras siguientes.

Una función sumar1 que reciba dos números y retorne el resultado
Una función sumar2 que reciba dos números y no retorne nada (o sea que la función se encargue de mostrar el resultado)
Una función sumar3 que no reciba nada y se encargue de pedir dos números y retornar el resultado
Una función sumar4 que no reciba nada y no retorne nada, por ende se va encargar de pedir los numeros y de mostrar el resultado.

'''
# Una función sumar1 que reciba dos números y retorne el resultado


# def sumar_1 (numero_a:float, numero_b:float) -> float:
#     '''
#     El usuario pone dos numeros y retorna el resultado
#     '''
#     resultado = numero_a + numero_b
#     return resultado

# numero_uno = float(input("Ingrese el primer numero:"))
# numero_dos = float(input("Ingrese el segundo numero:"))

# print(sumar_1(numero_uno, numero_dos))

# Una función sumar2 que reciba dos números y no retorne nada (o sea que la función se encargue de mostrar el resultado)

# def sumar_2 (numero_a:int, numero_b:int) -> int:
#     '''
#     El usuario ingresa dos numeros, y la funcion se encarga de mostrar el resultado
#     '''
#     resultado = numero_a + numero_b
#     print(resultado)

# numero_uno = int(input("Ingrese un numero:"))
# numero_dos = int(input("Ingrese un numero:"))
# sumar_2(numero_uno, numero_dos)



# Una función sumar3 que no reciba nada y se encargue de pedir dos números y retornar el resultado

# def sumar_3 () -> int: 
#     '''
#     No recibe numeros, pide dos numeros al usuario y los suma
#     retorna el resultado
#     '''

#     numero_uno = int(input("Ingrese su numero:"))
#     numero_dos = int(input("Ingrese su numero:"))
#     resultado = numero_uno + numero_dos
#     return resultado

# suma = sumar_3()
# print(suma)

# Una función sumar4 que no reciba nada y no retorne nada, por ende se va encargar de pedir los numeros y de mostrar el resultado.

def sumar4 () -> int:
    '''
    
    '''
    numero_a = int(input("Ingrese un numero:"))
    numero_b = int(input("Ingrese un numero:"))
    resultado = numero_a + numero_b
    print(resultado)

sumar4()

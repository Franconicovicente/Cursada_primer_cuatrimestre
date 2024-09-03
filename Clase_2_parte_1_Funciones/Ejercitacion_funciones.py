'''
1.Crear una función que reciba dos números (acumulador y contador) y calcule el promedio, en caso de que haya división por cero imprimir un mensaje de error.

2.Crear una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.

3.Crear una función que verifique si un número es par o no, devuelve True si es par, y False si es impar

4.Crear una función que verifique si un primo o no, devuelve True si es primo, False si no lo es

5.Crear una función qué encuentre el máximo entre tres números. Debe aceptar tres argumentos y retornar el número más grande.

6.Crear una función qué encuentre el mínimo entre tres números. Debe aceptar tres argumentos y retornar el número más chico.

7. Crear una función qué se encargue de dividir dos números, la misma debe recibir como parámetro dos números y retornar el resultado. Validar división por cero.

8. Crear una función qué se encargue de multiplicar dos números, la misma debe recibir como parámetro dos números y retornar el resultado.
'''

#1.Crear una función que reciba dos números los divida y calcule el promedio, en caso de que haya división por cero imprimir un mensaje de error.

# def promedio (numero_a:float, numero_b:float) -> float:
#     '''
#     El usuario ingresa dos numeros.
#     Se suman esos dos numeros y se los divide por dos para calcular el promedio 
#     Se redondea a 2 cifras despues de la coma
#     ''' 
#     try:
#         resultado_promedio = round((numero_a / numero_b) / 2, 2)
#         return resultado_promedio
#     except ZeroDivisionError:
#         return "No es posible dividir por cero"
    
# numero_uno = float(input("Ingrese numero 1:"))
# numero_dos = float(input("Ingrese numero 2:"))

# resultado = promedio(numero_uno, numero_dos)

# print(f"El resultado del promedio entre la division de {numero_uno} y {numero_dos} es {resultado}")

#2.Crear una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.

# def calcular_area_rectangulo (base:float, altura:float) -> float:
#     '''
#     El usuario ingresa dos numeros, la base y la altura
#     Se multiplican esos numeros, para saber el area del rectangulo y retorna el área
#     '''
#     resultado_area_rectangulo = base * altura
#     return resultado_area_rectangulo

# base_usuario = float(input("Ingrese el numero de la base:"))
# altura_usuario = float(input("Ingrese el numero de la altura:"))

# resultado = calcular_area_rectangulo(base_usuario, altura_usuario)

# print(f"El resultado del area del rectangulo con una base de {base_usuario} y con una altura de {altura_usuario} es de {resultado}")

# 3.Crear una función que verifique si un número es par o no, devuelve True si es par, y False si es impar

# def verificar_numero_par (numero_a : int) -> int:
#     '''
#     Le pide un numero al usuario
#     y si su resto entre 2 es 0, es par y devuelve true
#     ''' 
#     verificacion_numero_par = numero_a % 2 == 0
#     return verificacion_numero_par



# numero_uno = float(input("Ingrese su numero:"))
# resultado = verificar_numero_par(numero_uno)
# print(resultado)


# 4.Crear una función que verifique si un primo o no, devuelve True si es primo, False si no lo es
# def verificar_primo (numero_a : int) -> int:
#     '''
    
#     '''
#     for i in range(2, numero_a, 1):
#         if numero_a % i == 0:
#             return False
#     return True

# numero_primo = int(input("Ingrese su numero:"))
# print(verificar_primo(numero_primo))

# 5.Crear una función qué encuentre el máximo entre tres números. Debe aceptar tres argumentos y retornar el número más grande.

# def encontrar_el_maximo (numero_a : float, numero_b : float, numero_c : float) -> float:
#     '''
    
#     '''
#     if numero_a > numero_b and numero_a > numero_c:
#         return numero_a
#     elif numero_b > numero_c:
#         return numero_b
#     else:
#         return numero_c
    
# numero_uno = float(input("Ingrese el primer numero:"))
# numero_dos = float(input("Ingrese el segundo numero:"))
# numero_tres = float(input("Ingrese el tercer numero:"))

# resultado = encontrar_el_maximo(numero_uno, numero_dos, numero_tres)

# print(resultado)

# 6.Crear una función qué encuentre el mínimo entre tres números. Debe aceptar tres argumentos y retornar el número más chico.

# def encontrar_el_minimo (numero_a:float, numero_b:float, numero_c:float) -> float:
#     '''
    
#     '''
#     if numero_a < numero_b and numero_a < numero_c:
#         return numero_a
#     elif numero_b < numero_c:
#         return numero_b
#     else: 
#         return numero_c
    
# numero_uno = float(input("Ingrese numero uno:"))
# numero_dos = float(input("Ingrese numero dos:"))
# numero_tres = float(input("Ingrese numero tres:"))

# resultado = encontrar_el_minimo(numero_uno, numero_dos, numero_tres)
# print(resultado)

# 7. Crear una función qué se encargue de dividir dos números, la misma debe recibir como parámetro dos números y retornar el resultado. Validar división por cero.

# def dividir_numeros (numero_a:int, numero_b:int) -> float:
#     '''
#     El usuario ingresa dos numeros, y se dividen
#     devolviendo el valor, y si es 0, informa que no se puede dividir por 0
#     ''' 
#     try:
#         resultado_division = round(numero_a / numero_b, 2)
#         return resultado_division
#     except ZeroDivisionError:
#         return "No se puede dividir por cero"

# numero_uno = int(input("Ingrese el primer numero:"))
# numero_dos = int(input("Ingrese el segundo numero:"))

# print(dividir_numeros(numero_uno, numero_dos))

# 8. Crear una función qué se encargue de multiplicar dos números, la misma debe recibir como parámetro dos números y retornar el resultado.

# def multiplicar_numeros (numero_a:float, numero_b:float) -> float:
#     '''
    
#     '''
#     resultado = numero_a * numero_b
#     return resultado

# numero_uno = float(input("Ingresa el primer numero:"))
# numero_dos = float(input("Ingresa el segundo numero:"))

# print(multiplicar_numeros(numero_uno, numero_dos))

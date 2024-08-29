'''
Ejercitación Clase 2 (Resolver con for)

1.Mostrar números ascendentes del 1 al 10

2.Mostrar números descendentes del 10 al 1

3.Ingresar dos números mostrar desde el primer número hasta el segundo que ingresaron de manera ascendente, en caso de que el primer número sea mayor al segundo mostrarlos en orden descendente, si los números son iguales, mostrar sólo ese número.
Por ejemplo: Si ingresaron 5 como primer número y 7 como segundo mostrar (5-6-7), si el primer número que ingresaron es 7 y el segundo un 5 mostrar (7-6-5)

4.Se ingresan un máximo de 5 números o hasta que el usuario ingrese el número 0. Mostrar la suma y promedio de los mismos.

5.Mostrar todos los números pares entre el 1 hasta el 100 (sin usar condiciones lógicas)

6.Ingresar un número. Determinar si el número es primo o no.

7.Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

8. Ingresar un número y mostrar la tabla de multiplicar de ese número. 

Por ejemplo si se ingresa el numero 3:
3 x 0 = 0 
3 x 1  = 3
3 x 2 = 6
3 x 3  = 9
'''
#1.Mostrar números ascendentes del 1 al 10

for i in range (1, 11, 1): 
    print (i)

# 2.Mostrar números descendentes del 10 al 1

for i in range (10, 0, -1): 
    print (i)

# 3.Ingresar dos números mostrar desde el primer número hasta el segundo que ingresaron de manera ascendente, en caso de que el primer número sea mayor al segundo mostrarlos en orden descendente, si los números son iguales, mostrar sólo ese número.
# Por ejemplo: Si ingresaron 5 como primer número y 7 como segundo mostrar (5-6-7), si el primer número que ingresaron es 7 y el segundo un 5 mostrar (7-6-5)

primer_numero = input("Primer numero:")
primer_numero = int(primer_numero)

segundo_numero = input("Segundo numero:")
segundo_numero = int(segundo_numero)

for i in range (primer_numero, segundo_numero+1):
    print (i)

if primer_numero > segundo_numero:
    for i in range (primer_numero, segundo_numero-1, -1):
        print (i)

elif primer_numero == segundo_numero:
    print(F"El numero al ser igual es: {primer_numero}")

# 4.Se ingresan un máximo de 5 números o hasta que el usuario ingrese el número 0. Mostrar la suma y promedio de los mismos.

acumulador_numeros = 0
contador = 0

for i in range(5):
    numero_1 = input("Inserte numero:")
    numero_1 = int(numero_1)
    acumulador_numeros += numero_1
    contador += 1

    if numero_1 == 0:
        break

if contador != 0:
    promedio_numeros = round(acumulador_numeros / contador, 2)
    print(f"El promedio de los numeros ingresados es: {promedio_numeros}")
    print(f"La suma de los numeros ingresados es: {acumulador_numeros}")
else:
    print("Error")

# 5.Mostrar todos los números pares entre el 2 hasta el 100 (sin usar condiciones lógicas)

for i in range (2, 101, 2):
    print (i, end= " ")             # END = " " ----> HACE ESPACIOS EN EL PRINT.

# 6.Ingresar un número. Determinar si el número es primo o no.

numero = int(input("Ingrese un numero:")) # 12

bandera = True

for i in range(2, numero, 1): 

    
    if numero % i == 0:
        print(f"{numero} / {i} da resultado entero")
        bandera = False 
        break 

if bandera == True:
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo") 

# 7.Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.
numero = int(input("Ingrese un numero:"))
contador = 0

for i in range (2, numero+1):
    bandera = True
    for t in range (2, i):
        if i % t == 0:
            bandera = False
            break
        
    if bandera == True:
        contador += 1
        print(i)

print(f"Se encontraron un total de {contador} numeros primos")

# 8. Ingresar un número y mostrar la tabla de multiplicar de ese número. 

# Por ejemplo si se ingresa el numero 3:
# 3 x 0 = 0 
# 3 x 1  = 3
# 3 x 2 = 6
# 3 x 3  = 9

numero = int(input("Ingrese numero:"))
print(f"La tabla del {numero} es:")
for i in range (1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")









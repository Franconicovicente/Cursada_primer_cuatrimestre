matriz = [
        [4,7,1],
        [-2,5,9],
        [5,4,-4]
                ]

#Buscamos si el numero ingresado se encuentra o no en la matriz

numero_ingresado = int(input("Ingrese un numero: "))
bandera = False

for fil in range(len(matriz)):
    for col in range(len(matriz[fil])):
        # Hacemos la busqueda
        numero = matriz[fil][col]
        if numero_ingresado == numero:
            bandera = True  
            break
    if bandera == True:
        break

if bandera == True:
    print(f"El numero {numero_ingresado} se encontró en la matriz")
else:
    print(f"El numero {numero_ingresado} no se encontró en la matriz")


# Contar la cantidad de veces que un numero se repite

numero_ingresado = int(input("Ingrese un numero: "))
contador_numeros = 0

for fil in range(len(matriz)):
    for col in range(len(matriz[fil])):
        numero = matriz[fil][col]
        if numero == numero_ingresado:
            contador_numeros += 1

if contador_numeros == 1:
    print(f"El numero {numero_ingresado} se encuentra {contador_numeros} vez en la matriz")
elif contador_numeros > 1:
    print(f"El numero {numero_ingresado} se encuentra {contador_numeros} veces en la matriz")
else:
    print(f"El numero {numero_ingresado} no se encuentra en la matriz")


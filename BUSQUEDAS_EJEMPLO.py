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
lista_numeros = [0,0,0,0,0] #5 elementos con valor cero
seguir = "si"

while seguir == "si":
    #El indice donde lo guardo se lo pido al usuario
    indice = int(input("Ingrese el indice en donde quiere guardar el numero: "))

    while indice >= len(lista_numeros) or indice < 0:
        indice = int(input("Indice fuera de rango... \nReingrese el indice en donde quiere guardar el numero: "))        


    numero_auxiliar = int(input("Ingrese un numero: "))

    lista_numeros[indice] = numero_auxiliar

    seguir = input("Desea seguir cargando numeros? : ")

print(lista_numeros)

for i in range (len(lista_numeros)):
    print(f"Elemento con indice {i} = {lista_numeros[i]}")
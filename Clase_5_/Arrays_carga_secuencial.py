lista_numeros = [0,0,0,0,0] #5 elementos con valor cero

for i in range (len(lista_numeros)):
    #Pido el dato
    numero_auxiliar = int(input("Ingrese un numero: "))
    #variables auxiliares = variables que defino dentro del for y las uso solo como comodin asi le cargo valores a la lista 

    #guardo el numero en el array
    lista_numeros[i] = numero_auxiliar

print(lista_numeros)

for i in range (len(lista_numeros)):
    print(f"Elemento con indice {i} = {lista_numeros[i]}")
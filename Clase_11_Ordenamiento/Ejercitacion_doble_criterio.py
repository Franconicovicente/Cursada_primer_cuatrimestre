def mostrar_matriz(matriz:list)->None:
    '''
    
    '''
    if type(matriz) == list:
        for fil in range(len(matriz)):
        # For para las columnas
        # Cantidad columnas:
            for col in range(len(matriz[fil])):
                print(matriz[fil][col], end=" ")
            print("")
    else:
        print("No se ingresaron listas")
'''
ORDENAMIENTO DOBLE CRITERIO

1. Realizar una función que me permita ordenar una matriz de productos [nombre,precio,stock] por precio de mayor a menor y tomando como segundo criterio el stock (mayor a menor también)

2. Realizar una función que me permita ordenar una matriz de productos [nombre,precio,stock] por precio de mayor a menor y tomando como segundo criterio el nombre (alfabeticamente)

3. Realizar una función que me permita ordenar una matriz (cualquiera) por doble criterio , recibirá la matriz a ordenar, el índice de la columna del primer criterio, el índice de la columna del segundo criterio, el orden de ordenamiento (mayor o menor) (mismo para ambos criterios) 
Se puede usar la matriz del ejercicio 1 como ejemplo

4. Dada la función anterior mejorarla a tal nivel que me permita elegir un orden diferente para cada criterio, por ejemplo capaz quiero ordenar de mayor a menor el primer criterio y de menor a mayor el segundo criterio.
Usar de base lo desarrollado en el ejercicio 2, debería funcionar para resolver de la misma manera. El criterio del precio se ordenará de mayor a menor y el criterio del nombre alfabéticamente (menor a mayor)

'''
# 1. Realizar una función que me permita ordenar una matriz de productos [nombre,precio,stock] por precio de mayor a menor y tomando como segundo criterio el stock (mayor a menor también)
matriz_productos = [
    ["Coca Cola", 1000, 50],
    ["Pepsi", 800, 60],
    ["Fanta", 600, 70],
    ["Gatorade", 1500, 40],
    ["Monster", 3000, 60]
]

I_PRECIO = 1
I_STOCK = 2
I_NOMBRE = 0

def ordenar_matriz(matriz:list):
    '''
    
    '''
    for i in range(len(matriz) -1):
        for j in range(i+1,len(matriz)):
            if matriz[i][I_PRECIO] < matriz[j][I_PRECIO] or matriz[i][I_PRECIO] == matriz[j][I_PRECIO] and matriz[i][I_STOCK] < matriz[j][I_STOCK]:
                auxiliar = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = auxiliar
    
    return matriz


resultado = ordenar_matriz(matriz_productos)

# mostrar_matriz(resultado)

# 2. Realizar una función que me permita ordenar una matriz de productos [nombre,precio,stock] por precio de mayor a menor y tomando como segundo criterio el nombre (alfabeticamente)

def ordenar_matriz(matriz:list):
    '''
    
    '''
    for i in range(len(matriz) -1):
        for j in range(i+1,len(matriz)):
            if matriz[i][I_PRECIO] < matriz[j][I_PRECIO] and matriz[i][I_NOMBRE] > matriz[j][I_NOMBRE]:
                auxiliar = matriz[i]
                matriz[i] = matriz[j]
                matriz[j] = auxiliar
    
    return matriz


resultado = ordenar_matriz(matriz_productos)

# mostrar_matriz(resultado)

# 3. Realizar una función que me permita ordenar una matriz (cualquiera) por doble criterio , recibirá la matriz a ordenar, el índice de la columna del primer criterio, el índice de la columna del segundo criterio, el orden de ordenamiento (mayor o menor) (mismo para ambos criterios) 
# Se puede usar la matriz del ejercicio 1 como ejemplo

matriz_productos = [
    ["Coca Cola", 1000, 50],
    ["Pepsi", 800, 60],
    ["Fanta", 600, 70],
    ["Gatorade", 1500, 40],
    ["Monster", 3000, 60]
]
indice_1 = int(input("Que indice desea que sea su primer criterio: 0, 1 o 2: "))
indice_2 = int(input("Que indice desea que sea su segundo criterio: 0, 1 o 2: "))
while indice_2 == indice_1:
    indice_2 = int(input("ERROR, ingrese bien el indice: 0, 1 o 2: "))   
orden = input("Desea un ordenamiento de mayor o menor?: ")
def ordenar_matriz(matriz:list,indice_1:int,indice_2:int,orden:str):
    '''
    
    '''
    for i in range(len(matriz) -1 ):
        for j in range(i+1,len(matriz)):
            if orden == "mayor":
                if matriz[i][indice_1] < matriz[j][indice_1] or matriz[i][indice_1] == matriz[j][indice_2] and matriz[i][indice_1] < matriz[j][indice_2]:
                    auxiliar = matriz[i]
                    matriz[i] = matriz[j]
                    matriz[j] = auxiliar
            elif orden == "menor":
                if matriz[i][indice_1] > matriz[j][indice_1] or matriz[i][indice_1] == matriz[j][indice_2] and matriz[i][indice_1] > matriz[j][indice_2]:
                    auxiliar = matriz[i]
                    matriz[i] = matriz[j]
                    matriz[j] = auxiliar
    
    return matriz

resultado = ordenar_matriz(matriz_productos,indice_1,indice_2,orden)

# mostrar_matriz(resultado)

# 4. Dada la función anterior mejorarla a tal nivel que me permita elegir un orden diferente para cada criterio, por ejemplo capaz quiero ordenar de mayor a menor el primer criterio y de menor a mayor el segundo criterio.
# Usar de base lo desarrollado en el ejercicio 2, debería funcionar para resolver de la misma manera. El criterio del precio se ordenará de mayor a menor y el criterio del nombre alfabéticamente (menor a mayor)
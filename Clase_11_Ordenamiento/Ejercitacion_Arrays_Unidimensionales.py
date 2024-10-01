'''
ARRAYS UNIDIMENSIONALES

1.Realizar una función que ordene una lista de enteros de forma ascendente (menor a mayor) , la misma debería devolver False en caso de que se ya se encuentre ordenada. True en caso contrario

2.Realizar una función que ordene una lista de enteros de forma descendente (mayor a menor) , la misma debería devolver False en caso de que se ya se encuentre ordenada. True en caso contrario

3.Realizar una función que ordene una lista de enteros en orden ascendente o descendente dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad de intercambios que se realizaron.

4.Realizar una función que ordene una lista de nombres de la alfabéticamente (A-Z) o viceversa (Z-A) dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad de cambios que se realizaron. 
Investigar cómo comparar str en alfabéticamente en python.

5. Similar a la función anterior, se debe realizar otra que ordene una lista de nombres por su largo, de manera ascendente o descendente, la función debe retornar la cantidad de cambios que se realizaron.

'''

# 1.Realizar una función que ordene una lista de enteros de forma ascendente (menor a mayor) , la misma debería devolver False en caso de que se ya se encuentre ordenada. True en caso contrario

lista = [3,7,4,2]
lista_ordenada = [2,3,4,7]

def ordenar_lista_menor_a_mayor(lista:list) -> list:
    '''
    Ordena numeros de forma ascendente. Si está ordenada devuelve False, Si esta desornedada devuelve True
    '''
    bandera = False
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                bandera = True
                num_aux = lista[i]
                lista[i] = lista[j]
                lista[j] = num_aux

    return bandera
    

print(ordenar_lista_menor_a_mayor(lista_ordenada))
print(ordenar_lista_menor_a_mayor(lista))

# 2.Realizar una función que ordene una lista de enteros de forma descendente (mayor a menor) , la misma debería devolver False en caso de que se ya se encuentre ordenada. True en caso contrario

def ordenar_lista_menor_a_mayor(lista:list) -> list:
    '''
    Ordena numeros de forma descendente. Si está ordenada devuelve False, Si esta desornedada devuelve True
    '''
    bandera = False
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i] < lista[j]:
                bandera = True
                num_aux = lista[i]
                lista[i] = lista[j]
                lista[j] = num_aux

    return bandera
    

print(ordenar_lista_menor_a_mayor(lista))
print(ordenar_lista_menor_a_mayor(lista_ordenada))

# 3.Realizar una función que ordene una lista de enteros en orden ascendente o descendente dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad de intercambios que se realizaron.

orden = int(input("Ingrese numero 1 para calcular de forma ascendente.\nIngrese numero 2 para calcular de forma descendente.\nSu respuesta: "))
def ordenar_enteros(lista:list, orden):
    '''
    Calcula el total de intercambios que hubo en la lista, dependiendo la opcion que haya elegido el usuario
    1 para calcular de forma ascendente y 2 para calcular de forma descendente.
    Devuelve el contador de los intercambios
    '''
    contador_intercambios = 0
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if orden == 1:
                if lista[i] > lista[j]:
                    num_aux = lista[i] 
                    lista[i] = lista[j]
                    lista[j] = num_aux
                    contador_intercambios += 1
            elif orden == 2:
                if lista[i] < lista[j]:
                    num_aux = lista[i] 
                    lista[i] = lista[j]
                    lista[j] = num_aux
                    contador_intercambios += 1
    
    return contador_intercambios

lista = [3,7,4,2]

print(f"Se realizaron un total de {ordenar_enteros(lista, orden)} intercambios")

# 4.Realizar una función que ordene una lista de nombres de la alfabéticamente (A-Z) o viceversa (Z-A) dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad de cambios que se realizaron. 
# Investigar cómo comparar str en alfabéticamente en python.


orden = int(input("Ingrese numero 1 para calcular de la A-Z.\nIngrese numero 2 para calcular de la Z-A.\nSu respuesta: "))
def ordenar_nombres(lista:list, orden):
    '''
    Calcula el total de intercambios que hubo en la lista, dependiendo la opcion que haya elegido el usuario
    1 para calcular de A-Z y 2 para calcular de Z-A.
    Devuelve el contador de los intercambios
    '''
    contador_intercambios = 0
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if orden == 1:
                if lista[i] > lista[j]:
                    num_aux = lista[i] 
                    lista[i] = lista[j]
                    lista[j] = num_aux
                    contador_intercambios += 1
            elif orden == 2:
                if lista[i] < lista[j]:
                    num_aux = lista[i] 
                    lista[i] = lista[j]
                    lista[j] = num_aux
                    contador_intercambios += 1
    
    return contador_intercambios


nombres = ["Abril", "Morena", "Tadeo"]

print(ordenar_nombres(nombres, orden))


# 5. Similar a la función anterior, se debe realizar otra que ordene una lista de nombres por su largo, de manera ascendente o descendente, la función debe retornar la cantidad de cambios que se realizaron.

orden = int(input("Ingrese numero 1 para calcular de menor a mayor longitud.\nIngrese numero 2 para calcular de mayor a menor longitud.\nSu respuesta: "))
def ordenar_nombres(lista:list, orden):
    '''
    Calcula el total de intercambios que hubo en la lista, dependiendo la opcion que haya elegido el usuario
    1 para calcular el largo de menor a mayor y 2 para calcular el largo de mayor a menor
    Devuelve el contador de los intercambios
    '''
    contador_intercambios = 0
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if orden == 1:
                if len(lista[i]) > len(lista[j]):
                    num_aux = lista[i] 
                    lista[i] = lista[j]
                    lista[j] = num_aux
                    contador_intercambios += 1
            elif orden == 2:
                if len(lista[i]) < len(lista[j]):
                    num_aux = lista[i] 
                    lista[i] = lista[j]
                    lista[j] = num_aux
                    contador_intercambios += 1
    
    return contador_intercambios


nombres = ["Abril", "Morena", "Morenita"]

print(ordenar_nombres(nombres, orden))
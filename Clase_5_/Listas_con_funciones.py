def mi_funcion (lista_numeros):
    lista_numeros[0] = 5
    lista_numeros[4] = 1
#no hace falta return si uso lista
#si retorno una lista, si la misma fue creada dentro de la funcion

lista_numeros = [1,2,3,4,5]
print(f"Antes de la funcion : {lista_numeros}" )
mi_funcion(lista_numeros)

print(f"Despues de la funcion : {lista_numeros}")
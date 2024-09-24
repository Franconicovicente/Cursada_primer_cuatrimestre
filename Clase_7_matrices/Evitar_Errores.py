def mi_funcion(matriz_a:list,matriz_b:list) -> list:
    if type(matriz_a) == list and type(matriz_b) == list:
        print("Es lista")
        retorno = [1,2,3]
        #ACA ESCRIBO TODO EL CODIGO
    else:
        print("No es lista")
        retorno = []
    
    return retorno

matriz = [
        [3,4,5]
                ]
mi_funcion(matriz,matriz) # --> Es lista
mi_funcion(matriz,30) # --> No es lista


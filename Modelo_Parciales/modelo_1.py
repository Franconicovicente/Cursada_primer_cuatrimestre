'''
Una competencia de baile califica a los mejores bailarines de la ciudad.
De 10 participantes los tres jurados fueron calificando al mejor bailarín o bailarina de la
ciudad
Cada bailarín o bailarina se los identifica con un número que comienza del 1 hasta el 10
Realizar (en lo posible) un menú de opciones:
1
1. Calificar Bailarines: Se realiza una carga secuencial de todas las notas que eligió
cada jurado de cada uno de los bailarines.
2. Mostrar Notas: Muestra en un lindo formato los siguientes datos:
Nro Participante, Nota Jurado 1,Nota Jurado 2,Nota Jurado 3,Nota Promedio:
3. Ordenar Bailarines jurado 2: Ordena a los participantes por la mejor nota que les
puso el jurado 2.
4. Triple 7: Encontrar y mostrar a los participantes que tengan un 7 de nota en todos los
jurados. En caso de no haber indicar que no existen.
5. Jurado malo: Muestra a todos los bailarines que fueron aplazados por el jurado 3
(Aplazo seria nota menor 4)
6. TOP 3: Muestra el top 3 de los participantes con mayor nota promedio.
7. Verificar Ganador: El ganador de la competencia se verifica con el bailarín/bailarina
que tenga mayor nota promedio. En caso de empate se tendrá en cuenta la nota del
jurado 1. En caso de igualdad nuevamente se muestran todos los ganadores que
hayan resultado.
'''

def inicializar_matriz(cant_filas:list,cant_columnas:list,valor_inicial:any)-> list:

    
    '''
    
    '''
    matriz = []
    for fil in range(cant_filas):
        fila =  [valor_inicial] * cant_columnas
        matriz += [fila]
    return matriz


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



# 1. Calificar Bailarines: Se realiza una carga secuencial de todas las notas que eligió
# cada jurado de cada uno de los bailarines.


lista_bailarines = inicializar_matriz(10,3,0)
# mostrar_matriz(lista_bailarines)

def calificar_bailarines (lista_bailarines:list):
    '''
    
    '''
    for fil in range(len(lista_bailarines)):
        for i in range(len(lista_bailarines[0])):
            print(f"Jurado NRO: {i+1}")
            nota = int(input(f"Introduzca nota para el bailarin Nro {fil+1} = "))
            lista_bailarines[fil][i] = nota

    return lista_bailarines
calificar_bailarines(lista_bailarines)




# 2. Mostrar Notas: Muestra en un lindo formato los siguientes datos:
# Nro Participante, Nota Jurado 1,Nota Jurado 2,Nota Jurado 3,Nota Promedio:

def mostrar_notas_bailarines(lista:list):
    '''
    
    '''
    
    for i in range(len(lista)):
        acumulador_nota = 0
        notas_jurado = lista[i]
        for nota in notas_jurado:
            acumulador_nota += nota

        promedio_notas = acumulador_nota / len(notas_jurado)
        

        print(f"Nro participante = {i+1}\nNota jurado 1 = {lista[i][0]}\nNota jurado 2 = {lista[i][1]}\nNota jurado 3 = {lista[i][2]}\nNota promedio = {promedio_notas}")
        print("=" * 40)



mostrar_notas_bailarines(lista_bailarines)

# 3. Ordenar Bailarines jurado 2: Ordena a los participantes por la mejor nota que les
# puso el jurado 2.

def ordenar_mejor_nota_jurado_2 (lista:list):
    '''
    
    '''
    for i in range(len(lista) - 1):
        for j in range(i+1, len(lista)):
            if lista[i][1] < lista[j][1]:
                nota_aux = lista[i]
                lista[i] = lista[j]
                lista[j] = nota_aux
    
    return lista
ordenar_mejor_nota_jurado_2(lista_bailarines)

# 4. Triple 7: Encontrar y mostrar a los participantes que tengan un 7 de nota en todos los
# jurados. En caso de no haber indicar que no existen.

def buscar_nota_7 (lista:list):
    '''
    
    '''
    bandera_bailarines = False
    for fil in range(len(lista)):
        for col in range(len(lista[fil])):
            if lista[fil][0] == 7 and lista[fil][1] == 7 and lista[fil][2] == 7:
                print(f"Nro de participante que tiene un triple 7: {fil+1}")
                bandera_bailarines = True
                break
    
    if bandera_bailarines == False:
        print("No se encontraron bailarines con un triple 7")


buscar_nota_7(lista_bailarines)

# 5. Jurado malo: Muestra a todos los bailarines que fueron aplazados por el jurado 3
# (Aplazo seria nota menor 4)

def mostrar_aplazados_por_jurado_3(lista:list):
    '''
    
    '''
    for i in range(len(lista)):
        if lista[i][2] < 4:
            print(f"Bailarines aplazados por el jurado NRO 3: Bailarin numero: {i+1}")




mostrar_aplazados_por_jurado_3(lista_bailarines)

# 6. TOP 3: Muestra el top 3 de los participantes con mayor nota promedio.

lista_promedios = []
def mostrar_top_3_mayor_nota_promedio(lista:list):
    '''
    
    '''
    
    for i in range(len(lista)):
        acumulador_nota = 0
        notas_jurado = lista[i]
        for notas in notas_jurado:
            acumulador_nota += notas

        promedio = round(acumulador_nota / len(notas_jurado), 1)

        lista_promedios.append((i+1, promedio))


    for i in range(len(lista_promedios)-1):
        for j in range(i+1, len(lista_promedios)):
            if lista_promedios[i][1] < lista_promedios[j][1]:
                promedio_aux = lista_promedios[i]

                lista_promedios[i] = lista_promedios[j]
                lista_promedios[j] = promedio_aux

    return lista_promedios

print(mostrar_top_3_mayor_nota_promedio(lista_bailarines))
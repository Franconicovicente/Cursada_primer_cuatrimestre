#ARRAYS O ARREGLOS = SON ESTRUCTURAS DE DATOS QUE NOS PERMITE ORGANIZAR UN CONJUNTO DE ELEMENTOS QUE LOS VAMOS A REFERENCIAR
#O A CLASIFICAR BAJO UN MISMO NOMBRE


# UNIDIMENSIONALES ---> LOS ELEMENTOS SE ORGANIZAN UNO TRAS OTRO EN UNA SOLA DIMENSIÓN --> (VECTORES)

# V -> [5,2,1,3,9]

#BIDIMENSIONALES ---> LOS ELEMENTOS SE ORGANIZAN UNO TRAS OTRO PERO EN DOS DIMENSIONES --> (MATRICES)

#PARA QUE UN ARRAY DEFINA A CADA UNO DE ESTOS ELEMENTOS, LOS VA A ORGANIZAR ADELANTE DE UN INDICE

# EN PYTHON EXPRESAMOS LOS ARREGLADOS CON UN TIPO DE DATO LLAMADO LISTA (LIST)



# mi_arreglo = []
# o
# mi_Arreglo = list()

# mi_arreglo = [5, "Hola", 3.14]

mi_arreglo = [1,5,9,2,5]

# print(mi_arreglo)


# #El primer elemento de mi array se lo define con el indice 0
# #El ultimo elemento de mi array se lo define con el indice 
# # (cantidad de elementos - 1)

# #Accedo solo al primer elemento
# print(mi_arreglo[0])
# #Accedo al segundo
# print(mi_arreglo[1])
# #Acceder solo al ultimo
# print(mi_arreglo[4])


# #Acceder solo al ultimo
# cantidad_elementos = len(mi_arreglo)
# print(f"El arreglo tiene {cantidad_elementos} elementos")
# print(mi_arreglo[cantidad_elementos - 1])


# Mostrar toda la info. de un array:

# for i in range (cantidad_elementos):
#     print(mi_arreglo[i])

# for i in range(len(mi_arreglo)):
#     print (mi_arreglo[i])

# for numero in mi_arreglo:
#     print(numero)

#Tambien podemos hacer operaciones con mi array
#ejemplo = acumular elementos y calcular el promedio

suma_elementos = 0

for numero in mi_arreglo:
    suma_elementos += numero

promedio_elementos = suma_elementos / len(mi_arreglo)

print(f"La suma de los elementos de mi array = {suma_elementos}")
print(f"El promedio de los elementos de mi array = {promedio_elementos}")
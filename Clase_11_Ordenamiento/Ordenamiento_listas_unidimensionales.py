# En clase vamos a ver el ordenamiento por burbujeo ya que es uno de los más sencillos para comenzar. (se evalua ese en el parcial)


array_numeros = [5,3,1,7,9]


print("Antes de ordenar: ")
print(array_numeros)
print("")

#De menor a mayor

# Primer version

#Es el for de los numeros a la izquierda
# for i in range(len(array_numeros)-1):
#Es el for de los numeros a la derecha
    # for j in range(i+1,len(array_numeros)):
        # Intercambio (numero_izquierda > numero_derecha)
        # numero_izquierda = array_numeros[i]
        # numero_derecha = array_numeros[j]
        # if numero_izquierda > numero_derecha:
        #     array_numeros[i] = numero_derecha
        #     array_numeros[j] = numero_izquierda

# Segunda version --> Version final. (Siempre esta expresado de esta manera)

#Es el for de los numeros a la izquierda
for i in range(len(array_numeros)-1):
# Es el for de los numeros a la derecha
    for j in range(i+1,len(array_numeros)):
        # Intercambio (numero_izquierda > numero_derecha)
        if array_numeros[i] > array_numeros[j]:
            numero_izquierda = array_numeros[i] # Numero izquierda = numero auxiliar.

            array_numeros[i] = array_numeros[j]
            array_numeros[j] = numero_izquierda

# De mayor a menor

for i in range(len(array_numeros)-1):
    for j in range(i+1,len(array_numeros)):
        if array_numeros[i] < array_numeros[j]:
            numero_aux = array_numeros[i]

            array_numeros[i] = array_numeros[j]
            array_numeros[j] = numero_aux



print("Despues de ordenar: ")
print(array_numeros)
print("")
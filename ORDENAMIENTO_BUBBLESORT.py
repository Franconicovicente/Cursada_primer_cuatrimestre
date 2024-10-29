array_numeros = [5,3,1,7,9]
for i in range(len(array_numeros)-1):
    for j in range(i+1,len(array_numeros)):
        if array_numeros[i] < array_numeros[j]:
            numero_aux = array_numeros[i]

            array_numeros[i] = array_numeros[j]
            array_numeros[j] = numero_aux
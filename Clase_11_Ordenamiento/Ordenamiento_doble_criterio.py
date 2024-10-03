#Imaginemos que tenemos la siguiente matriz
#La queremos ordenar por Apellido 
#En caso de que los apellidos sean iguales tenemos que aplicar otro criterio de ordenamiento (Por nombre)

matriz_nombres = [
    ["Mariano","Fernandez"],
    ["Agustin","Fernandez"],
    ["Juan","Gonzalez"],
    ["Daniela","Fernandez"],
    ["Ana","Gonzalez"]
]

I_NOMBRE = 0
I_APELLIDO = 1

for i in range(len(matriz_nombres) - 1):
    for j in range(i+1,len(matriz_nombres)):
        if (matriz_nombres[i][I_APELLIDO] > matriz_nombres[j][I_APELLIDO]) or ( matriz_nombres[i][I_APELLIDO] == matriz_nombres[j][I_APELLIDO] and matriz_nombres[i][I_NOMBRE] > matriz_nombres[j][I_NOMBRE]) :
            auxiliar = matriz_nombres[i]
            matriz_nombres[i] = matriz_nombres[j]
            matriz_nombres[j] = auxiliar
            #matriz_nombres[i],matriz_nombres[j] = matriz_nombres[j],matriz_nombres[i] -> SOLO FUNCIONA EN PYTHON
        #Si los apellidos son IGUALES (tenemos que aplicar un doble criterio)
        # elif matriz_nombres[i][I_APELLIDO] == matriz_nombres[j][I_APELLIDO]:
        #     #Se aplica el doble criterio
        #     if matriz_nombres[i][I_NOMBRE] > matriz_nombres[j][I_NOMBRE]:
        #         auxiliar = matriz_nombres[i]
        #         matriz_nombres[i] = matriz_nombres[j]
        #         matriz_nombres[j] = auxiliar                
            

for i in range(len(matriz_nombres)):
    print(f"Nombre: {matriz_nombres[i][I_NOMBRE]}")
    print(f"Apellido: {matriz_nombres[i][I_APELLIDO]}\n")
    
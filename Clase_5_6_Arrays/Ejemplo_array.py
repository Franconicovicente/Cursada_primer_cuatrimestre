#Necesitamos un sistema que permita cargar las notas de 5 alumnos del 1 al 10

#Necesitamos mostrar la suma y el promedio de esas notas

#Necesitamos mostrar las notas cargadas

notas_alumnos = [0, 0, 0, 0, 0]
suma_notas = 0

for i in range (len(notas_alumnos)):
    nota_auxiliar = int(input("Ingrese una nota entre el 1 al 10: "))
    while nota_auxiliar > 10 or nota_auxiliar < 1:
        nota_auxiliar = int(input("Error\nIngrese una nota entre el 1 al 10: "))

    notas_alumnos[i] = nota_auxiliar
    suma_notas += nota_auxiliar

promedio_notas = suma_notas / len(notas_alumnos)
print(f"La suma de las notas es = {suma_notas} \nSu promedio es = {promedio_notas} ")
print(notas_alumnos)

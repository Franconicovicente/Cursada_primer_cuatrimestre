#TUPLAS -> Son una colección inmutable de datos, similares a la listas

#Declaracion

# mi_tupla = (1,3,5,7,9)
#mi_tupla[0] = 10 -> ERROR

#Acceso

# #Accedo al primer elemento
# print(mi_tupla[0])
# #Accedo al segundo elemento
# print(mi_tupla[1])
# #Accedo a todos los elementos
# print(mi_tupla)

# for i in range(len(mi_tupla)):
#     print(mi_tupla[i])
    
#DESEMPAQUETADO

mi_tupla = ("Mariano",3.14,21)

NOMBRE_CREADOR,NUMERO_PI,PORCENTAJE_IVA = mi_tupla

print(f"Nombre: {NOMBRE_CREADOR}")
print(f"PI: {NUMERO_PI}")
print(f"IVA: {PORCENTAJE_IVA}")
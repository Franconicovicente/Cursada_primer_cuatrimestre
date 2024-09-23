# #Una forma de organizar datos que puede ser de personas, productos, de usuarios, etc.
# #Cada uno de estos elementos se relacionan teniendo el mismo indice

lista_nombres = ["Mariano", "Renato", "German"]
lista_apellido = ["Fernandez", "Nani", "Scarafilo"]
lista_edad =  ["40", "50", "60"]
lista_legajo = [111111,222222,333333]

# # Toda la info de mariano --> está en el indice 0
# # Toda la info de renato  --> está en el indice 1
# # Toda la info de german --> está en el indice 2

# # Como muestro un array paralelo: 

for i in range(len(lista_nombres)): # da igual que lista elija, tienen la misma longitud ya que estoy haciendo el for con I.
    nombre_auxiliar = lista_nombres[i]
    apellido_auxiliar = lista_apellido[i]
    edad_auxiliar = lista_edad [i]
    legajo_auxiliar = lista_legajo[i]
    print(f"Nombre:{nombre_auxiliar}\nApellido:{apellido_auxiliar}\nEdad:{edad_auxiliar}\nLegajo:{legajo_auxiliar}\n")



# Como cargar info. de una persona a un array paralelo: 

# Quiero cargar 3 profes en mi sistema
lista_nombres = []
lista_apellido = []
lista_edad =  []
lista_legajo = []

for i in range(3):
    #CARGO LOS DATOS    
    nombre_aux = input("Ingrese el nombre: ")
    apellido_aux = input("Ingrese el apellido: ")
    edad_aux = input("Ingrese la edad: ")
    legajo_aux = input("Ingrese el legajo: ")
    print("Ingrese nuevos datos...")

    #GUARDO LOS DATOS EN LAS LISTAS
    lista_nombres.append(nombre_aux)
    lista_apellido.append(apellido_aux)
    lista_edad.append(edad_aux)
    lista_legajo.append(legajo_aux)

for i in range(len(lista_nombres)): # da igual que lista elija, tienen la misma longitud ya que estoy haciendo el for con I.
    nombre_auxiliar = lista_nombres[i]
    apellido_auxiliar = lista_apellido[i]
    edad_auxiliar = lista_edad [i]
    legajo_auxiliar = lista_legajo[i]
    print(f"Nombre:{nombre_auxiliar}\nApellido:{apellido_auxiliar}\nEdad:{edad_auxiliar}\nLegajo:{legajo_auxiliar}\n")

    



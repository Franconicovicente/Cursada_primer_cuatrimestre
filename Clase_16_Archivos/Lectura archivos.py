import os

#ARCHIVOS -> Nosotros podemos hacer operaciones de lectura o escritura con archivos

#Necesitamos acceder al archivo

#Creamos el archivo -> se guarda en la variable archivo un objeto file
#EJEMPLO RUTA RELATIVA

#archivo = open("archivo10.txt","r") ->Rompe si el archivo no existe
#archivo = open("/Users/marianofernandez/Desktop/Prog 1 python/ARCHIVOS/archivo.txt")

# if os.path.exists("archivo.txt"):
#     archivo = open("archivo.txt","r")
#     print("EL ARCHIVO EXISTE")
    
#     #METODO READ -> Lee todos los datos de mi archivo, podemos limitar la cantidad de bytes (caracteres a mostrar)
    
#     #texto = archivo.read() -> Leo toda la info de mi archivo
#     #texto = archivo.read(20) #-> Lee los primeros 20 bytes de mi archivo
#     #print(texto)
    
#     #METODO READLINE -> Lee una linea del archivo cada vez que se ejecuta
    
#     # print(archivo.readline(),end="") #Lee primer linea
#     # print(archivo.readline(),end="") #Lee segunda linea
#     # print(archivo.readline(),end="") #Lee tercer linea
#     # print(archivo.readline(),end="") #Se quedo sin lineas devuelve string vacio
    
#     #Readlines -> Devuelve una lista con todas las lineas de mi archivo
    
#     # lista_lineas = archivo.readlines()
#     # # print(lista_lineas)
#     # for linea in lista_lineas:
#     #     print(linea,end="")
    
#     #Alternativa a readlines -> No hace falta usar el el metodo readlines para recorrer un archivo.
    
#     for linea in archivo:
#         print(linea,end="")

#     #Una vez abierto el archivo, lo tengo que cerrar
#     archivo.close()
# else:
#     print("ERROR, EL ARCHIVO NO EXISTE")

#with -> abre el archivo y el interprete de python se encarga de cerrarlo automaticamente

if os.path.exists("archivo.txt"):
    with open("archivo.txt","r") as archivo:
        print(archivo.read())
        print(f"Dentro del with: {archivo.closed}")
    print(f"Despues del with: {archivo.closed}")
else:
    print("ERROR, EL ARCHIVO NO EXISTE")

#Ruta absoluta = La ruta completa de su archivo
# C:/archivos de programa/rockstar games/gta v/gtav.exe

#Ruta relativa = Es dentro estoy parado
#archivo.txt
#archivo/archivo_2.txt

#RUTA ABSOLUTA
#/Users/marianofernandez/Desktop/Prog 1 python/ARCHIVOS/archivo.txt

#RUTA RELATIVA
#archivo.txt

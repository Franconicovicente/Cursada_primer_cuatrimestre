import os
import json

# #dos tipos de archivos

# #csv -> Normalmente archivos que puedan ser abiertos en un excel, son separados por un separador, normalmente usamos la coma (,).
# #json -> Me permite crear un archivo fácil de exportar en cualquier lenguaje.

# #Un sistema de una facultad necesita cargar de un archivo una lista de estudiantes.

# #1.Leer csv -> Pasar del archivo a la lista de diccionarios
# #Parser -> Signfica conversión

# #Nombre, apellido, genero, nota final

def crear_diccionario_alumno(lista_valores:list) -> dict:
    mi_alumno = {}
    mi_alumno['nombre'] = lista_valores[0]
    mi_alumno['apellido'] = lista_valores[1]
    mi_alumno['genero'] = lista_valores[2]
    mi_alumno['nota_final'] = int(lista_valores[3])
    
    return mi_alumno

def leer_csv_alumnos(nombre_archivo:str,lista_alumnos:list) -> bool:
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r") as archivo:
            #Leo la primer linea, para ahorrarme la cabecera
            archivo.readline()#FALSA LECTURA
            for linea in archivo:
                linea_aux = linea.replace("\n","")
                lista_valores = linea_aux.split(",")     
                mi_alumno_aux = crear_diccionario_alumno(lista_valores)
                lista_alumnos.append(mi_alumno_aux)
            retorno = True
    else:
        retorno = False
        
    return retorno

# #2.Guardar csv -> Pasar de la lista de diccionarios al archivo .csv

def crear_cabecera(diccionario:dict,separador:str) -> str:
    lista_claves = list(diccionario.keys())
    cabecera = separador.join(lista_claves)
    
    return cabecera

def crear_dato_csv(diccionario:dict,separador:str) -> str:
    lista_valores = list(diccionario.values())
    #Convierto todo a str para evitar que rompa
    for i in range(len(lista_valores)):
        lista_valores[i] = str(lista_valores[i])
    dato = separador.join(lista_valores)

    return dato

def guardar_csv(nombre_archivo:str,lista:list) -> bool:
    if type(lista) == list and len(lista) > 0:
        cabecera = crear_cabecera(lista[0],",")
        with open(nombre_archivo,"w") as archivo:
            archivo.write(cabecera + "\n")
            for diccionario in lista:
                linea = crear_dato_csv(diccionario,",")
                archivo.write(linea + "\n")
        retorno = True
    else:
        retorno = False
    
    return retorno

# #3. Leer json

def leer_json(nombre_archivo:str,lista:list) -> bool:
    if os.path.exists(nombre_archivo):
        lista.clear()
        with open(nombre_archivo,"r") as archivo:
            lista.extend(json.load(archivo))
        retorno = True
    else:
        retorno = False
        
    return retorno
# #4. Guardar json

def generar_json(nombre_archivo:str,lista:list) -> bool:
    if type(lista) == list and len(lista) > 0:
        with open(nombre_archivo,"w") as archivo:
            json.dump(lista,archivo,indent=4)
        retorno = True
    else:
        retorno = False
    return retorno
        

def mostrar_diccionario(diccionario) -> None:
    for clave,valor in diccionario.items():
        print(f"{clave.title().replace("_"," ")} : {valor}")
        
def mostrar_lista_diccionarios(lista:list) -> bool:
    retorno = False
    for elemento in lista:
        retorno = True
        mostrar_diccionario(elemento)
        print("")
        
    return retorno

lista_alumnos = []

while(True):
    print("1.Leer en csv\n2.Guardar en csv")
    opcion = int(input("\nIngrese opcion:"))
    
    if opcion == 1:
        if leer_csv_alumnos("alumnos.csv",lista_alumnos):
            print("Archivo leido con exito")
            print("Estos son los resultados")
            if mostrar_lista_diccionarios(lista_alumnos) == False:
                print("Error, lista vacia")
        else:
            print("Error al leer el archivo, no existe.")
    elif opcion == 2:
        lista_alumnos = [
            {"nombre":"Mariano","apellido":"Fernandez","genero":"masculino","nota_final":10},             {"nombre":"Jose","apellido":"Perez","genero":"masculino","nota_final":4},
            {"nombre":"Maria","apellido":"Lopez","genero":"femenino","nota_final":7}
        ]
        guardar_csv("alumnos_guardados.csv",lista_alumnos)
    elif opcion == 3:
        leer_json("alumnos.json",lista_alumnos)
        mostrar_lista_diccionarios(lista_alumnos)
    elif opcion == 4:
        lista_alumnos = [
            {"nombre":"Mariano","apellido":"Fernandez","genero":"masculino","nota_final":10},             {"nombre":"Jose","apellido":"Perez","genero":"masculino","nota_final":4},
            {"nombre":"Maria","apellido":"Lopez","genero":"femenino","nota_final":7}
        ]
        generar_json("alumnos.json",lista_alumnos)
        
        
numero = 5 

print("Es positivo" if numero > 0 else "No es positivo")
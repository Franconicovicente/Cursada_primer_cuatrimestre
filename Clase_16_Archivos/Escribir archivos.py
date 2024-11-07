import os

#Escritura

with open("archivo3.txt","w") as archivo:
    #A diferencia de la lectura, si el archivo no existe lo crea, si ya existe, lo sobreescribe
    
    #Write -> Escribe una cadena completa en un archivo, cada vez que se ejecuta
    
    # archivo.write("Hola Mundo\n")
    # archivo.write("Hola DIV 114\n")
    # archivo.write("Hola Mariano")
    
    #writelines -> Escribe una lista de strings dentro de mi archivo
    
    lista_strings = ["Hola Mundo\n","Mariano\n","Ezequiel"]
    archivo.writelines(lista_strings)
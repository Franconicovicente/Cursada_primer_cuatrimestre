#Aparte de leer y escribir, yo puedo anexar información sin sobreescribir lo anterior, para eso debo abrir el archivo en modo a, al igual que en la escritura, si no existe lo crea, si existe en este caso no sobreescribe la info

with open("archivo.txt","a") as archivo:
    archivo.write("\nBuen dia")

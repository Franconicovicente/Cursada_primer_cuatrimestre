lista_numeros = [1,3,5]

# lista_numero_dos = lista_numeros #SE GUARDA EN LISTA NUMERO DOS EL ID DE LISTA NUMERO, SE CAMBIA TODO
# lista_numero_dos = [1,3,5] # se guarda en un id diferente
lista_numeros_dos = lista_numeros.copy()#copia SOLO la info de la lista lista_numeros, y la guarda en un id diferente bajo el numero lista_numeros_dos

print(f"lista numeros = {lista_numeros}")
print(f"Lista numeros dos = {lista_numeros_dos}")

lista_numeros [0] = 2

print(f"lista numeros = {lista_numeros}")
print(f"Lista numeros dos = {lista_numeros_dos}")





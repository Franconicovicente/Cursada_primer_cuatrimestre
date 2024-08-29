#NUMEROS QUE SOLO PUEDEN SER DIVIDIDOS POR SI MISMOS Y POR EL 1


#PARA VERIFICAR SI UN NUMERO ES PRIMO O NO, HAY QUE VERIFICAR QUE ESE NUMERO NO SE PUEDA VERIFICAR POR OTROS NUMEROS ANTERIORES



numero = int(input("Ingrese un numero:")) # 12


bandera = True #POR DEFECTO ES PRIMO HASTA QUE SE DEMUESTRE LO CONTRARIO


for i in range(2, numero, 1): #TENGO QUE EVALUAR DESDE EL 2 AL 12---> (12 NUMERO INGRESADO)

    #SI ESTO SE CUMPLE UNA SOLA VEZ, EL NUMERO NO ES PRIMO
    if numero % i == 0:
        print(f"{numero} / {i} da resultado entero")
        bandera = False #NO ES PRIMO
        break # CUANDO YA VERIFIQUE QUE NO ES PRIMO, CORTO EL FOR.


if bandera == False:
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo") 
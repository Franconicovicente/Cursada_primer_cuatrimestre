# SE ENCARGA DE LLAMAR A LAS FUNCIONES
# NO VAMOS A TENER FUNCIONES


from Paquete.Funciones import *

saludar()

numero_a = int(input("Ingrese el primer numero:"))
numero_b = int(input("Ingrese el segundo numero:"))

suma = sumar(numero_a, numero_b)
print (f"El resultado de la suma entre {numero_a} y {numero_b} es {suma}")

numero = int(input("Ingrese un numero:"))

informar_num_positivo(numero)


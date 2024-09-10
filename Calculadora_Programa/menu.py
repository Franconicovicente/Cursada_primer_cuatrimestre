import os
from funciones import *




def menu():
    
    contador_numeros = 0

    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        
        opcion = int(input("Su opcion: "))
        
        if opcion == 1:
            numero_uno = float(input("Ingrese el primer numero:"))
            print("Ingreso Primer Operando")
            contador_numeros += 1
        elif opcion == 2:
            numero_dos = float(input("Ingrese el segundo numero:"))
            print("Ingreso Segundo Operando")
            contador_numeros += 1

        elif contador_numeros == 2 and opcion == 3:
            resultado_suma = calcular_suma(numero_uno, numero_dos)
            resultado_resta = calcular_resta(numero_uno, numero_dos)
            resultado_division = calcular_division(numero_uno, numero_dos)
            resultado_multiplicacion = calcular_multiplicacion(numero_uno, numero_dos)
            resultado_potencia = calcular_potencia(numero_uno, numero_dos)
            resultado_resto = calcular_resto(numero_uno, numero_dos)
            resultado_factorial_A = calcular_factorial_A(numero_uno)
            resultado_factorial_B = calcular_factorial_B(numero_dos)

        elif contador_numeros == 2 and opcion == 4:
            if numero_dos == 0:
                print (resultado_division)
            else:
                print(f"Division de {numero_uno} / {numero_dos} = {resultado_division}")
            print(f"Suma entre {numero_uno} + {numero_dos} = {resultado_suma}")
            print(f"Resta entre {numero_uno} - {numero_dos} = {resultado_resta}")
            print(f"Multiplicacion entre {numero_uno} x {numero_dos} = {resultado_multiplicacion}")
            print(f"Potencia de {numero_uno} elevado a {numero_dos} = {resultado_potencia}")
            if numero_dos == 0:
                    print(resultado_resto)
            else:
                print(f"Resto entre {numero_uno} % {numero_dos} = {resultado_resto}")
                print(f"Factorial del numero {numero_uno} = {resultado_factorial_A}")
                print(f"Factorial del numero {numero_dos} = {resultado_factorial_B}")

        elif opcion == 5:
            print("Saliendo...")
            break
        
    
        elif contador_numeros != 2 and opcion == 3:
            print("No se puede acceder si no se ingresaron los operandos")
        elif contador_numeros != 2 and opcion == 4:
            print("No se puede acceder si no se calcularon las operaciones")

        else:
            print("Opcion invalida ingrese números entre 1-5")


        input("Pulse boton para continuar...")
        os.system('cls')
        
    
    
menu()

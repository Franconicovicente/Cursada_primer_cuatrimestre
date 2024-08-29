'''
TAREA: 
Realizar una calculadora en donde se le pida al usuario una operación
Validar (“+” , “-” , “/”, “*”) en caso de no ser ninguno de esos especificar error

(+) -> Suma
(-) -> Resta
(/) -> Dividir
(*) -> Multiplicar

Luego de tener el operador, pedir dos números y hacer la operación correspondiente.
'''

operacion = input("Inserte una operación:'+, -, *, /':")
while operacion != "+" and operacion != "-" and operacion != "*" and operacion != "/":
    input("ERROR")

numero_1 = int(input("Ingrese el primer numero:"))
numero_2 = int(input("Ingrese el segundo numero"))

match operacion:
    case "+":
        suma = numero_1 + numero_2
        mensaje = f"El resultado de su suma es {suma}"
    case "-":
        resta = numero_1 - numero_2
        mensaje = f"El resultado de su resta es {resta}"
    case "*":
        multiplicar = numero_1 * numero_2
        mensaje = f"El resultado de su multiplicación es {multiplicar}"
    case "/":
        if numero_2 == 0:
            mensaje = "No se puede dividir por 0"
        else:
            dividir = round(numero_1 / numero_2, 2)
            mensaje = f"El resultado de su division es {dividir}"

print(mensaje)
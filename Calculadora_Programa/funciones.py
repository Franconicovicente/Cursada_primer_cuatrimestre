def calcular_suma (numero_a:float, numero_b:float) -> float:
    '''
    El usuario ingresa dos numeros y se calcula la suma.
    retorna el resultado
    '''
    resultado_suma = numero_a + numero_b
    return resultado_suma
calcular_suma

def calcular_resta (numero_a:float, numero_b:float) -> float:
    '''
    El usuario ingresa dos numeros y se calcula la resta, se retorna el resultado
    '''
    resultado_resta = numero_a - numero_b
    return resultado_resta

calcular_resta

def calcular_division (numero_a:float, numero_b:float) -> float:
    '''
    El usuario ingresa dos numeros y se los divide, se retorna el resultado
    Si el segundo numero es 0, se da una alerta de que no se puede dividir por 0
    Se redondea a dos decimales
    '''
    if numero_b != 0:
        resultado_division = round(numero_a / numero_b, 2)
        return resultado_division
    else:
        return "No se puede dividir por 0"

calcular_division

def calcular_multiplicacion (numero_a:float, numero_b:float) -> float:
    '''
    El usuario ingresa dos numeros y se los multiplica, se retorna el resultado
    En caso de ser con coma, se le redondea a dos decimales
    '''
    resultado_multiplicacion = round(numero_a * numero_b, 2)
    return resultado_multiplicacion

calcular_multiplicacion

def calcular_potencia (numero_a:float, numero_b:float) -> float:
    '''
    El usuario ingresa dos potencias y se hace la cuenta, se retorna el resultado
    '''
    resultado_potencia = round(numero_a ** numero_b, 2)
    return resultado_potencia

calcular_potencia

def calcular_resto (numero_a:float, numero_b:float) -> float:
    '''
    El usuario calcula el resto entre los dos numeros ingresados, retorna el resultado
    se redondea en caso de ser necesario
    '''
    if numero_b != 0:
        resultado_resto = round(numero_a % numero_b, 2)
        return resultado_resto
    else:
        return "No se puede hacer el resto de un numero con 0"

calcular_resto

def calcular_factorial_A (numero_a) -> float:
    '''
    El usuario ingresa dos numeros, y se calcula su factor por separado

    '''
    if numero_a == 0 or numero_a == 1:
        return 1
    else:
        resultado_factorial_A = round (numero_a * calcular_factorial_A (numero_a - 1), 2) 
        return resultado_factorial_A

calcular_factorial_A

def calcular_factorial_B (numero_b) -> float:

    if numero_b == 0 or numero_b == 1:
        return 1
    else:
        resultado_factorial_B = round(numero_b * calcular_factorial_B (numero_b - 1) , 2)
        return resultado_factorial_B
    
calcular_factorial_B
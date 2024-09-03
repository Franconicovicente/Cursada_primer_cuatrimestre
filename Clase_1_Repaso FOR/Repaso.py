'''Para un hospital veterinario

Es necesario registrar el ingreso de las mascotas en la próxima hora (solo se pueden atender 20 mascotas), para esto hay que considerar los siguientes datos y encasillarlos en ciertos diagnósticos para poder derivarlos adecuadamente:










CALCULAR










'''

contador_mascotas_sin_vacuna_enfermedad = 0
bandera_mascota_mas_vieja = True
edad_mascota_mas_vieja = 0
contador_vacunadas = 0
contador_no_vacunadas = 0
contador_mascotas = 0
contador_gato = 0
contador_perro = 0
contador_loro = 0
acumulador_gato = 0

for i in range (2):


    # -Edad (Validar entre 1 y 25 años) 

    edad = input("Diga la edad de su mascota, entre 1 y 25 años: ")
    edad = int(edad)
    while edad < 1 or edad > 25:
        edad = input("Diga la edad de su mascota, entre 1 y 25 años: ")
        edad = int(edad)

    # -Tipo: (Validar “gato”, “perro”, “loro”) 
    
    tipo = input("Diga su tipo de animal 'gato' , 'perro' o 'loro': ")
    while tipo != "gato" and tipo != "perro" and tipo != "loro":
        tipo = input("Diga su tipo de animal 'gato' , 'perro' o 'loro': ")
    
    # -Peso: (Más de 0 kg) -

    peso = input("Diga el peso de su mascota :")
    peso = float(peso)
    while peso < 0:
        peso = input("Diga el peso de su mascota :")
        peso = float(peso)

    # -Diagnóstico: (Validar “problemas digestivos”, “parásitos”, “infección”)

    diagnostico = input("Diagnostico de su mascota 'problemas digestivos', 'parasitos' o 'infeccion' :")
    while diagnostico != "problemas digestivos" and diagnostico != "parasitos" and diagnostico != "infeccion":
        diagnostico = input("Diagnostico de su mascota 'problemas digestivos', 'parasitos' o 'infeccion' :")

    #-Vacuna antirrábica (validar “si”, ”no”)

    vacuna = input("Tiene vacuna antirrabica? 'si' o 'no' : ")
    while vacuna != "si" and vacuna != "no":
        vacuna = input("Tiene vacuna antirrabica? 'si' o 'no' : ")


# 1. Cantidad de mascotas sin vacuna antirrábica, cuya edad está entre los 4 y 12 años, que se presentaron por infección o parásitos.
    if vacuna == "no":
        if edad > 3 and edad < 12:
            if tipo == "infeccion" or tipo == "parasitos":
                contador_mascotas_sin_vacuna_enfermedad += 1
        contador_no_vacunadas += 1
    else:
        # 3. Edad y tipo de la mascota más vieja con vacuna antirrábica.
        if edad_mascota_mas_vieja < edad or bandera_mascota_mas_vieja == True:
            edad_mascota_mas_vieja = edad
            tipo_mascota_mas_vieja = tipo
            bandera_mascota_mas_vieja = False
        
        contador_vacunadas += 1
    
    if tipo == "gato":
        # 5. Promedio de edad de los gatos.
        acumulador_gato += edad
        if diagnostico == "problemas digestivos":
            contador_gato += 1
    elif tipo == "perro":
        if diagnostico == "problemas digestivos":
            contador_perro += 1
    else:
        if diagnostico == "problemas digestivos":
            contador_loro += 1

    


    contador_mascotas += 1


#2. El tipo de mascota más ingresada con problemas digestivos.

if contador_gato > contador_perro > contador_loro:
    mensaje_animales = "Hay mas gatos"
elif contador_perro > contador_loro:
    mensaje_animales = "Hay mas perros"
else:
    mensaje_animales = "Hay mas loros"



# 4. Porcentaje de mascotas vacunadas y no vacunadas.

porcentaje_vacunadas = round((contador_vacunadas / contador_mascotas) * 100, 2)

porcentaje_no_vacunadas = round((contador_no_vacunadas / contador_mascotas) * 100, 2)


if bandera_mascota_mas_vieja == True:
    mensaje = f"No hay mascota con vacuna antirrabica.Cantidad de mascotas sin vacuna antirrabica con entre 4 y 12 años es de {contador_mascotas_sin_vacuna_enfermedad}.El porcentaje de mascotas vacunadas es de {porcentaje_vacunadas}%, el de no vacunadas es del {porcentaje_no_vacunadas}%. El promedio de la edad de los gatos es de {acumulador_gato} años"
else:
    mensaje = f"La mascota mas vieja con antirrabica tiene {edad_mascota_mas_vieja} años y es un {tipo_mascota_mas_vieja}.El porcentaje de mascotas no vacunadas es de {porcentaje_no_vacunadas}%, el de vacunadas es de {porcentaje_vacunadas}% El promedio de la edad de los gatos es de {acumulador_gato}años"


print(mensaje)
print(mensaje_animales)

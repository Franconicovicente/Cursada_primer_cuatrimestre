'''
INTEGRADOR

La división de higiene está trabajando en un control de stock para productos sanitarios. 
Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos: 
1. El tipo (validar "barbijo", "jabón" o "alcohol") 
2. El precio: (validar entre 100 y 300) 
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades) 
4. La marca y el Fabricante. 

Se debe informar lo siguiente: 
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante. 
B. Del ítem con más unidades, el fabricante. 
C. Cuántas unidades de jabones hay en total.
'''
bandera_barbijo = True
bandera_unidades = True
mas_caro_barbijo = 0
item_maximo_unidades = 0
acumulador_jabones = 0
unidades_barbijo = 0


for i in range (2):

    # 1. El tipo (validar "barbijo", "jabón" o "alcohol") 
    tipo = input("Ingrese tipo: barbijo, jabon o alcohol:")
    while tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol":
        tipo = input("Ingrese un tipo valido:")
    
    # 2. El precio: (validar entre 100 y 300) 
    precio = input("Ingrese un precio entre 100 y 300:")
    precio = int(precio)
    while precio < 100 or precio > 300:
        precio = input("Ingrese un precio valido entre 100 y 300:")
        precio = int(precio)

    # 3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades) 

    unidades = input("Ingrese un numero de unidades. Entre 1 y 1000:")
    unidades = int(unidades)
    while unidades < 1 or unidades > 1000:
        unidades = input("Ingrese un numero valido de unidades:")
        unidades = int(unidades)
    
    # 4. La marca y el Fabricante. 

    marca = input("Introduzca una marca:")

    fabricante = input("Introduzca un fabricante:")

    # A. Del más caro de los barbijos, la cantidad de unidades y el fabricante. 
    if tipo == "barbijo":
        if mas_caro_barbijo < precio or bandera_barbijo == True:
            mas_caro_barbijo = precio
            unidades_barbijo = unidades
            fabricante_barbijo = fabricante
            bandera_barbijo = False
    
    # C. Cuántas unidades de jabones hay en total.
    elif tipo == "jabon":
        acumulador_jabones += unidades

    # # B. Del ítem con más unidades, el fabricante. 
    if item_maximo_unidades < unidades or bandera_unidades == True:
        item_maximo_unidades = unidades
        fabricante_unidades = fabricante
        bandera_unidades = False

if bandera_barbijo:
    mensaje = f"No se ingresaron barbijos, por ende no hay unidades ni nombre de fabricante.
    \nHay un total de {acumulador_jabones} unidades en jabones \nEl nombre del fabricante del item con mas unidades es {fabricante_unidades}"
else:
    mensaje = f"El precio del barbijo mas caro es {mas_caro_barbijo} con un total de {unidades_barbijo} unidades y el nombre del fabricante es {fabricante_barbijo}. 
    \nHay un total de {acumulador_jabones} unidades en jabones \nEl nombre del fabricante del item con mas unidades es {fabricante_unidades}"

print(mensaje)

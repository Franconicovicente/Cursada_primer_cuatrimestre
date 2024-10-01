import random

def inicializar_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    matriz = []
    
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz:list)->None:
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):#len(matriz[0])
            print(matriz[fil][col],end=" ")
        print("")
        
def mostrar_producto(producto:list) -> None:
    
    print(f"ID:{producto[COL_ID_UNICO]}")
    print(f"NOMBRE:{producto[COL_NOMBRE]}")
    print(f"PRECIO:${producto[COL_PRECIO]}")
    print(f"STOCK:{producto[COL_STOCK]} unidades\n")
    # for fil in range(len(lista_productos)):
    #     print(f"ID:{lista_productos[fil][COL_ID_UNICO]}")
    #     print(f"NOMBRE:{lista_productos[fil][COL_NOMBRE]}")
    #     print(f"PRECIO:${lista_productos[fil][COL_PRECIO]}")
    #     print(f"STOCK:{lista_productos[fil][COL_STOCK]} unidades\n")

def mostrar_productos(lista_productos:list) -> None:
    for fil in range(len(lista_productos)):
        print(f"ID:{lista_productos[fil][COL_ID_UNICO]}")
        print(f"NOMBRE:{lista_productos[fil][COL_NOMBRE]}")
        print(f"PRECIO:${lista_productos[fil][COL_PRECIO]}")
        print(f"STOCK:{lista_productos[fil][COL_STOCK]} unidades\n")

#Imaginemos que nos piden un sistema en el que tenemos que almacenar productos

#Identificador Único (11111-99999) -> Random
#Nombre
#Precio
#Cantidad Stock

#Nos piden lo siguiente

#1. Ingresar 3 productos
#2. Mostrar todos los productos
#3. Buscar un producto por código único.
#4. Salir del sistema.

# lista_id = []
# lista_nombres = []
# lista_precios = []
# lista_stocks = []

# lista_productos = [
#                [0,0,0,0],
#                [0,0,0,0],
#                [0,0,0,0],
#                [0,0,0,0],
#                [0,0,0,0]
#                   ]

lista_productos = inicializar_matriz(3,4,0)

COL_ID_UNICO = 0
COL_NOMBRE = 1
COL_PRECIO = 2
COL_STOCK = 3

#mostrar_matriz(lista_productos)

#1.CARGA PRODUCTO
for fil in range(len(lista_productos)):
    print("SE ESTA CARGANDO UN NUEVO PRODUCTO")
    id_unico = random.randint(11111,99999)
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = float(input("Ingrese el precio del producto: "))
    cantidad_stock = int(input("Ingrese la cantidad de stock: "))
    
    lista_productos[fil][COL_ID_UNICO] = id_unico
    lista_productos[fil][COL_NOMBRE] = nombre_producto
    lista_productos[fil][COL_PRECIO] = precio_producto
    lista_productos[fil][COL_STOCK] = cantidad_stock

#2.MOSTRAR PRODUCTOS
mostrar_productos(lista_productos)

#3.BUSCAR PRODUCTO
id_unico_a_buscar = int(input("Ingrese el id del producto a buscar: "))
bandera = False

for fil in range(len(lista_productos)):
    if lista_productos[fil][COL_ID_UNICO] == id_unico_a_buscar:
        print("El producto se encontro: ")
        bandera = True
        mostrar_producto(lista_productos[fil])
        break
    
if bandera == False:
    print("No se encontro el producto")


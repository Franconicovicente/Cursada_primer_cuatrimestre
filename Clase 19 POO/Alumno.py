import random
# Alumno -> legajo, nombre, apellido, edad, nota final

# El nombre de una clase se pone en UpperCamelCase

# usuario -> Usuario
#mi clase -> MiClase

class Alumno:
    #Elemento constructor: el que le da vida a mi objeto, da valor a los atributos de mi clase

    def __init__(self,nombre:str,apellido:str,edad:int) -> None:
        #Definir las caracteristicas de mi clase
        #Creando atributos
        self.nombre = nombre
        self.apellido = apellido 
        self.edad = edad 
        self.legajo = random.randint(11111,222222)
        self.nota_final = None

    # las propiedades me permiten darle un poco mas de personalizacion a mis atributos
    #Creo una propiedad personalizada para el atributo edad
    @property
    def Edad(self):
        return f"{self.edad} años"
    
    # Defino propiedad de setter (para modificar el atributo)

    @Edad.setter
    def Edad(self,edad_derecha:int):
        if edad_derecha >= 18 and edad_derecha <= 80:
            self.edad = edad_derecha
        else:
            #ponemos una edad por defecto
            # self.edad = 18
            #podemos no hacer nada
            #lanzar un error -> con excepciones (no vimos)
            pass

    def rendir_final(self) -> bool:
        '''
        Este metodo se encarga de rendir un final, genera una nota aleatoria 
        y la guarda en la nota final, si la nota generada es 6 o mas, no va a poder volver a rendir el final
        '''
        if self.nota_final == None or self.nota_final < 6:
            #Rendir el final
            self.nota_final = random.randint(1,10)
            retorno = True
        else:
            retorno = False
        
        return retorno

    def obtener_informacion(self) -> str:
        retorno = ""
        retorno += f"Nombre: {self.nombre}\n"
        retorno += f"Apellido: {self.apellido}\n"
        retorno += f"Edad: {self.Edad}\n"
        if self.nota_final != None:
            retorno += f"Nota: {self.nota_final}"
        else:
            retorno += "Nota: SIN DEFINIR"
        return retorno
    
    #Metodos DUNDER -> Metodos especiales que me permiten hacer tareas especiales con mi objeto, por ejemplo, imprimirlo con un print, recorrerlo en un for
    def __str__(self) -> str:
        return self.obtener_informacion()
    
    def __iter__(self):
        lista_objeto = [self.legajo,self.nombre,self.apellido,self.edad,self.nota_final]

        if self.nota_final == None:
            del lista_objeto[-1]

        for elemento in lista_objeto:
            yield elemento

    def __eq__(self, alumno_derecha: object) -> bool:
        return self.nombre == alumno_derecha.nombre and self.apellido == alumno_derecha.apellido and self.edad == alumno_derecha.edad and self.nota_final == alumno_derecha.nota_final


#Crear un objeto

alumno_uno = Alumno("Franco","Vicente",19)
alumno_dos = Alumno("Lucia","Rodriguez",19)
alumno_tres = Alumno("Avril","Escalada",18)

#Probamos __eq__()

print(alumno_uno == alumno_uno)
print(alumno_uno == alumno_dos)

#Probamos metodo __iter__()

# alumno_uno.rendir_final()
# for elemento in alumno_uno:
#     print(elemento)

#Probamos metodo __str__()

# # print(alumno_uno) # METODO DUNDER
# print("")
# alumno_uno.rendir_final()
# print(alumno_uno)
# print("")
# # print(alumno_dos) # METODO DUNDER
# alumno_dos.rendir_final()
# print("")
# print(alumno_dos) # METODO DUNDER
# print("")
# # print(alumno_tres) # METODO DUNDER
# print("")
# alumno_tres.rendir_final()
# print(alumno_tres)

#Acceso 

# print(alumno_uno.nombre)
# print(alumno_uno.edad)
# print(alumno_uno.apellido)
# print(alumno_uno.legajo)
# print(alumno_uno.nota_final)

#Pruebo el metodo rendir_final()
# while True:
#     if alumno_uno.rendir_final():
#         print("Rindió final correctamente")
#         print(alumno_uno.nota_final)
#     else:
#         print("Ya rindió este final anteriormente")
#         break

# Llamo al metodo obtener_informacion()

# print(alumno_uno.obtener_informacion())
# alumno_uno.rendir_final()
# print(alumno_uno.obtener_informacion())

# Probamos la propiedad getter Edad()

# print(alumno_uno.Edad)
# print(alumno_uno)

# Probamos la propiedad setter Edad()

alumno_uno.Edad = 200 
print(alumno_uno)


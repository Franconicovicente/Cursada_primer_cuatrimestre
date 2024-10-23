'''
Ejercitación Clase 13 
(Clase String)

1. Realizar una función que reciba un string de una fecha de nacimiento en cualquiera de los dos formatos (DD-MM-AAAA) o (DD/MM/AAAA) y devuelva una lista de ENTEROS con el día mes y año convertidos a entero.

Por ejemplo:
Ingreso un string que diga “18-10-2024” y devuelve una lista así

lista_enteros = [18,10,2024] -> Los str ya convertidos en int

2. Realizar una función que haga lo contrario a la función anterior, recibe una lista de enteros de 3 elementos y devuelve un str en formato fecha, también recibe el separador, pudiendo pasar ‘-’ o ‘/’.
En caso de pasar cualquier otro separador o se le pase una lista que no tenga 3 elementos la función retorna None

Por ejemplo:
Le paso una lista así 
lista_enteros = [10,10,2020] 
Devuelve un str como los siguientes -> “10-10-2020” o “10/10/2020”
None en caso de error

3.Realizar una función que reemplace todas las vocales de mi string por una letra aleatoria, devuelve una cadena resultado.

4.Realizar una función que me genere un número de legajo aleatorio para mi empleado, el mismo debe tener si o si 6 caracteres.
El sistema debe generar un número aleatorio entre 1 y 300000, en caso de que el número generado sea menor a 6 caracteres rellenarlo con todos ceros a la izquierda.

5. Crear una función que reciba una cadena de caracteres y devuelva otro string eliminando a los caracteres que se repiten más de una vez.
Por ejemplo.
“Mariano” -> “Mrino”

6. Crear una función que reciba una cadena de caracteres y retorne una matriz contando todas las vocales (no discriminar mayúsculas ni minúsculas)
EJEMPLO “Mariano”



'''
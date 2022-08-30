#Tuplas: son similares a las listas aunque no se pueden modificar los valores luego de crearlas y sus valores los definimos entre parentesis

tupla = ("lunes", "martes", "miercoles")
tupla_multi = ([1,2,3], "a", 75.5, tupla)

print(tupla)
print(tupla_multi)

#La unica forma de modificar los valores de una tupla es convertirla a una lista
#lista = list(tupla)

#Metodos de tupla
#index nos permide saber el indice de un valor de la tupla

print(tupla.index("lunes"))

#count nos indica la cantidad de veces que aparece un elemento en la lista

print(tupla_multi.count("a"))

#----- Conjuntos -----

#Los conjuntos son colecciones de datos que nos facilitan ciertas operaciones ya que solo contiene valores unicos
#Cada elemento es unico (no se repiten) y no estan ordenados
#La funcion set nos ayuda a hacer converciones de datos

conjunto_vacio = set()
conjunto = {1, 2, 3}
print(type(conjunto_vacio), conjunto)

#Para agregar un elemento se utiliza la funcion .add
conjunto.add(4)

#Para verificar la pertenencia de un elemento en un conjunto se usa el comando "in"

grupo = {"sam", "juan", "pedro", "pepe"}
print("sam" in grupo)
print("juan" not in grupo)

#Un conjunto elimina automaticamente los elementos duplicados

extra = {1, 2, 2, 2, 3}
c = set(extra)
print(c)

#-----  Diccionarios  -----

#Los diccionarios son colecciones de datos similares a las listas
#Se define cada elemento dentro de un diccionario como una relacion entre Clave:Valor
#Las claves ejercen como indices de cada elemento

colores = {"azul":"blue", "negro":"black", "rosa":"pink"}
propiedades = {1:"nombre", 2:"apellido", 3:"profesion", 4:"region"}
print(propiedades)

#Para acceder a los valores por claves 

print(colores["negro"])

#Para modificar o añadir colores

colores["negro"] = "noir"

colores["blanco"] = "white"
colores["naranja"] = "orange"
print(colores)

#Recorrer los elementos de un diccionario a travez de un for (imprime la Clave)

for i in colores:
    print(i)

#Para recorrer por indice de los valores (imprime los Valores)

for i in colores:
    print(colores[i])

#El metodo items() nos devuelve Clave y Valor automaticamente

for i, j in colores.items():
    print(i, j)

#El metodo del() nos permite eliminar los valores de un diccionario

del(colores["azul"])
print(colores)
    
#Combinacion  de listas con diccionarios

equipo = []
personajes = {"Nombre":"Sam", "Edad":"24", "Pais":"Mexico"}
equipo.append(personajes)

personajes = {"Nombre":"Juan", "Edad":"20", "Pais":"Japon"}
equipo.append(personajes)

personajes = {"Nombre":"Pedro", "Edad":"29", "Pais":"Peru"}
equipo.append(personajes)
print(equipo)

#Para imprimir los valores 

for i in equipo:
    print(i["Nombre"], "--", i["Edad"], "--", i["Pais"])








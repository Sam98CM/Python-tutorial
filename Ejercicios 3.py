#Listas son un tipo de dato compuesto de varos elementos
#list
lista_de_compras = ["Huevos", "Leche", "Queso", "Jabon"]
lista_con_precios = ["Huevos",1.55, "Leches",2, "Queso",3.5, "Jabon",5]

print(f"""Los {lista_con_precios[0]} cuesta {lista_con_precios[1]}
La {lista_con_precios[2]} cuesta {lista_con_precios[3]}""")

#Mutabilidad
lista_con_precios[1] = 0.9
print(f"""{lista_con_precios}
Los {lista_con_precios[0]} cuesta {lista_con_precios[1]}""")

#Metodos de las listas
#Podemos inicializar una lista de numeros a traves de una funcion range(a, b, in)
#a es el limite inferior de la secuencia de numeros
#b es el limite superior (este se excluye)
#in es la unidad de incremento (argumento opcional)

numeros = range(0,20,2)
lista_numeros = list(numeros)

print(numeros)
print(lista_numeros)

#Para añadir elementos a la lista usamos el metodo append()
lista_numeros.append(4)
print(lista_numeros)

#Si se quiere concatenar una lista a otra solo agregamos +

#La funcion len nos permite saber el numero total de elementos
print(len(lista_numeros))

#Con la funcion IN se puuede comprobar si algun valor existe en una lista
print(4 in lista_numeros)

#Se puede actualizar varios elementos de una lista usando slicing
lista_numeros[:5] = [54, 20, 1, 23, 0]
print(lista_numeros)

#Listas anidadas: se asignan listas como valores en una lista

fila_1 = [1, 2, 3]
fila_2 = [4, 5, 6]
fila_3 = [7, 8, 9]

matriz = [fila_1, fila_2, fila_3]
print(matriz)

#Para acceder a un valor de una matriz matriz[0][1]
#Donde matriz[0] es la primera lista y [1] es el elemento de de la lista seleccionada

print(matriz[0][1])











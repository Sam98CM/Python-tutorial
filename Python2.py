x = 30
nombre= "la cartulina de perla"
print(x)
#la palabra reservada add agrega la cantidad que se le ponga a la variable
x.__add__(10) 
#como hacer un diccionario
diccionario = {"uno": x, "dos": x.__add__(10)}
print(diccionario)
#tipos de variables:
#Int = enteros, float = flotantes, string(str) = caracteres o textos
#Tipos de impresion (print)
print("Una cadena \tseparada por una tabulacion")
print("Una cadena de una linea \n una cadena de otra linea")
print("""Linea 1 es esta 
Linea 2
linea 3 
continua
...""")
#Booleanos
#Se usa condicion de verdad o comparativo==
# 1 + 1 == 2  true  1 + 2 == 2  false
#(2 == 1+1) and (3 == 1+2)   =  true
#true and true = true
#false and false = false

#Conversion de tipos de datos
print(type(x))
nu_x = str(x)
print(type(nu_x))

#Operadores de asignacion
#numero = numero - 2,  nummero = numero + 2,  numero = numero / 2
# -=  +=  /=

#Operadores logicos (True o False)
#AND = sirve para evaluar dos condiciones
#OR = sirve para comprobar cual condicion es verdadera
#NOT = sirve para negar una sentencia True o false

#Operadores de comparacion (True o false), tambien sirve para comparar cadenas de caracteres
# == igualdad, != desigualdad, <, >, <=, >=  

#Lectura por teclado (Cuando quieres asignarle un valor a una variable desde la terminnal)
# numero = input()  (Se puede asignar el tipo de variable que puede aceptar la variable int, float, str)
# print(numero) (imprime el valor de la variable "numero")

#Formateo (format)
#Sirve para asignar valores en una cadena de texto
print("{} es el primer calor y {} es el segundo valor".format(1,2))
print(f"El valor  de {nombre.title()}\n es", x , "dolares por el papel") #title hace mayusculas cada primera letra de cada palabra guardada en la varible








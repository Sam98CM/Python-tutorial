#-----  Definir una funcion  -----
#La palabra reservada es def 
"""
def saludar():
    print("Hola mundo")
print(saludar())

def tabla():
    for i in range(10):
        print(f"5 * {i} = {5*i}")
print(tabla())
"""
# Scope o alcance define el area de un programa en el cual puedes acceder a un nombre
"""
def prueba():
    n = 10
    return n
print(prueba())
"""
#Si una funcion manda a llamar una variable fuera de ella es correcto, pero si intentamos acceder al valor de una variable que se encuentra en una funcion no se va a poder

#Retorno de valores (return)

def funcion():
    return "Hola Mundo"
print(funcion())

def lista():
    return [1, 2, 3, 4, 5]
print(lista())

#Argumentos y parametros

def resta(a, b):
    return a - b
print(resta(5, 2))

#Argumentos indeterminados (args) sirve para asignar datos de distintos tipos 

def argumentar(*args):
    print(args)
print(argumentar(5, "Samuel", [1, 2, 3]))

#Para imprimir cada elemento  de args
def argumentar1(*args):
    for i in args:
        print(i)
print(argumentar1(1, "Pedro", [3, 2, 1]))

#Para pasar una relacion de nombre y argumento se utiliza kwargs (devuelve un diccionario)
def nombrar(**kwargs):
    print(kwargs)
print(nombrar(id = 5, nombre = "Sam Cruz", numeros = [1, 2, 3, 4]))

#Para imprimir los nimbres y argumentos

def nombrar1(**kwargs):
    for i in kwargs:
        print(i, " ", kwargs[i])
print(nombrar1(id = 5, nombre = "Sam Cruz", numeros = [1, 2, 3, 4]))  


"""
caballero = {"vida":2, "ataque":2, "defensa":2, "alcance":2}
guerrero = {"vida":2, "ataque":2, "defensa":2, "alcance":2}
arquero = {"vida":2, "ataque":2, "defensa":2, "alcance":2}

print(caballero, guerrero, arquero)
#Modificamos los atributos

guerrero["ataque"] = caballero["ataque"]*2
guerrero["alcance"] = caballero["alcance"]*2

caballero["vida"] = guerrero["vida"]*2
caballero["defensa"] = guerrero["defensa"]*2

arquero["ataque"] = guerrero["ataque"]
arquero["defensa"] = guerrero["defensa"]/2
arquero["alcance"] = guerrero["alcance"]*2

print(caballero, guerrero, arquero)
"""
#-----  Sentencia if  -----
"""
x = 5
if x == 5:
    print("x vale 5")

#Sentencia if anidada

a = 10
b = 5

if a == 10:
    print("A vale {}".format(a)) #El metodo format sirve  para asignar el valor dentro de las llaves
    if b == 5:
        print("B vale {}".format(b))

#Tambien se puede utilizar operadores logicos

if a == 10 and b == 5:
    print("A vale {}, y B vale {}".format(a, b))
"""
#-----  Else y Elif  -----
#Else(si no) se encadena al final del bloque para abrir una lista de instrucciones
#Elif(si no, si) establece una nueva condicion que se encadena a otro if o elif cuya condicion resultó falsa
"""
z = 13
if z % 2 == 0:
    print(z, "es un numero par")
else:
    print(z, "es un numero impar")

#Respuestas dinamicas

texto = input("¿Que desea hacer?\n")

if texto == "saludar":
    print("Buenas noches")
elif texto == "despedirce":
    print("adios")
else:
    print("Ingrese un dato valido")
"""
#Clasificador
"""
puntaje = float(input("Introduce la calificaion: \n"))
if puntaje >= 9:
    print("Excelente desempeño")
elif puntaje >= 7:
    print("Buen desempeño")
elif puntaje >= 5:
    print("Aprobado")
else:
    print("Reprobado")
"""
#-----  Bucle while  ------
"""
contador = 0

while contador <= 5:
    contador += 1
    print("Contador es igual a = ", contador)

c = 0 

while c <= 5:
    print("Contador vale = ", c)
    c += 1
else:
    print("Se realizaron {} iteraciones".format(c))

#Se puede utilizar el comando break para salir de un bucle

contador_1 = 0
while contador_1 <= 5:
    contador_1 += 1
    if contador_1 == 4:
        print("Rompemos el bucle cuando Contador vale ", contador_1)
        break
    print("Contador vale ", contador_1)
else: 
    print("Se realizaron {} iteraciones".format(contador_1))
"""
#Se puede utilizar el comando continue para seguir con la iteracion sin salir del bucle
"""
c = 0
while c <= 5:
    c += 1
    if c == 4:
        print("Ya que C vale {} saltamos esta iteracion \n y continuamos con la siguiente".format(c))
        continue
    print("C vale = ", c)
else:
    print("Se realizacon {} iteraciones".format(c))
"""

#Menu de usuario

print("-----  Bienvenido  -----")

while (True):
    opcion = input("""\n Ingrese una opcion:
    (1) Saludar.
    (2) Sumar dos numeros.
    (3) Salir \n""")
    if opcion == "1":
        print("\n Buenos dias! \n")
    elif opcion == "2":
        numero1 = float(input("Ingrese el primer numero: \n"))
        numero2 = float(input("Ingrese el segundo numero: \n"))
        print("\n La suma es igual a {}".format(numero1 + numero2))
    elif opcion == "3":
        print("\n Adios!")
        break
    else:
        print("\n Elija una opcion valida")


#-----  For  -----
#Es un bucle que se repite un numero determinado de veces

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numeros:
    print(i)

#Se puede modificar su valor

numeros01 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
for i in numeros01:
    numeros01[i] *= 10
    i += 1
print(numeros01)

#Recorer una cadena de texto 

cadena = "Hola mundo"
for i in cadena:
    print(cadena)

#Range genera la secuencia de numeros enteros definida por el usuario
#El primer numero es con el que se va a empezar o inicializar
#El segundo numero es hasta donde va a finalizar
#El tercer numero define en de cuanto a cuanto van a ser las iteraciones

range(0, 10, 2)
for i in range(10):
    print(i)


#-----  Funciones Recursivas  -----
"""
def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print(num, "boom")
    print("Fin de funcion ", num)
print(cuenta_atras(5))

def factorial(num):
    print("Valor inicial ---> ", num)
    if num > 1:
        num = num * factorial(num - 1)
    print("Valor final ---> ", num)
    return num
print(factorial(5))
"""
#-----  Exceptiones  -----
#Son bloques de codigo que permiten continuar la ejecucion del codigo aun cuando se presenta un error

while(True):
    try:
        num = int(input("Ingrese un numero: "))
        print("El numero {} y la divicion da {}".format(num, num / num))
        break
    except:
        print("Por favor intente de nuevo.")

#Else y Finally

while(True):
    try:
        num = int(input("Ingrese un numero: "))
        print("El numero {} y la divicion da {}".format(num, num / num))
    except:
        print("Por favor intente de nuevo.")
    else:
        print("La ejecucion fue exitosa.")
        break
    finally:
        print("Fin del bucle.")


#-----  Programcion Orientada a Objetos  -----
#Programacion estructurada
"""
productos = [
    {"cod":"10001", "Nombre":"Jabon", "Categoria":"Higiene personal", "pvp":0.9},
    {"cod":"10002", "Nombre":"Cereal", "Categoria":"Granos", "pvp":1.5},
    {"cod":"10003", "Nombre":"Limones", "Categoria":"Fruta", "pvp":0.7}
]
def mostrar_productos(productos, cod):
    for i in productos:
        if (cod == i["cod"]):
            return print("{} {}".format(i["Nombre"], i["pvp"]))
    print("Producto no encontrado")
print(mostrar_productos(productos, "10003"))

def borrar_productos(productos, cod):
    for j, i in enumerate(productos):
        if (cod == i["cod"]):
            del(productos[j])
            return print(str(i), "-->Eliminado")
    print("Producto no encontrado")
print(borrar_productos(productos, 10002))
"""
#-----POO-----

class Producto:

    def __init__(self, cod, nombre, categoria, pvp):
        self.cod = cod
        self.nombre = nombre
        self.categoria = categoria
        self.pvp = pvp
    
    def __str__(self):
        return "{} {}".format(self.nombre, self.pvp)
        
#Otra estrctura para el negocio

class Negocio:

    def __init__(self, productos=[]):
        self.productos = productos
    
    def mostrar_producto(self, cod = None):
        for i in self.productos:
            if (i.cod == cod):
                print(i)
                return
        print("Producto no encontrado")

    def borrar_producto(self, cod = None):
        for i, j in enumerate(self.productos):
            if (j.cod == cod):
                del(self.productos[i])
                print(str(j), "-->ELIMINADO")
                return
        print("Producto no encontrado")    

#Asignamos valores a la clase Producto

limones = Producto(nombre = "Limon", cod = "10010", categoria = "Fruta", pvp = 0.8)
platos = Producto("10020", "Platos", "Vajilla", 2.4)

print(limones)

negocio = Negocio(productos=[limones, platos])

print(negocio.mostrar_producto("10010"))
print(negocio.borrar_producto("10010"))
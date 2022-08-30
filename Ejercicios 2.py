#Indices y Slicing 
#Los indices son numeros ordenados asociados a las variables que nos permite identificar los elementos por su posicion
texto = "Esta-Cadena"
print(texto[0], texto[1], texto[2], texto[3])
#Los slicing sirve para seleccionar un rango de valores [a:b]
print(texto[0:7])
#Escribir a[:b] equivale a [0:b]
#Escribir b[a:] equivale a [a:(n-1)]
print(texto[6:])
print(texto[:4])
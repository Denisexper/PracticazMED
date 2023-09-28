''' Crear funciones que permitan:
a. Ingresar n datos a una lista.
b. Ordenar una lista de menor a mayor.
c. Calcular la sumatoria de los datos de una lista.
d. Calcular la media de los datos.
e. Calcular la mediana.
f. Calcular la moda.
g. Calcular la desviación típica o estándar para datos sin agrupar.
'''

def ingresar_datos():
    n = int(input("Ingrese la cantidad de datos que desea ingresar: "))
    lista = []
    for i in range(n):
        dato = int(input(f"Ingrese el dato {i + 1}: "))
        lista.append(dato)
    return lista

def ordenar_lista(lista):
    lista.sort()
    return lista

def calcular_sumatoria(lista):
    suma = sum(lista)
    return suma

def calcular_media(lista):
    suma = calcular_sumatoria(lista)
    media = suma / len(lista)
    return media

def calcular_mediana(lista):
    lista_ordenada = ordenar_lista(lista)
    n = len(lista_ordenada)
    if n % 2 == 0:
        mediana = (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    else:
        mediana = lista_ordenada[n // 2]
    return mediana

def calcular_moda(lista):
    from collections import Counter
    contador = Counter(lista)
    moda = [item for item, frecuencia in contador.items() if frecuencia == max(contador.values())]
    return moda

def calcular_desviacion_estandar(lista):
    import math
    media = calcular_media(lista)
    n = len(lista)
    suma_de_cuadrados = sum([(x - media) ** 2 for x in lista])
    desviacion_estandar = math.sqrt(suma_de_cuadrados / (n - 1))
    return desviacion_estandar

datos = ingresar_datos()
print("Datos ingresados:", datos)
print("Datos ordenados:", ordenar_lista(datos))
print("Sumatoria:", calcular_sumatoria(datos))
print("Media:", calcular_media(datos))
print("Mediana:", calcular_mediana(datos))
print("Moda:", calcular_moda(datos))
print("Desviación estándar:", calcular_desviacion_estandar(datos))

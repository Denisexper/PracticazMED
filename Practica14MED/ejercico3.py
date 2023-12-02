"""Desarrolla una función que tome un texto y encuentre todas las palabras que contengan
solo letras minúsculas. Utiliza la función findall para obtener una lista de todas las palabras
que cumplen con este criterio."""
import re

def encuentra_palabras_minusculas(texto):
    palabras_minusculas = re.findall(r'\b[a-z]+\b', texto)
    return palabras_minusculas


texto_ejemplo = "El perro esta Comiendo Carne."
resultado = encuentra_palabras_minusculas(texto_ejemplo)
print(resultado)

"""Escribe una función que tome un texto y encuentre todas las ocurrencias de una palabra
específica proporcionada como argumento. Utiliza la función finditer para obtener un
iterador de objetos de coincidencia que contienen las ubicaciones de cada ocurrencia."""

import re

def encuentra_ocurrencias_palabra(texto, palabra_buscar):
    iterador_coincidencias = re.finditer(r'\b' + re.escape(palabra_buscar) + r'\b', texto)
    return list(iterador_coincidencias)


texto_ejemplo = "Es una mañana muy soleada."
palabra_a_buscar = "mañana"
resultado = encuentra_ocurrencias_palabra(texto_ejemplo, palabra_a_buscar)
print(resultado)

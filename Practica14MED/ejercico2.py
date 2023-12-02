"""Crea una función que tome una cadena y busque la presencia de una fecha en el formato
"dd/mm/yyyy". La función debe devolver True si encuentra al menos una fecha válida y
False en caso contrario. Utiliza la función search."""

import re

def busca_fecha_valida(cadena):
    patron_fecha = re.compile(r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b')
    coincidencia = patron_fecha.search(cadena)
    return bool(coincidencia)


texto_con_fechas = "Hoy es 02/12/2023 y mañana será 03/12/2023."
resultado = busca_fecha_valida(texto_con_fechas)
print(resultado)  

"""Escribe una función que verifique si una cadena contiene un código de empleado válido.
Un código de empleado válido debe comenzar con "EMP" seguido de tres números. Utiliza
la función match para realizar la verificación."""

import re

def es_codigo_empleado_valido(cadena):
    patron = re.compile(r'^EMP\d{3}$')
    coincidencia = patron.match(cadena)
    return bool(coincidencia)

codigo1 = "EMP123"
codigo2 = "EMP456"
codigo3 = "ABC789"

print(es_codigo_empleado_valido(codigo1))
print(es_codigo_empleado_valido(codigo2))  
print(es_codigo_empleado_valido(codigo3))  

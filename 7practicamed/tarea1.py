"""1. Crea una clase Divisor que tenga un método dividir. Utiliza el manejo de excepciones para
evitar la división por cero y maneja la excepción ZeroDivisionError que se levanta cuando
se intenta"""

class Divisor:
    def dividir(self, dividendo, divisor):
        try:
            resultado = dividendo / divisor
            return resultado
        except ZeroDivisionError:
            return "Error: No se puede dividir por cero."

divisor = Divisor()
resultado1 = divisor.dividir(10, 2)
resultado1 = int(resultado1)
print(resultado1)

resultado2 = divisor.dividir(10, 5)
resultado2 = int(resultado2)
print(resultado2)

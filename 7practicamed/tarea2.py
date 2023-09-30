"""2.Crea una clase ValidadorDeEdad que tenga un método validar para verificar si una edad
ingresada es un número entero válido. Utiliza el manejo de excepciones para manejar la
excepción ValueError que se levanta cuando el valor ingresado no es un entero."""

class ValidadorDeEdad:
    def validar(self, edad):
        try:
            edad_entero = int(edad)
            return True, edad_entero
        except ValueError:
            return False, None


validador = ValidadorDeEdad()

Edad = input("Ingrese su edad: ")
valido, edad = validador.validar(Edad)

if valido:
    print("La edad ingresada es correcta")
else:
    print("La edad ingresada no es un número entero.")

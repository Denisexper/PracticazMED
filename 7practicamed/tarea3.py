"""3.Crea una clase ValidadorContraseña que tenga un método validar para verificar si una
contraseña cumple con cierta longitud mínima. Utiliza el manejo de excepciones para
indicar si la contraseña es válida o no."""

class ValidadorContraseña:
    def __init__(self, longitud_minima):
        self.longitud_minima = longitud_minima

    def validar(self, contraseña):
        try:
            if len(contraseña) >= self.longitud_minima:
                return "Contraseña válida."
            else:
                raise ValueError("La contraseña es demasiado corta.")
        except ValueError as e:
            return str(e)


validador = ValidadorContraseña(8)

contraseña = input("Ingrese su contraseña: ")
validamos = validador.validar(contraseña)

print(validamos)

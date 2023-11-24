"""Diseña una clase llamada Biblioteca que utilice una pila para gestionar libros prestados.
Implementa métodos para prestar, devolver y mostrar el estado de la pila. Crea una
instancia de la clase y realiza operaciones de préstamo y devolución con libros específicos
como "Cien años de soledad" o "Don Quijote de la Mancha". Imprime mensajes
informativos para cada operación y muestra el estado de la pila después de ciertas
acciones."""

class Biblioteca:
    def __init__(self):
        self.pila_libros = []

    def prestar_libro(self, libro):
        self.pila_libros.append(libro)
        print(f"Libro prestado: {libro}")

    def devolver_libro(self):
        if not self.pila_libros:
            print("No hay libros para devolver.")
        else:
            libro_devuelto = self.pila_libros.pop()
            print(f"Libro devuelto: {libro_devuelto}")

    def mostrar_estado(self):
        if not self.pila_libros:
            print("La biblioteca está vacía.")
        else:
            print("Libros prestados:")
            for libro in reversed(self.pila_libros):
                print(f"- {libro}")

biblioteca = Biblioteca()

biblioteca.prestar_libro("Cien años de soledad")
biblioteca.prestar_libro("Don Quijote de la Mancha")

biblioteca.mostrar_estado()

biblioteca.devolver_libro()

biblioteca.mostrar_estado()

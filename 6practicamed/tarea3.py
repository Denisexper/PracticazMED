"""Elabore una clase estudiante, defina los atributos nombre, apellido, carnet y
carrera. Utilice un constructor para inicializar los atributos, ademas elabore
funciones para actualizar los valores de los atributos (nombre, apellido, carnet y
carrera)."""


class Estudiante:
    def __init__(self, nombre, apellido, carnet, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.carrera = carrera

    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def actualizar_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def actualizar_carnet(self, nuevo_carnet):
        self.carnet = nuevo_carnet

    def actualizar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

 
estudiante1 = Estudiante("Denis", "Vasquez", "12345", "Ingeniería desarollo de software")
print(estudiante1.nombre, estudiante1.apellido, estudiante1.carnet, estudiante1.carrera)

estudiante1.actualizar_nombre("Alexander")
estudiante1.actualizar_carrera("Ciencias de la Computación")
print(estudiante1.nombre, estudiante1.apellido, estudiante1.carnet, estudiante1.carrera)

class Estudiante:
    def __init__(self, nombre, apellido, carnet, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet_estudiante = carnet
        self.carrera_estudiante = carrera

    def Actualizar_Imfo(self, NuevoNombre, NuevoApellido, NuevoCarnet, NuevaCarrera):
        self.nombre = NuevoNombre
        print(f"Nombre actualizado: {self.nombre}")

        self.apellido = NuevoApellido
        print(f"Apellido actualizado: {self.apellido}")

        self.carnet_estudiante = NuevoCarnet
        print(f"Carnet actualizado: {self.carnet_estudiante}")

        self.carrera_estudiante = NuevaCarrera
        print(f"Carrera actualizada: {self.carrera_estudiante}")

    def MostrarImformacion(self):
        print("IMFORMACION DEL ESTUDIANTE")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Carnet: {self.carnet_estudiante}")
        print(f"Carrera: {self.carrera_estudiante}")

Estudiante1 = Estudiante("Daniel", "Guevara", "U20227845", "Ingenieria Software" )
print(Estudiante1.MostrarImformacion())
Estudiante1.Actualizar_Imfo("Denis", "Vasquez", "U20220066", "ING Software")
print(Estudiante1.MostrarImformacion)
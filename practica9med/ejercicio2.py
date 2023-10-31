class Cuenta_Usuario:
    def __init__(self, nombre, Saldo_Inicial = 0):
        self.nombre = nombre
        self.saldo = Saldo_Inicial

    def Consultar(self):
        print(f"El saldo de {self.nombre} es: ${self.saldo}")

    def Depositar(self,cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print("El deposito se realizo con exito")

    def Retirar(self,cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print("El retiro se realizo con exito")

        elif cantidad <= 0:
            print("La cantidad debe ser mayor a cero")

        else:
            print("No hay suficiente dinero en la cuenta para el retiro")

Usuario1 = Cuenta_Usuario("Andres", 100)

Usuario1.Consultar()
Usuario1.Depositar(50)
Usuario1.Retirar(20)


       
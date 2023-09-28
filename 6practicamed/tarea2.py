class Usuario:
    def __init__(self, nombre, apellido, correo, saldo_inicial):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito exitoso. Saldo actual: ${self.saldo}"
        else:
            return "La cantidad de depósito debe ser mayor que cero."

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                return f"Retiro exitoso. Saldo actual: ${self.saldo}"
            else:
                return "Saldo insuficiente para realizar el retiro."
        else:
            return "La cantidad de retiro debe ser mayor que cero."

    def consultar_saldo(self):
        return f"Saldo actual: ${self.saldo}"

# Ejemplo de uso:
usuario1 = Usuario("Juan", "Perez", "juan@example.com", 1000.0)
print(usuario1.consultar_saldo())
print(usuario1.depositar(500.0))
print(usuario1.retirar(200.0))
print(usuario1.consultar_saldo())
print(usuario1.retirar(1500.0))


        
        
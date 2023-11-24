"""Diseña un programa en Python que simule la atención de clientes en un banco. La atención
debe seguir el principio "primero en llegar, primero en ser atendido" (FIFO - First In, First
Out) utilizando una estructura de cola"""

from collections import deque

class Banco:
    def __init__(self):
        self.cola_clientes = deque()

    def llegada_cliente(self, cliente):
        self.cola_clientes.append(cliente)
        print(f"Cliente {cliente} llegó al banco. En espera.")

    def atender_cliente(self):
        if not self.cola_clientes:
            print("No hay clientes en espera.")
        else:
            cliente_atendido = self.cola_clientes.popleft()
            print(f"Atendiendo al cliente {cliente_atendido}.")

    def mostrar_cola(self):
        if not self.cola_clientes:
            print("No hay clientes en cola.")
        else:
            print("Clientes en cola:")
            for cliente in self.cola_clientes:
                print(f"- {cliente}")

banco = Banco()

banco.llegada_cliente("Cliente1")
banco.llegada_cliente("Cliente2")
banco.llegada_cliente("Cliente3")

banco.mostrar_cola()

banco.atender_cliente()
banco.atender_cliente()

banco.mostrar_cola()

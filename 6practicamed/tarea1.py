class Articulo:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def vender(self, cantidad_vendida):
        if cantidad_vendida <= 0:
            return "La cantidad vendida debe ser mayor que cero."
        elif cantidad_vendida > self.cantidad:
            return "No hay suficiente stock para la venta."
        else:
            self.cantidad -= cantidad_vendida
            total_venta = cantidad_vendida * self.precio
            return f"Venta exitosa: {cantidad_vendida} {self.nombre} vendidos por ${total_venta}"

    def obtener_stock(self):
        return f"Stock disponible de {self.nombre}: {self.cantidad}"


articulo1 = Articulo("Camiseta", 34, 10.99)
print(articulo1.obtener_stock())
print(articulo1.vender(10))
print(articulo1.obtener_stock())
print(articulo1.vender(60))
print(articulo1.vender(-5))



class Articulo:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad    
        self.precio = precio

    def Comprar(self, cantidadVenta):
        if cantidadVenta > self.cantidad:
            print("No hay suficientes articulos")
            print(f"Articulos disponibles {self.cantidad}")

        else:
            self.cantidad -= cantidadVenta
            print("Venta exitosa!!")

articulo1 = Articulo("short", 3, 10)
articulo2 = Articulo("t-shirt", 5, 20)

print(articulo1.Comprar(10))


 

  

        

    
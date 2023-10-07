"""Crea un programa que solicite al usuario que ingrese una serie de nombres y escriba
esos nombres en un archivo llamado "nombres.txt", uno por línea"""

"""nombres = input("Ingresa los nombres que deseas agregar: ")
agregar = open("archivo2.txt", "w")

agregar.write(nombres + "\n")
agregar.close

print("Los nombres se agregaron correctamente")"""

with open("archivo2.txt", "w") as archivo:
    while True:
        nombre = input("Ingresa un nombre (o presiona Enter para terminar): ")
        if nombre == "":
            break
        archivo.write(nombre + "\n")

print("Los nombres se han guardado en el archivo 'archivo2.txt'.")

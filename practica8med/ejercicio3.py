try:
    with open("archivoinexistente.txt", "r") as archivo:
        contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)
except FileNotFoundError:
    print("El archivo no se pudo encontrar. Verifica el nombre o la ruta del archivo.")
except Exception as e:
    print("Se ha producido un error:", str(e))

"""Escribe un programa que abra un archivo de texto llamado "archivo.txt" en modo
lectura, lo lea línea por línea y lo muestre en la pantalla."""

lectura = open("archivo.txt", "r")
open = lectura.readlines()
print(open)
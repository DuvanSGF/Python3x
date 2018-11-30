""" Ejemplo que muestra un programa que analiza un archivo
"""
# Aqui muestra como el archivo puede ser abierto y leido
filename = input("Enter a filename: ")

with open(filename) as f:
    text = f.read()

print(text)



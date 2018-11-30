""" Ejemplo que muestra un programa que analiza un archivo
"""
# Aqui muestra un afuncion que cuenta cuantas veces un caracter aparee en una cadena

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

filename = input("Enter a filename: ")

with open(filename) as f:
    text = f.read()

print(count_char(text, "r"))


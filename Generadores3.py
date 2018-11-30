"""
Los generadores finitos pueden ser convertidos en listas
al pasalor como argumentos de la funcion list
"""

# Ejercicio

def make_name():
    name =""
    for ch in "Duvan":
        name +=ch
        yield name
print(list(make_name()))
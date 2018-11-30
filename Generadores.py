"""
Los generadores son un tipo de iterable, como las listas o las tuplas.
A diferencia de las listas, no permiten indexar con indeces arbitrarios, pero pueden aun ser iterados
con el bucle for .
Pueden ser creados utilizado funciones y la sentencia Yield
"""

def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1
for i in countdown():
    print(i)

"""
La sentencia yield es utilizada para
definir un generador, reemplazando el retorno de una funcion para
proveer un resultado a su llamador sin destruir las variables locales.
"""

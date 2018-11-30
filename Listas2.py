"""
Una lista puede contener datos de todo tipo, lo que incluye cadenas,
numeros y hasta otras listas. Ademas, dentro de una lista puede mezclar tipos de Datos.

Para Acceder al contenido de una Lista dentro de otra, se pone un indice acontinuacion del otro:

"""

lista = [["1", "2", "3"], ["Uno", "Dos", "Tres"],"Hola"]

# Si quiero imprimir Dos
print lista[1][1]

# si quiero imprimir 3
print lista[0][2]
print lista[2][3]
print lista[1][0]

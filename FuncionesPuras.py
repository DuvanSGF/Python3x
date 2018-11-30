"""
Las funciones puras no tienen efectos secundarios y devuelven un valor que depende unicamente de susu argumentos A son
las funciones en las matematicas:
las funcion cosX puede, para el mismo valor de X siempre devolvera el mismo resultado.

"""

# Funcion Pura:
def pure_function(x, y):
    temp = x + 2*y
    return temp / (2*x + y)

# Funcion Impura :: No es pura porque cambió el estado de some_list
some_list[]
def impure(arg):
    some_list.append(arg)

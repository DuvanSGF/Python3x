"""
La recursion tambien puede ser indirecta. una funcion
puede llamar a una segunda, que a su vez llama a la primera, que llama a una segunda, a si sucesivamente.
Esto puede ocurrir con cualquier cantidad de funciones
Acontinuacion vamos a ver un ejemplo:
"""

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_even(23))



# Ejercicio

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
print(fib(4))

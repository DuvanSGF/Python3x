"""
La programacion funcional es un estilo de programacion que (como dice su nnombre gira en torno de funciones)

Se utiliaza las funciones de orden superior.
"""

def apply_three_times(func, arg):
    return func(func(func(arg)))

def add_ten(x):
    return x + 50

print(apply_three_times(add_ten, 10))

# 160


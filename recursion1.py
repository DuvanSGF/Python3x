"""
Las funciones recursivas pueden ser infinitas,
al igual que los bucles while. Estas ocurre cuando olvidas implementar el caso base.

Acontinuacion vamos a ver un ejemplo:
"""

def sum_to(x):
    return x + sum_to(x-1)
print(sum_to(5))
"""
La recursion es un concepto muy importante en la programacion funcional.
Lo fundamental de la recursion es la autoreferencia-funciones que se llaman a si mismas. Se utilizan
para resolver problemas que pueden ser divididos en subproblemas mas sencillos del mismo tipo.

Un ejemplo clasico de una Funcion que es implementada recursivamente es la funcion factorial, que encuentra
el producto de todos los enteros positivos por debajo de un numero especifico por ejemplo 5! = 5*4!, 4!=4*3!, 3!= 3*2!..
genrelamente n! = n * (n-1)!
es mas 1I = 1. Esto se conoce como el caso base.
ya que puede ser calculado sin realizar mas operaciones factoriales.

Acontinuacion vamos a ver un ejemplo:
"""

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))
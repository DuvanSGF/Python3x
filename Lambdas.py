"""
Las funciones lambda recibem su nombre del calculó Lambda, el cual
es un modelo computacional inventado por Alonzo Church.

Las funciones creadas utilizando la sintaxis lambda son conocidas como
Funciones Anonimas

"""

def my_func(f, arg):
    return f(arg)

my_func(lambda x: 2*x*x, 5)

"""
Las funciones lambda no son tan potentes como las funciones con nombre 
Solo pueden hacer cosas que requieren de una sola expresion - normalmente el equivalente a una sola linea
de codigo. 
ejemplo:

"""
# Named function

def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(4))

# Lambda
print((lambda x: x**2 + 5*x + 4)
(4))

"""
Las funciones lambda pueden ser asignadas a variables y ser 
utilizadas como funciones regulares.
"""
double = lambda x: x * 2
print(double(7))


# Ejercio Cual es el resultado del siguiente codigo
triple = lambda x: x*3
add = lambda x,y: x+y
print(add(triple(3), 4))
print(add(9,4))

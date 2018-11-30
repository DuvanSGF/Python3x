"""
Los decoradores ofrecen una manera de modificar funciones utilizando
otras funciones.
Esto es ideal cuando necesitas extender la funcionalidad de las
funciones que no quieres modificar.
"""

def decor(func):
    def wrap():
        print("================")
        func()
        print("================")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()
"""
Definimos una funcion Llamada decor que tiene un solo parametro 
func. Dentro de decor definimos una funcion anidada llamada wrap.
La funcion wrap imprimira una cadena, para luego llamar func() e imprimir otra cadena .
La funcion decor devuelve una funcion envolver como resultado.

Podriamos decir que la variable decorated es una version  de print_text con la version decorad 


Print_text = decor(print_text)
print_text()
"""

# Podemos tambien definir el siguiente Patron  O decorando la funcion con el simbolo Q

def print_text():
    print("hello world!")

print_text = decor(print_text)

# Es lo mismo que tener

@decor
def print_text():
    print("hello world!")

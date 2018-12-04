"""
Las clases son creadas utilizando la palabra clave
class y un bloque indentado que contiene
los metodos de una clase(los cuales son funciones).


Definimos una clase llamada Cat,
La cual tiene dos atributos: Color y legs.
Luego, la clase es utilizada para crear 3 objetos independientes de esa clase.
"""

class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)}
stumpy = Cat("brown", 3)


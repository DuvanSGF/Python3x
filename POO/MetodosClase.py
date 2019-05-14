"""
    Los metodos de clase  son distintos - son llamados por una clase que es pasada al parametro
    cls del metodo.

    Un uso comun de estos son los metodos de fabrica , los cuales instancian un objeto de la clase utilizando
    diferente parametros que aquellos normalmente pasados al constructor
    de la clase

"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

"""
    new_square es un metodo de clase y se llama en la 
    clase en vez de una instancia de la clase Devuelve un nuevo
    objeto de la clase
"""

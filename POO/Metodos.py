"""
Las clases pueden tener otros metodos
definidos para agregarles funcionalidad.
Recuerda que todos los metodos deben tener
self como su primer parametro.
Estos metodos son accedidos utilizando la misma sintaxis de punto que los atributos
"""

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")
fido = Dog("Luigi", "Brown")
print(fido.name)
fido.bark()

"""
Las clases pueden tener atributos de clase
tambien, creados al asignar variables dentro del cuerpo
de una clase o la clase misma.
"""

class Dog:
    legs = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")


fido = Dog("Luigi", "Brown")
print(fido.legs)
print(Dog.legs)
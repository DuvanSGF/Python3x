"""
La herencia brinda una manera de compartir funcionalidades entre clases
Imaginate varias clases, Cat, Dog, Rabbit y asi sucesivamente. Aunque
presenten algunas diferencias entre si (Solo Dog puede que tenga un metodo bark)
Son propensos a ser parecidos en otros ( Todos tienen los atributos color y name)
Este parecido puede ser expresado haciendo Que todos hereden de una Superclase Animal
que contiene funcionalidades compartidas .
Para heredar de una clase desde otra clase, coloca el nombre de la superclase entre
parentesis luego del nombre de la clase.

"""

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("purr...")

class Dog(Animal):
    def bark(self):
        print("Woof!")


luigui = Dog("Luigui", "brown")
print(luigui.color)
luigui.bark()

"""
Una clase que hereda de otra clase se le llama
subclase.
Una clase de la cual se hereda se le llama
superclase.
Si una clase hereda de otra con los mismos atributos o metodos, los sobreescribe
"""

class A:
    def method(self):
        print(1)

class B(A):
    def method(self):
        print(2)

B().method()
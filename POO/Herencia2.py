"""
La funcion super es una util funcion relacionada
a la herencia que hace referencia a la clase
padre. Puede ser utilizada para encontrar un metodo
con un determinado nombre en la superclase objeto.
"""

class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()

# super().spam() llama al metodo spam de la superclase

# Ejercicio

class Animal:
    def sound(self):
        print("I'm a new animal")

class Dog(Animal):
    def sound(self):
        print("gau")

class Cat(Animal):
    def meow(self):
        print("meow")

class imitador(Animal):
    def sound(self):
        print("hahah")
        super().sound()

imitador().sound()














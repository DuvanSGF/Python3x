"""
Los metodos magicos son metodos especiales que tienen doble
guion bajo al principio y al final de sus nombres.

Son utilizados para crear funcionalidades que no pueden ser representadas en
un metodo regular.
"""

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3,9)
result = first + secondMetodosMagicos.py
print(result.x)
print(result.y)

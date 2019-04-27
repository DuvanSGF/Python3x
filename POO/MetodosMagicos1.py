"""
Metodos Magicos para operadores comunes

__sub__ para -
__mul__ para *
__truediv__ /
__floordiv__ //
__mod__ para %
__pow__ para **
__and__ para ^
__or__ para |

"""
class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello World!")
programmer = SpecialString("Ing. Duvan Mejia")
languague = SpecialString("Python 3.6")
print(spam / hello)
print(programmer /languague)

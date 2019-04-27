"""
Python ofrece metodos magicos para comparaciones

__it__ para <
__le__ para <=
__eq__ ==
__ne__ !=
__gt__ para >
__ge__ para >=


si __ne__ no esta implementado, devuelve el opuesto de __eq__.

Note:
    No hay ninguna otra relacion entre los otros operadores
"""
class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index]\
                     + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialString("spam")
languague = SpecialString("Python 3.6")
spam > languague

"""
>spam>Python 3.6
P>spam>ython 3.6
Py>spam>thon 3.6
Pyt>spam>hon 3.6
Pyth>spam>on 3.6
Pytho>spam>n 3.6
Python>spam> 3.6
Python >spam>3.6
Python 3>spam>.6
Python 3.>spam>6
Python 3.6>spam>

"""

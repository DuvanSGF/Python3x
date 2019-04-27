"""
Hay varios metodos magicos para hacer que las clases actuen como contenedores.

__len__ para len()
__getitem__ para indexar
__seitem__ para asignar valores indexados
__delitem__ para borrar valores indexados
__iter__ para la iteracion sobre objetos (Como por ejemplo in para blucles)
__contains__ para in

otros:
__call__ para llamar objetos como funciones
__int__ , __str__ y otros similares, para convertir objetos a tipos incorporados.


"""
import random

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    # Funcion indexacion devuelve un elemento aleatorio
    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    # len() devuelve un numero aleatoria
    def __len__(self):
        return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["D", "U", "V", "A", "N"])

print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
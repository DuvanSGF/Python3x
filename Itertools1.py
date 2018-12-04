"""
Tambien hay numerosas funciones combinatorias en
iterol, tales como product y permutacion.
Etsas son utilizadas cuando quieres cumplir una tarea
con todas las combinaciones posibles de algunos elementos

"""

from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))

a = {1,2}
print(len(list(product(range(3), a))))

# Ejercicios
nums = {1,2,3,4,5,6}
nums = {0,1,2,3} & nums
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))

# Ejercicio 1

def power(x,y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)
print(power(2,3))

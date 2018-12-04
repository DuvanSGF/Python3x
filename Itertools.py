"""
Hay muchas funciones en itertools que operan
sobre iterables, de una manera similar a Map o filter.

Algunos ejemplos:
takewhile - toma un elemento de un iterable mientras que una funcion predicado permanece verdadera;
chain - combina varioas iterables en uno solo mas largo;

accumulate - devuelve un total actualizado de valores ejecutados en un iterable

"""

from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))

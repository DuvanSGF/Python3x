"""
Debido al hecho que yield produce un elemento a la vez,
los generadores no tienen las restricciones de memoria
de las listas
De hecho, pueden ser infinitas!
"""
def infinite_tens():
    while True:
        yield 10
for i in infinite_tens():
    print(i)


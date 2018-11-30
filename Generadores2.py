"""
Los generadores finitos pueden ser convertidos en listas
al pasalor como argumentos de la funcion list
"""
def numbers(x):
    for i in range(x):
        if i % 3 == 0:
            yield i
print(list(numbers(11))


# Ejercicio

def make_word():
    word =""
    for ch in "spam":
        word +=ch
        yield word
print(list(make_word()))
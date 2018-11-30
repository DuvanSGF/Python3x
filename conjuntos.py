"""
Los conjuntos son estructuras de datos parecidas a las listas
o a los diccionarios. son creados utilizados LLAVES O LA FUNCION SET.
Comparten algunas de las funcionalidades de las listas, como el uso
de in para chequear si contienen un elemento en particular.
"""

num_set = {1, 2, 3, 4}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)

"""
Los conjuntos difieren de las listas de varias formas, pero comparten varias operaciones como len.
No estan ordenados, lo cual significa que no pueden estar indexados 
No pueden contener elementos duplicados Debido a la manera que son almacenados , 
es mas rapido chequear si un elemento es parte de un conjunto, en vez de ser 
parte de una lista. 
En lugar de utilizar append para agregarle algo al conjunto, utilice add
El metodo remove elimina en elemnto especifico de un conjunto ; pop
elimina un aelemnto arbitrario

"""
print("============================")

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

print("============================")

"""
Los conjuntos pueden ser combinados
utilizando operadores matematicas.
El operador union | combina dos conjuntos
para formar uno nuevo que contiene los 
elemntos cualquiera de los dos.
El operador de interseccion & Obtiene solo los elementos que estan en ambos .
El operador de diferencia - obtine los 
elemntos que estan en el primer conjunto pero no en el segundo.
El operador de diferencia simetrica ^ obtiene los elemntos que estan en cualquiera de los conjuntos ,
pero no en ambos
"""

first = {1, 2, 3, 4, 5, 6, 7, 8, 9}
second = {2, 4, 6, 8, 10}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

print("============================")

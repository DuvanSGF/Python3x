"""
    Los metodos y atributos fuertemente privados tienen doble guion bajo al principio
    de sus nombres. Esto hacen que sus nombres sean decorados, lo cual significa que no pueden ser accdidos desde afuera de la
    clase.

"""

class Duvan:
    __edad = 20
    def print_edad(self):
        print(self.__edad)

d = Duvan()
d.print_edad()
print(d._Duvan__edad)
print(d.__edad)
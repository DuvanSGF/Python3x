"""
El metodo __init__ es el mas importante de una clase.
Es llamado cuando una instancia (objeto) de una clase es creada, utilizando el nombre de una clase como funcion.

Todos los metodos deben tener SELF como su primer parametro, aunque no sea pasado
explicitamente, Python agrega el argumento SELF a lista por ti, no necesitas incluirlo cuando llamas
a los metodos. Dentro de la definicion de un Metodo, self se refiere a la instancia que esta llamando al metodo.

Las instancias de una clase tienen atributos, los cuales
son pedazos de datos asociados a ellas.
En este ejemplo, las instancias de Cat tiene los atributos color y legs. Estos pueden ser accedidos
al poner un punto y el nombredel atributo luego del nombre de una instancia.
En un metodo __INIT__ , self.attributte pueden entonces ser utilizados para fijar un valor inicial los atributos

Ejemplo:
"""

class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
print(felix.color)
print(felix.legs)

"""
En este Ejemplo, el metodo __init__ recibe dos argumentos y los asigna  a los atributos del objeto. 
El método __init__ es llamado el constructor de la clase.
"""

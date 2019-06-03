"""
Las expresiones regulares en pyhton pueden ser accedidas
utilizando el modulo re, el cual es parte de la biblioteca estandar.

la funcion re.match puede ser utilizada para ver si corresponde al principio
de una cadena.

"""

import re

pattern = r"In" #Aqui se debe empezar con esta letra, de lo contrario no hace el macth

if re.match(pattern,
            "InGodWeTrust"):
    print("match")
else:
    print("no match")

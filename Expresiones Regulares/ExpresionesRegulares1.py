"""
Otras funciones para corresponder patrones son
re.search y re.findall

La funcion re.search encuentra una correspondencia de un patron en cualquier parte
de la cadena

La funcion re.findall devuelve una lista con todas las subcadenas que coinciden con un patron.


"""

import re

pattern = r"God" #Aqui se debe empezar con esta letra, de lo contrario no hace el macth

if re.match(pattern,
            "InGodWeTrust"):
    print("match")
else:
    print("no match")
    #No match

if re.search(pattern,
             "InGodWeTrust"):
    print("match")
else:
    print("no match")
    #Match : Aqui la busca en la frase

print(re.findall(pattern,
                 "InGodWeTrustGod"))#Aqui Imprime las veces enque esta la palabra
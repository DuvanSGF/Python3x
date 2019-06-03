
import re

pattern = r"God"

match = re.search(pattern,
             "InGodWeTrust")
if match:
    print(match.group()) #Palabra
    print(match.start()) #Empieza despued de la letra 2
    print(match.end()) #Termina en la posicion 5
    print(match.span())#La palabra esta ubicada entre la letra 2 y la 5.

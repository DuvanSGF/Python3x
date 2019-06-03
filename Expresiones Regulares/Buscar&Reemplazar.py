"""
Uno de los metodos re mas importantes que utilizan expresiones regulares es sub.

Sintaxis:

re.sub(pattern, repl, string, max=0)




Este metodo reemplaza todas las ocurrencias de un pattern con repl, sustituyendo
todas las ocurrencias hasta que max sea provisto. Este método devuelve una cadena modificada
"""

import re

str = "Hello There!  My name is Duván , I'm a Software Engineer. Hi Ing. Duván."
pattern = r"Duván"
newstr = re.sub(pattern, "Karla", str)
pattern = r"Software Engineer"
newstr1 = re.sub(pattern, "politologue", newstr)
pattern = r"Ing."
newstr2 = re.sub(pattern, "Miss", newstr1)
print(newstr2) # Hello There!  My name is Karla , I'm a politologue. Hi Miss Karla.
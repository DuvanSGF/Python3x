"""
Son aquellas que nos sirve para efectuar operaciones con valores logicos y retornan
siempre un valor boleano TRUE o FALSE

and (Y logica)
or (o Logica)
not (Negacion)
"""

resultado = 3 == 2
print resultado
# 3 no es igual a 2, por lo que es falso

print True and True
# Algo que es "cierto y cierto" es cierto

print True and resultado
# algo que es "cierto y falso" es falso

print not True
# "No cierto " es falso

print False or resultado
# algo que es "falso o falso"  es falso

print not False
# "No es false" es Verdadero



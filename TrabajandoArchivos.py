"""
Es bueno asegurar los archivos sean siempre cerrados luegos de
que sean utilizados .
"""
try:
    f = open("Prueba.txt")
    print(f.read())
finally:
    f.close()
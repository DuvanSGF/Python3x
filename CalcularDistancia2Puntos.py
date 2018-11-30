import math
print("Va a calcular la distancia entre 2 puntos ")
x1 = float(input("X1: "))
x2 = float(input("X2: "))
y1 = float(input("Y1: "))
y2 = float(input("Y2: "))
raiz = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print("La distancia es :", raiz)

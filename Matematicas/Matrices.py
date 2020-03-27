# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:13:34 2020

@author: Mr Mejia
"""
import numpy
import sys
print ("Este programa calculara la operacion estre matrices")
r1=int(input('Numero de filas de la matriz 1: '))
c1=int(input('Numero de columnas de la matriz 1: '))
r2=int(input('Numero de filas de la matriz 2: '))
c2=int(input('Numero de columnas de la matriz 2: '))
#Verificar si se puede hacer la multiplicacion
# Numero de columnas matriz 1 = numero de filas matriz 2
if (c1 != r2):
    print("No se puede hacer la mutiplicacion de matrices")
    sys.exit()

matriz1 = numpy.zeros((r1,c1))
matriz2 = numpy.zeros((r2,c2))
matrizr = numpy.zeros((r1,c2))

print("Introduce los elemntos de la matriz 1: ")
for r in range (0, r1):
    for c in range (0, c1):
        matriz1[r, c] = input ("Elemnto a ["+str(r+1)+str(c+1)+"]")
    
print("Introduce los elemntos de la matriz 2: ")
for r in range (0, r2):
    for c in range (0, c2):
        matriz2[r, c] = input ("Elemnto b ["+str(r+1)+str(c+1)+"]")
               
# Operacion de las Multiplicaciones
for r in range (0, r1):
    for c in range (0, c2):
        for m in range (0, r2):
            matrizr[r,c]+=matriz1[r,m] * matriz2[m,c]
print (matrizr)
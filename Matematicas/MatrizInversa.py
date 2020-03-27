# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:32:30 2020

@author: Mr Mejia
"""
# Segunda Matriz 
from numpy import matrix 
from scipy import linalg
A=matrix([[1, 2], [1, 3]])
c=matrix([[3, 2], [4, 5]])
a = matrix([[1, 1], [3, 4]])
b = matrix([[2, 1], [1, 1]])
print (" Suma de  A + B")
print (a+b)
print ("Inversa de C:")
print(linalg.inv(c))
print ("La Solucion del sistema de ecuaciones: ")
j = (linalg.inv(c)*A)
print (j)


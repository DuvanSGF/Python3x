# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:49:38 2020

@author: Mr Mejia
"""

def poli(x):
    y = pow(x,2)-3.0*x-4
    return (y)

def deri(x):
    d=(2*x)-3
    return (d)

print ("Método de Newton-Raphson") 
x=float(input('Introduce el valor de inicio '))
erroru=float(input('Introduce el error '))
raiz=[ ]
raiz.insert(0,0)
i=0
error = 1
while abs(error) > erroru:
    x1=x-(poli(x)/deri(x))
    raiz.append(x1)
    i = i + 1
    x = x1
    error=(raiz[i]-raiz[i-1])/raiz[i]
    print (x)

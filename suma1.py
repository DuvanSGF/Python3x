import json
numero1 = 4
numero2 = 5

suma = (numero1 + numero2)

print("La suma es: " + str(suma))


tabla = {'Duvan': 3214756394, 'Karla': 32147869, 'Colleen': 182484515}
for nombre, telefono in tabla.items():
    print('{0:10} ==> {1:10d}'.format(nombre, telefono))



json.dumps([1, 'simple', 'lista'])


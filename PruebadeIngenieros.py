"""
    Ejercicio NP-HARD
Autores:
    * Cristian Julian Andrade
    * Sergio Daniel Velasquez Pobre.
Descripcion:
    *Ejercicio para encontrar la ruta mas cercana desde
    un punto de origen hasta un punto final.
    *Realizado en Python.
"""
ciudades = "abcdefghij"
space = " "
validacion = False

ciudadA = {"a": -1, "b": 106, "c": 60, "d": 32, "e": 46, "f": 116, "g": 60, "h": 39, "i": 105, "j": 100}
ciudadB = {"a": 120, "b": -1, "c": 76, "d": 106, "e": 118, "f": 31, "g": 66, "h": 131, "i": 108, "j": 78}
ciudadC = {"a": 117, "b": 52, "c": -1, "d": 91, "e": 36, "f": 54, "g": 102, "h": 68, "i": 99, "j": 38}
ciudadD = {"a": 46, "b": 122, "c": 135, "d": -1, "e": 128, "f": 129, "g": 110, "h": 121, "i": 37, "j": 115}
ciudadE = {"a": 83, "b": 48, "c": 119, "d": 97, "e": -1, "f": 103, "g": 133, "h": 43, "i": 122, "j": 47}
ciudadF = {"a": 143, "b": 100, "c": 87, "d": 138, "e": 150, "f": -1, "g": 49, "h": 71, "i": 98, "j": 99}
ciudadG = {"a": 86, "b": 94, "c": 105, "d": 97, "e": 60, "f": 145, "g": -1, "h": 33, "i": 138, "j": 114}
ciudadH = {"a": 41, "b": 42, "c": 127, "d": 57, "e": 47, "f": 70, "g": 71, "h": -1, "i": 45, "j": 144}
ciudadI = {"a": 75, "b": 140, "c": 67, "d": 46, "e": 61, "f": 46, "g": 125, "h": 148, "i": -1, "j": 49}
ciudadJ = {"a": 144, "b": 38, "c": 116, "d": 109, "e": 102, "f": 120, "g": 128, "h": 64, "i": 125, "j": -1}
matriz = {"a": ciudadA, "b": ciudadB, "c": ciudadC, "d": ciudadD, "e": ciudadE, "f": ciudadF, "g": ciudadG,
          "h": ciudadH, "i": ciudadI, "j": ciudadJ}

print(space * 5, "A", space * 3, "B", space * 3, "C", space * 3, "D", space * 3, "E", space * 3, "F", space * 3, "G",
      space * 3, "H", space * 3, "I", space * 3, "J")

for i in range(0, 10, 1):
    print(ciudades[i], " ", repr(matriz[ciudades[i]]["a"]).center(5),
          repr(matriz[ciudades[i]]["b"]).center(5),
          repr(matriz[ciudades[i]]["c"]).center(5),
          repr(matriz[ciudades[i]]["d"]).center(5),
          repr(matriz[ciudades[i]]["e"]).center(5),
          repr(matriz[ciudades[i]]["f"]).center(5),
          repr(matriz[ciudades[i]]["g"]).center(5),
          repr(matriz[ciudades[i]]["h"]).center(5),
          repr(matriz[ciudades[i]]["i"]).center(5),
          repr(matriz[ciudades[i]]["j"]).center(5))

print(3 * space)
while not validacion:
    try:
        # Se inician algunas variables para su posterior utilizacion
        origen = input("Ingrese la ciudad de origen: ").lower().strip()
        destino = input("Ingrese la ciudad de destino: ").lower().strip()

        distanciaDirecta = matriz[origen][destino]
        print("La distancia directa entre ", origen, " y ", destino, " es ", distanciaDirecta)
        noVisitadas = list(ciudades)
        sigo = True
        current = origen
        nextCity = ""
        ruta =[]
        if len(origen) == 1 and len(destino) == 1:
            if (origen in ciudades) and (destino in ciudades) and (destino != origen):
                validacion = True
        if validacion:
            # Encuentra la ruta mas corta a partir de aqui.
            while sigo:
                for i in range(len(noVisitadas)):
                    if noVisitadas[i] != current:
                        if matriz[current][noVisitadas[i]] <= matriz[origen][destino]:
                            if current == origen:
                                camino = origen +" - "+ noVisitadas[i]
                                ruta.append([matriz[current][noVisitadas[i]], camino])
                                ruta.sort()
                            else:
                                distancia = ruta[0][0] + matriz[current][noVisitadas[i]]
                                if distancia < matriz[origen][destino]:
                                    camino = ruta[0][1] +" - "+ noVisitadas[i]
                                    ruta.append([distancia, camino])
                                    ruta.sort()
                if ruta[0][0] <= distanciaDirecta and ruta[0][1][len(ruta[0][1]) - 1] == destino:
                    sigo = False
                else:
                    pop = True
                    noVisitadas.remove(current)
                    if current != origen:
                        ruta.pop(0)
                    while pop:
                        for i in range(len(noVisitadas)):
                            if noVisitadas[i] == ruta[0][1][len(ruta[0][1]) - 1]:
                                pop = False
                        if pop:
                            ruta.pop(0)
                    nextCity = ruta[0][1][len(ruta[0][1]) - 1]
                    current = nextCity

            print("El camino mas corto es por ", ruta[0][1], "y la distancia a recorrer es de ", ruta[0][0])
            print("Desea buscar otra ruta")
            decision = input("[s/n] : ").lower().strip()
            if decision == 's':
                validacion = False
        else:
            print("Ocurrio un error, ingrese datos correctos por favor.")
    except:
        print("Ocurrio un error.")
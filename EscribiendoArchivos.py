file = open("Prueba.txt", "w")
file.write("This has been written to a file : Pd : Duvan")
file.close()

file = open("longitud.txt", "r")
print(file.read())
file.close()

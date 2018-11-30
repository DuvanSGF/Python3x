msg = "Hello Tita"
file = open("Prueba.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()
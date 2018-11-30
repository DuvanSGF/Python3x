file = open("filename.txt", "r")
print(file.readlines())
file.close()

file = open("filename.txt", "r")
for line in file:
    print(line)

file.close()
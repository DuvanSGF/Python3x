print("******** Calculadora para acabar el año ******** ")
mes = int(input("Ingresa  el mes:"))
dia = int(input("Ingresa  el dia:"))
hora = int(input("Ingresa  el hora:"))
minutos = int(input("Ingresa  el minutos:"))

mes1 = 12 - mes
dia1 = 31 - dia
hora1 = 24 - hora
minutos1 = 60 - minutos

print("Lo que falta para que se acabe el año es  : ", mes1, " meses y ", dia1, " dias con ", hora1, " horas y ", minutos1, " minutos")


print("******** Calculadora para acabar el año ******** ")
mes = int(input("Ingresa  el mes:"))
dia = int(input("Ingresa  el dia:"))
hora = int(input("Ingresa  el hora:"))
minutos = int(input("Ingresa  el minutos:"))

mes1 = 12 - mes
dia1 = 30 - dia
hora1 = 24 - hora
minutos1 = 60 - minutos

mess = [4, 5, 7, 8, 10]
if mes1 in mess:
    print("Lo que falta para que se acabe el año es  : ", mes1, " meses y ", dia1, " dias con ", hora1, " horas y ",
          minutos1, " minutos")
else:
    print("Lo que falta para que se acabe el año es  : ", mes1, " meses y ", dia1+1, " dias con ", hora1, " horas y ",
          minutos1, " minutos")
print("¡Hasta la próxima!")



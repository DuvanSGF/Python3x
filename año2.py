def lunes():
	print('lunes')

def martes():
	print('martes')

def miercoles():
	print('miércoles')

def jueves():
	print('jueves')

def viernes():
	print('viernes')

def sabado():
	print('sábado')

def domingo():
	print('domingo')

def error():
	print('error')

switch_semana = {
	1: lunes,
	2: martes,
	3: miercoles,
	4: jueves,
	5: viernes,
	6: sabado,
	7: domingo
}

dia = 8

#tomamos la función asociada a la variable y la invocamos
switch_semana.get(dia, domingo())
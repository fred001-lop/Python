hour = int(input("Ingrese las horas"))
mins = int(input("Ingrese los minutos"))
dura = int(input("Ingrese la duracion"))

mins = mins + dura
hour = hour + mins // 60
mins = mins % 60 
hour = hour % 24

print (hour, ":", mins, sep="")
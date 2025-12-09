

nombre = str(input("Ingrese Espatifilo: "))

if nombre == "ESPATIFILO":
    result = ("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
elif nombre == "espatifilo":
    result = ("No, ¡quiero un gran Espatifilo!")
else:
    result = ("¡Espatifilo!, ¡No  " + nombre + "!")
print(result)
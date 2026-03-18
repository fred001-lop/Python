largest = -999999999

#para ingresar numero
number = int(input("Intruduce un numero o escribe -1 para detener: "))


#si el numero no es igual a -1, continuaremos
while number != -1:
    #Es el numero mas grande que el valor de largest?
    if number > largest:
        #si es asi, se actualiza lartgest
        largest = number
        #ingrese el siguiente numero
    number = int(input("Introduce un numero o escribe -1 para detener"))
#imprime el numero mas grande
print("El numero mas grande es: ", largest)


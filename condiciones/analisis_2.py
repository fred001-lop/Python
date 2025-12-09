
number_1 = int(input("Ingrese el primer valor: "))
number_2 = int(input("Ingrese el primer valor: "))
number_3 = int(input("Ingrese el primer valor: "))

mayor_number = number_1


if number_2 > mayor_number:
    mayor_number = number_2

if number_3 > mayor_number:
    mayor_number = number_3

print("El numero mayor es:", mayor_number)
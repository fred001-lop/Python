
#Pedimos los numeros, estos se leeran para posteriormete utilizarse en la funcion
number_1 = int(input("Ingrese el primer numero "))
number_2 = int(input("Ingrese el segundo numero "))


#funcion

if number_1 > number_2:
    larger_number = number_1
else:
    larger_number = number_2

print("El numero mas grande es:", + larger_number)


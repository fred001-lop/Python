#Reconoce el valor mas grande
#variables
largest = -99999
counter = 0

while True: 
    number = int(input("Introduce un numero o ingresa -1 para finalizar"))
    if number == -1:
        break
    counter += 1
    if number > largest:
        largest = number
    
if counter != 0:
    print("El numero mas grande es:", largest)
else:
    print("No has ingresado ningun numero") 


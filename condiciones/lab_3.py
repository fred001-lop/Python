
year = int(input("Ingrese el año"))

if year < 1582:
    print("No esta dentro del periodo del calendario Gregoriano")
else:
    if year % 4 != 0:
        print("Ano comunn")
    elif year % 100 != 0:
        print("Anno bisiesto")
    elif year % 400 != 0:
        print("Ano comun")
    else:
        print("Ano Bisiesto")
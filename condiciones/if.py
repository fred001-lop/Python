climaEsBueno = ""
encontramosBuenRestaurante = ""
almorzaremos= ""
comeremosSandwich= ""
boletosDisponibles= ""
iremosAlCine= ""
iremosDeCompras = ""



if climaEsBueno:
    if encontramosBuenRestaurante:
        almorzaremos()
    else: 
        comeremosSandwich()
else:
    if boletosDisponibles:
        iremosAlCine()
    else:
        iremosDeCompras()

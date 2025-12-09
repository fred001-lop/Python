
imp = float(input("Ingrese su Ingreso"))


if imp < 85528:
    total = imp * 0.18 -556.02
else:
    total = (imp - 85528) * 0.32 + 14839.02
if total < 0.0:
    total = 0.0

total = round(total, 0)
print("El impuesto es:", total, "$")

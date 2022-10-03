ingreso = float(input("Introduzca el ingreso inicial: "))
interes = 0.04
primer_año = ingreso * (1 + interes)
print("Ahorro en el primer año: " + str(round(primer_año, 2)))
segundo_año = primer_año * (1 + interes)
print("Ahorro en el segundo año: " + str(round(segundo_año, 2)))
tercer_año = segundo_año * (1 + interes)
print("Ahorro en el tercer año: " + str(round(tercer_año, 2)))
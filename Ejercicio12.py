barras_de_pan = int(input("Introduzca el número de barras vendidas que no son del dia: "))
precio = 3.49
descuento = 0.6
total = barras_de_pan * precio * (1- descuento)
print("El coste de una barra del dia es " + str(precio) + "€")
print("El descuento sobre una barra no del dia es del " + str(descuento * 100) + ("%"))
print("El total a pagar es " + str(round(total, 2)) + "€")
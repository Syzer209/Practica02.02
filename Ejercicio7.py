peso = input("¿Cuanto pesas? ")
altura = input("¿Cuanto mides?")
imc = round(float(peso)/float(altura)**2,2)
print("Tu imc es: " + str(imc))
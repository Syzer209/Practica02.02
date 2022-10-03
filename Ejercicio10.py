peso_payaso = 112
peso_muñeca = 75
numero_payasos = int(input("¿Cuantos payasos desea enviar?: "))
numero_muñecas = int(input("¿Cuantas muñecas desea enviar?: "))
total = peso_payaso * numero_payasos + peso_muñeca * numero_muñecas
print("En total, el paquete pesa: " + str(total) + " gramos")
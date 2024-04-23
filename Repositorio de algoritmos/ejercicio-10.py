# Leer el número de llantas de la compra
numero_llantas = int(input("Ingrese el número de llantas de la compra: "))

# Calcular el precio unitario según la política del almacén
if numero_llantas < 6:
    precio_unitario = 240000
elif numero_llantas == 6 or numero_llantas == 7:
    precio_unitario = 221000
else:
    precio_unitario = 180000

# Calcular el valor total a pagar
valor_total = numero_llantas * precio_unitario

# Mostrar el valor que debe pagarse
print("El valor a pagar por", numero_llantas, "llantas es de $", valor_total)

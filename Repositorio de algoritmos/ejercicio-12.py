cantidad_articulos = int(input("Ingrese la cantidad de artículos: "))
precio_unitario_original = float(input("Ingrese el precio unitario original: "))

# Calcular el descuento según la cantidad de artículos
if cantidad_articulos <= 5:
    descuento = 0
elif 5 < cantidad_articulos < 10:
    descuento = 0.05
else:
    descuento = 0.08

# Calcular el precio unitario con descuento
precio_unitario_descuento = precio_unitario_original - (precio_unitario_original * descuento)

# Calcular el valor total a pagar
valor_total = cantidad_articulos * precio_unitario_descuento

# Mostrar el valor total a pagar
print("El valor total a pagar es: $", valor_total)

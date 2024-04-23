# Solicitar al empleado el tamaño de la pizza
tamaño_pizza = int(input("Ingrese el número correspondiente al tamaño de la pizza:\n1. Pequeña - $15.000\n2. Mediana - $24.000\n3. Grande - $36.000\n"))

# Solicitar al empleado el número de ingredientes adicionales
ingredientes_adicionales = int(input("Ingrese el número de ingredientes adicionales: "))

# Definir los precios base según el tamaño de la pizza
if tamaño_pizza == 1:
    precio_base = 15000
elif tamaño_pizza == 2:
    precio_base = 24000
elif tamaño_pizza == 3:
    precio_base = 36000
else:
    print("Tamaño de pizza no válido.")
    exit()

# Calcular el costo adicional por los ingredientes
costo_ingredientes = ingredientes_adicionales * 4000

# Calcular el precio total
precio_total = precio_base + costo_ingredientes

# Mostrar el precio que debe pagar el cliente
print("El precio total a pagar es: $", precio_total)

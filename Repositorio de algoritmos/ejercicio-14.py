edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su género (1 para femenino, 2 para masculino): ")

# Calcular el número de pulsaciones
if genero == '1':
    pulsaciones = (220 - edad) / 10
elif genero == '2':
    pulsaciones = (210 - edad) / 10
else:
    print("Género no válido.")
    exit()

# Mostrar el número de pulsaciones
print("El número de pulsaciones es:", pulsaciones)

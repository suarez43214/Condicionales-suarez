print("Seleccione la figura geométrica para calcular su área:")
print("1. Rectángulo")
print("2. Cuadrado")
print("3. Paralelogramo")
print("4. Rombo")
print("5. Trapecio")
print("6. Triángulo")
print("7. Triángulo Equilátero")
print("8. Triángulo Rectángulo")
print("9. Polígono Regular")

opcion = int(input("Ingrese el número correspondiente a la figura: "))

if opcion == 1:  # Rectángulo
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area = base * altura
    print("El área del rectángulo es:", area)
elif opcion == 2:  # Cuadrado
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = lado * lado
    print("El área del cuadrado es:", area)
elif opcion == 3:  # Paralelogramo
    base = float(input("Ingrese la base del paralelogramo: "))
    altura = float(input("Ingrese la altura del paralelogramo: "))
    area = base * altura
    print("El área del paralelogramo es:", area)
elif opcion == 4:  # Rombo
    diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
    diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
    area = (diagonal_mayor * diagonal_menor) / 2
    print("El área del rombo es:", area)
elif opcion == 5:  # Trapecio
    base_mayor = float(input("Ingrese la base mayor del trapecio: "))
    base_menor = float(input("Ingrese la base menor del trapecio: "))
    altura = float(input("Ingrese la altura del trapecio: "))
    area = ((base_mayor + base_menor) / 2) * altura
    print("El área del trapecio es:", area)
elif opcion == 6:  # Triángulo
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    print("El área del triángulo es:", area)
elif opcion == 7:  # Triángulo Equilátero
    lado = float(input("Ingrese el lado del triángulo equilátero: "))
    area = (math.sqrt(3) / 4) * lado ** 2
    print("El área del triángulo equilátero es:", area)
elif opcion == 8:  # Triángulo Rectángulo
    base = float(input("Ingrese la base del triángulo rectángulo: "))
    altura = float(input("Ingrese la altura del triángulo rectángulo: "))
    area = (base * altura) / 2
    print("El área del triángulo rectángulo es:", area)
elif opcion == 9:  # Polígono Regular
    perimetro = float(input("Ingrese el perímetro del polígono regular: "))
    apotema = float(input("Ingrese la apotema del polígono regular: "))
    area = (perimetro * apotema) / 2
    print("El área del polígono regular es:", area)
else:
    print("Opción no válida. Por favor, seleccione un número válido del 1 al 9.")

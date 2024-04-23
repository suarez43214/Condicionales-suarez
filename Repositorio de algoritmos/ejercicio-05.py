nota1 = float(input("Ingrese la nota 1 (0.0 - 5.0): "))
nota2 = float(input("Ingrese la nota 2 (0.0 - 5.0): "))
nota3 = float(input("Ingrese la nota 3 (0.0 - 5.0): "))
nota4 = float(input("Ingrese la nota 4 (0.0 - 5.0): "))
nota5 = float(input("Ingrese la nota 5 (0.0 - 5.0): "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if promedio >= 3.0:
    print("Aprobó")
else:
    print("No aprobó")

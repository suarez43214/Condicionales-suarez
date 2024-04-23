# Solicitar tres números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Ordenar los números en orden ascendente
if num1 <= num2:
    if num2 <= num3:
        ascendente = [num1, num2, num3]
    else:
        if num1 <= num3:
            ascendente = [num1, num3, num2]
        else:
            ascendente = [num3, num1, num2]
else:
    if num1 <= num3:
        ascendente = [num2, num1, num3]
    else:
        if num2 <= num3:
            ascendente = [num2, num3, num1]
        else:
            ascendente = [num3, num2, num1]

# Ordenar los números en orden descendente
descendente = [ascendente[2], ascendente[1], ascendente[0]]

# Imprimir los números en orden ascendente y descendente
print("Números en orden ascendente:", ascendente)
print("Números en orden descendente:", descendente)


P = float(input("Ingrese su peso en kilogramos: "))
E = float(input("Ingrese su estatura en metros: "))

# Calcular el índice de masa corporal (IMC)
IMC = P / (E * E)

# Determinar el estado según el IMC calculado
if IMC < 18.5:
    estado = "Desnutrido"
elif 18.5 <= IMC < 25:
    estado = "Normal"
elif 25 <= IMC < 30:
    estado = "Sobrepeso"
elif 30 <= IMC < 35:
    estado = "Obesidad Grado 1"
elif 35 <= IMC < 40:
    estado = "Obesidad Grado 2"
elif 40 <= IMC < 50:
    estado = "Obesidad Grado 3"
else:
    estado = "Obesidad Grado 4"

# Mostrar el estado de acuerdo al IMC
print("Su IMC es:", IMC)
print("Su estado es:", estado)

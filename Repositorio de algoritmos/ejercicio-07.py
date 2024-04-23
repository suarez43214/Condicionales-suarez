print("Menú de opciones:")
print("1. Celsius a Fahrenheit")
print("2. Celsius a Kelvin")
print("3. Celsius a Rankine")
print("4. Celsius a Réaumur")
print("5. Fahrenheit a Celsius")
print("6. Fahrenheit a Kelvin")
print("7. Fahrenheit a Rankine")
print("8. Fahrenheit a Réaumur")
opcion = int(input("Ingrese el número correspondiente a la conversión que desea realizar: "))

if opcion == 1:
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("La temperatura en grados Fahrenheit es:", fahrenheit)
elif opcion == 2:
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    kelvin = celsius + 273.15
    print("La temperatura en Kelvin es:", kelvin)
elif opcion == 3:
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    rankine = (celsius + 273.15) * 9/5
    print("La temperatura en Rankine es:", rankine)
elif opcion == 4:
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    reaumur = celsius * 4/5
    print("La temperatura en Réaumur es:", reaumur)
elif opcion == 5:
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("La temperatura en grados Celsius es:", celsius)
elif opcion == 6:
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    kelvin = (fahrenheit + 459.67) * 5/9
    print("La temperatura en Kelvin es:", kelvin)
elif opcion == 7:
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    rankine = fahrenheit + 459.67
    print("La temperatura en Rankine es:", rankine)
elif opcion == 8:
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    reaumur = (fahrenheit - 32) * 4/9
    print("La temperatura en Réaumur es:", reaumur)
else:
    print("Opción no válida. Por favor, ingrese un número válido del 1 al 8.")

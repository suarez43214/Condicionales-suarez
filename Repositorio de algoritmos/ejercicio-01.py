numero = int(input('ingrese un numero:'))

 #verificar si el numero es cero
if numero == 0:
    print('el numero ingresado es cero')
elif numero %2 == 0:
    print('el numero ingresado es par')
else:
    print('el numero ingresado es impar')
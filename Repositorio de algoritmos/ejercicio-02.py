nombre = input('ingrese su nombre por favor:')
edad = int(input('ahora ingrese su edad:'))
if edad >=100:
    print('ingrese un valor valido')
elif edad <0:
    print('ingrese un valor valido')

if edad >= 18 and edad < 100:
    print ('usted es mayor de edad')
elif edad < 18 and edad >0:
    print('usted es menor de edad')

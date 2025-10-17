# Realizar un programa que diga si un nro es par o impar
"""
numero = int(input('Ingrese un número: '))
if numero % 2 == 0:
    resultado = 'PAR'
else:
    resultado = 'IMPAR'
print(f'El número ingresado es {resultado}')
"""

# Programa que pida nombre a usuario y edad y diga si es mayor de edad
"""
nombre = input('Ingrese su nombre: ')
edad   = int(input('Ingrese su edad: '))
if edad >= 18:
      print(f'{nombre} es mayor de edad')
else:
      print(f'{nombre} es menor de edad')
"""

# Programa que genere tabla de multiplicar de un nro ingresado por el usuario del 1 al 10
"""
lista = [0,1,2,3,4,5,6,7,8,9,10]
numero_a_multiplicar = int(input('Ingrese un nro a multiplicar: '))
for n in lista:
    print(f'{numero_a_multiplicar}x{n}={numero_a_multiplicar*n}')
"""

# Usuario ingrese una palabra y un nro e imprima por pantalla la palabra tantas veces como el nro ingresado
"""
palabra = input('Ingrese una palabra: ')
nro = int(input('Ingrese un número: '))
n = 1
while  n <= nro:
    print(palabra)
    n +=1
"""

# Programa que sume los numeros ingresados por el usuario hasta que se ingrese un 0. Al final mostrar la suma por pantalla
"""
numero = 1
suma = 0
while numero != 0:
    numero = int(input(f'Ingrese números a sumar. Si desea terminar ingrese "0": '))
    suma = suma + numero

print(f'La suma de los números ingresados es: {suma}.')
"""

# Realizar un programa que pide al usuario su nombre y apellidoy en el caso de no estar la primer letra en mayuscula devolver el nombre y apellido pero con la primer letra mayúsculas
"""
nombre = input('Ingrese Nombre: ')
apellido = input('Ingrese Apellido: ')
if nombre[0].upper() != nombre[0]:
    nombre = nombre[0].upper()+nombre[1:]

if apellido[0].upper() != apellido[0]:
    apellido = apellido[0].upper()+apellido[1:]

print(f'{nombre} {apellido}')
"""

# Pedir Edad de usuario y diga si debe votar,y en caso de tener entre 16 y 18, preguntar al usuario si decide votar o no
"""
edad = int(input('Ingrese su edad para saber si debe votar: '))
if edad > 18:
    print('Debe votar')
elif edad >= 16 and edad <= 18:
    print('Usted podria votar si quisiera')
else:
    print('No puede votar')
"""

# Realizar un programa que pida al user que ingrese varios nros y que devuelva la suma del cuadrado de ellos.
"""
nro = 1
cuadrado = 0
suma = 0

while nro != 0:
    nro = int(input('Ingrese un nro para calcular el CUADRADO e ir sumando los resultados. Finalice con 0: '))
    cuadrado = nro **2
    suma = suma + cuadrado
    print(f'El cuadrado de {nro} es {cuadrado}')

print(f'La suma de los resultados del cuadrado es {suma}')
"""
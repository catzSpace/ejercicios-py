#ejercicio n°1

valor1 = float(input("ingresa un numero "))
valor2 = float(input("ingresa otro numero "))

respuesta = (f'{valor1} es mayor', f'{valor2} es mayor')[valor2 > valor1]
print(respuesta)


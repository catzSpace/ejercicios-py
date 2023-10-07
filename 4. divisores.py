#ejercicio n°4

numero = int(input("ingresa un numero: "))

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
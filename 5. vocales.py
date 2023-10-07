#ejercicio n°5

frase = input("ingresa una frase: ")

vocales = ["a", "e", "i", "o", "u"]

n = 0
for vocal in vocales:
    for letra in frase:
        if vocal == letra:
            n = n + 1

print(f"vocales: {n}")
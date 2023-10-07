#ejercicio n°8

frase = input("ingrese una frase: ")
letra = input("ingrese una letra: ")

for i in frase:
    if letra in frase:
        r = i.replace(letra, '*')
        print(r, end='', flush=True)
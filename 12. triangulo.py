try:
    n = int(input("filas: "))

    a = -1
    for i in range(1, n + 1):
        s = n - i
        d = ' '*s
        a += 1
        print(d, '*'*(i + a))
except ValueError:
    print("debes ingresar un número entero")

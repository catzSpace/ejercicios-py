n = int(input("altura: "))

for i in range(1, n + 1):
    s = n - i #numero de espacios que se escriben antes de la x
    d = ' '*s #dibujando espacios
    print(d, '*')
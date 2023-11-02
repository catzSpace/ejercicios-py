a = []

d = int(input('cuantos numeros desea agregar? '))

for i in range(d):
    b = int(input('>'))
    a.append(int(b))

print(a)

n = int(input("target: "))


#devuelve los indices de los números que suman el target dado
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == n:
            print(f"[{j},{i}]") 
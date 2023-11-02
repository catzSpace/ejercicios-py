strs = ["flower","flow","car"]
x = []
y = []
z = []
var = [x, y, z]

def extraer(): #funcion principal
    def loop(v): #extraer las dos primeras letras de las palabras de la lista
        c = 0
        for a in i:
            if c == 2:
                break
            else:
                c += 1
                v.append(a) #v = variable / parametro a recibir
                print(a)
    for i in strs:
        print(f'>{i}')
        if i == strs[0]:
            loop(x)
        if i == strs[1]:
            loop(y)
        if i == strs[2]:
            loop(z)
    #print(i)
extraer()
print(x, y ,z)

def comp():
    if x == y:
        print(end='el prefijo comun es: ')
        for i in x:
            print(end=i)
    elif x == z:
        print(end='el prefijo comun es: ')
        for i in x:
            print(end=i)
    elif z == y:
        print(end='el prefijo comun es: ')
        for i in z:
            print(end=i)
    else:
        print('no hay prefijo comun')

comp()
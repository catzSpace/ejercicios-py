s = sorted(input(': '))

mayus = ''
minus = ''
par = ''
impar = ''
numbers = '0123456789'

for i in s:
    if i.isupper():
        mayus += i
    if i.islower():
        minus += i
    if i in numbers:
        if int(i) % 2 == 0:
            par += i
        if int(i) % 2 != 0:
            impar += i

print(minus + mayus + impar + par)
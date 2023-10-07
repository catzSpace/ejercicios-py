#Hexadecimal  0	      1	     2	      3	      4	      5	     6	     7
#Decimal	0000	0001	0010	0011	0100	0101	0110	0111

def conv():
    hexa = {
        "0":"0000",
        "1":"0001",
        "2":"0010",
        "3":"0011",
        "4":"0100",
        "5":"0101",
        "6":"0110",
        "7":"0111",
        "8":"1000",
        "9":"1001",
        "A":"1010",
        "B":"1011",
        "C":"1100",
        "D":"1101",
        "E":"1110",
        "F":"1111"
    }
    n = input('ingresa un hexadecimal: ')

    print('el hexadecimal en binario es: ')
    for i in n:
        bi = hexa[i]
        print(bi, end='', flush=True)

conv()
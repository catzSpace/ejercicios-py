a = []

b = input()
n = int(input("target: "))

for i in b:
    a.append(int(i))


for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == n:
            print(f"[{j},{i}]")
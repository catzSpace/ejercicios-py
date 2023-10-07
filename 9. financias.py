#VF = VA*(1 + i)^n
#VA = VF / (1 + i)^n


def vf(ca, t, p):
    for i in range(p):
        print(f"año {i}: {ca*(1 + t / 100)**(i + 1)}")

vf(1000, 10, 3)


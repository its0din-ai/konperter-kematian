xxx = "101011.110"

sd = xxx.split('.')
xa = list(map(''.join, zip(*[iter(sd[0])]*3)))
okt = oct(int(''.join(xa[0]), 2))[2:]
okt1 = oct(int(''.join(xa[1]), 2))[2:]

oktm = oct(int(''.join(sd[1]), 2))[2:]
print(f"oktal 1 = {okt}, oktal 2 = {okt1}. oktal . = {oktm}")
yyy = str(okt) + str(okt1) + "." + str(oktm)
print(f"oktal = {yyy}")

yd = yyy.split('.')
ya = yd[0]
print(yd)

modul = []
for i in range (0, len(ya)):

    kalkul = int(ya[i]) // 2
    modul += int(ya[i]) % 2

print(modul)
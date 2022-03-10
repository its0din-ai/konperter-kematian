
print("\nKONVERSI BINER KE DESIMAL")
print("=========================")
user = input("Biner ke Desimal :: ")
listbin = user.split(' ')
listdec = []
print(f"{len(listbin) % 4}")
if len(listbin) % 4 == 0:
    print(listbin)
elif len(listbin) % 4 == 1:
    ax = "0" + listbin[0]
    print(ax)
elif len(listbin) % 4 == 2:
    ax = "00" + listbin[0]
    print(ax)
elif len(listbin) % 4 == 3:
    ax = "000" + listbin[0]
    print(ax)
#!/usr/bin/python

from tabulate import tabulate


# KONVERTER BILANGAN

import re


bins = "biner"
octs = "oktal"
decs = "desimal"
hexs = "hexa"

def main():
    print("\nKONVERTER BILANGAN")
    print("=================")
    print("1. Biner")
    print("2. Oktal")
    print("3. Desimal")
    print("4. Hexadesimal")
    print("5. Keluar")
    print("=================")
    pilih = int(input("Masukkan pilihan anda: "))
    if pilih == 1:
        submain(bins)
    elif pilih == 2:
        submain(octs)
    elif pilih == 3:
        submain(decs)
    elif pilih == 4:
        submain(hexs)
    elif pilih == 5:
        exit()
    else:
        print("\nPilihan tidak ada!")
        main()

def submain(to):
    if to == bins:
        print("\nKONVERSI BINER")
        print("===============")
        print("1. Biner ke Desimal")
        print("2. Biner ke Oktal")
        print("3. Biner ke Hexadesimal")
        print("4. Kembali")
        print("===============")
        pilih = int(input("Masukkan pilihan anda: "))
        if pilih == 1:
            bin_dec()
        elif pilih == 2:
            bin_oct()
        elif pilih == 3:
            bin_hex()
        elif pilih == 4:
            main()
        else:
            print("\nPilihan tidak ada!")
            submain(to)
    elif to == octs:
        print("\nKONVERSI OKTAL")
        print("===============")
        print("1. Oktal ke Desimal")
        print("2. Oktal ke Biner")
        print("3. Oktal ke Hexadesimal")
        print("4. Kembali")
        print("===============")
        pilih = int(input("Masukkan pilihan anda: "))
        if pilih == 1:
            oct_dec()
        elif pilih == 2:
            oct_bin()
        elif pilih == 3:
            oct_hex()
        elif pilih == 4:
            main()
        else:
            print("\nPilihan tidak ada!")
            submain(to)
    elif to == decs:
        print("\nKONVERSI DESIMAL")
        print("===============")
        print("1. Desimal ke Biner")
        print("2. Desimal ke Oktal")
        print("3. Desimal ke Hexadesimal")
        print("4. Kembali")
        print("===============")
        pilih = int(input("Masukkan pilihan anda: "))
        if pilih == 1:
            dec_bin()
        elif pilih == 2:
            dec_oct()
        elif pilih == 3:
            dec_hex()
        elif pilih == 4:
            main()
        else:
            print("\nPilihan tidak ada!")
            submain(to)
    elif to == hexs:
        print("\nKONVERSI HEXADESIMAL")
        print("====================")
        print("1. Hexadesimal ke Desimal")
        print("2. Hexadesimal ke Biner")
        print("3. Hexadesimal ke Oktal")
        print("4. Kembali")
        print("====================")
        pilih = int(input("Masukkan pilihan anda: "))
        if pilih == 1:
            hex_dec()
        elif pilih == 2:
            hex_bin()
        elif pilih == 3:
            hex_oct()
        elif pilih == 4:
            main()
        else:
            print("\nPilihan tidak ada!")
            submain(to)
    else:
        print("\nPilihan tidak ada!")
        main()


# BINARY
def bin_dec():
    print("+============[Binary to Decimal]============+")
    inputan = str(input("Masukkan bilangan Biner tanpa spacing: "))
    print("+-------------------------------------------------------------------------------------+")
    rev = inputan[::-1]
    desimal = 0
    arrr = list(rev.strip(" "))
    mult = []
    way = []
    for i in range(0, len(rev)):
        axx = int(rev[i])
        kalkul = axx*2**i
        desimal += kalkul
        mult.append(f"{kalkul}")
        way.append(f"({rev[i]}x2)^{i}")

    hasilAkhir = "+".join(mult)
    table = [arrr[::-1], way[::-1], mult[::-1]]
    print(tabulate(table, tablefmt='fancy_grid'))
    print("------------------------------------------")
    print(f"+==> Hasil dari biner {inputan} adalah {hasilAkhir} = {desimal} Desimal")
    print("+-------------------------------------------------------------------------------------+")
    submain(bins)

def bin_oct():
    print("+============[Binary to Octal]============+")
    inputan = str(input("Masukkan bilangan Biner tanpa spacing: "))
    print("+-------------------------------------------------------------------------------------+")
    if len(inputan) % 3 == 0:
        jobss = list(map(''.join, zip(*[iter(inputan)]*3)))
        hasil = ""
        for i in range(0, len(jobss)):
            hasil += oct(int(jobss[i], 2))[2:]
        hasilAkhir = list(map(( lambda x: ' ' + x + ' '), hasil))

        table = [[jobss, "rad-2"], [hasilAkhir, "rad-8"]]
        print(tabulate(table, tablefmt='fancy_grid'))
        print(f"+==> Hasil Biner {inputan} dalam Oktal adalah {hasil}")

    elif len(inputan) % 3 == 2:
        bint = "0" + inputan
        jobss = list(map(''.join, zip(*[iter(bint)]*3)))
        hasil = ""
        for i in range(0, len(jobss)):
            hasil += oct(int(jobss[i], 2))[2:]
        hasilAkhir = list(map(( lambda x: ' ' + x + ' '), hasil))

        table = [[jobss, "rad-2"], [hasilAkhir, "rad-8"]]
        print(tabulate(table, tablefmt='fancy_grid'))
        print(f"+==> Hasil Biner {inputan} dalam Oktal adalah {hasil}")

    elif len(inputan) % 3 == 1:
        bint = "00" + inputan
        jobss = list(map(''.join, zip(*[iter(bint)]*3)))
        hasil = ""
        for i in range(0, len(jobss)):
            hasil += oct(int(jobss[i], 2))[2:]
        hasilAkhir = list(map(( lambda x: ' ' + x + ' '), hasil))

        table = [[jobss, "rad-2"], [hasilAkhir, "rad-8"]]
        print(tabulate(table, tablefmt='fancy_grid'))
        print(f"+==> Hasil Biner {inputan} dalam Oktal adalah {hasil}")

    else:
        print("[!] TYPE ERROR")
        exit(0)
    print("+-------------------------------------------------------------------------------------+")
    submain(bins)

def bin_hex():
    print("+============[Binary to Hexadecimal]============+")
    inputan = str(input("Masukkan bilangan Biner tanpa spacing: "))
    print("+-------------------------------------------------------------------------------------+")
    print(f"Konversikan Biner menjadi bilangan Desimal terlebih dahulu")
    rev = inputan[::-1]
    desimal = 0
    arrr = list(rev.strip(" "))
    mult = []
    way = []
    for i in range(0, len(rev)):
        axx = int(rev[i])
        kalkul = axx*2**i
        desimal += kalkul
        mult.append(f"{kalkul}")
        way.append(f"({rev[i]}x2)^{i}")

    table = [arrr[::-1], way[::-1], mult[::-1]]
    print(tabulate(table, tablefmt='fancy_grid'))
    print("    ")
    print(f"Biner {inputan} Hasilnya {desimal} Desimal")
    print("+-------------------------------------------------------------------------------------+")
    print(f"Selanjutnya Ubah bilangan Desimal menjadi Heksadesimal")
    print(f"Desimal :: {desimal}")
    hasil  = ""
    while desimal != 0.0:
        while desimal % 16 != 0.0:
            vv = desimal % 16
            desimal = desimal // 16
            hasil += str(hex(int(vv)).replace("0x","").upper())
            print(f"{desimal} sisa {vv} -> dalam hex :: {hex(int(vv))}")
    print(f"\n+==> Dan Hasil Akhir Konversi dari {inputan} Biner adalah {hasil[::-1]} Hexa")
    print("+-------------------------------------------------------------------------------------+")
    submain(bins)


# OCTAL
def oct_dec():
    print("+============[Octal to Decimal]============+")
    inputan = str(input("Masukkan bilangan Oktal tanpa Spacing: "))
    print("+-------------------------------------------------------------------------------------+")
    rev = inputan[::-1]
    desimal = 0
    arrr = list(rev.strip(" "))
    mult = []
    way = []
    for i in range(0, len(rev)):
        axx = int(rev[i])
        kalkul = axx*8**i
        desimal += kalkul
        mult.append(f"{kalkul}")
        way.append(f"({rev[i]}x8)^{i}")

    hasilAkhir = "+".join(mult[::-1])
    table = [arrr[::-1], way[::-1], mult[::-1]]
    print(tabulate(table, tablefmt='fancy_grid'))
    print("------------------------------------------")
    print(f"+==> Hasil dari Oktal {inputan} adalah {hasilAkhir} = {desimal} Desimal")
    print("+-------------------------------------------------------------------------------------+")
    submain(octs)

def oct_bin():
    print("+============[Octal to Binary]============+")
    inputan = str(input("Masukkan bilangan Oktal tanpa Spacing: "))
    print("+-------------------------------------------------------------------------------------+")
    rev = 0
    chk = 0
    inputanint = int(inputan)

    while inputanint!=0:
        rem = inputanint%10
        if rem>7:
            chk = 1
            break
        rev = rem + (rev*10)
        inputanint = int(inputanint/10)

    if chk == 0:
        inputanint = rev
        binnum = ""

        while inputanint!=0:
            rem = inputanint%10
            if rem==0:
                binnum = binnum + "000"
            elif rem==1:
                binnum = binnum + "001"
            elif rem==2:
                binnum = binnum + "010"
            elif rem==3:
                binnum = binnum + "011"
            elif rem==4:
                binnum = binnum + "100"
            elif rem==5:
                binnum = binnum + "101"
            elif rem==6:
                binnum = binnum + "110"
            elif rem==7:
                binnum = binnum + "111"
            inputanint = int(inputanint/10)

        arr = list(map(( lambda x: ' ' + x + ' '), inputan))
        bintabs = list(map(''.join, zip(*[iter(binnum)]*3)))
        if len(binnum) % 4 == 0:
            akhirs = list(map(''.join, zip(*[iter(binnum)]*4)))
            akhir = " ".join(akhirs)
        elif len(binnum) % 4 == 1:
            binnums = "0" * 3 + binnum
            akhirs = list(map(''.join, zip(*[iter(binnums)]*4)))
            akhir = " ".join(akhirs)
        elif len(binnum) % 4 == 2:
            binnums = "0" * 2 + binnum
            akhirs = list(map(''.join, zip(*[iter(binnums)]*4)))
            akhir = " ".join(akhirs)
        elif len(binnum) % 4 == 3:
            binnums = "0" * 1 + binnum
            akhirs = list(map(''.join, zip(*[iter(binnums)]*4)))
            akhir = " ".join(akhirs)


        table = [arr, bintabs]
        print(tabulate(table, tablefmt='fancy_grid'))
        print(f"\nLalu kita ubah {binnum} menjadi 4 kelompok, dan hasilnya {akhir}")
        print(f"+==> Hasil dari Oktal {inputan} adalah {akhir} Biner")

    else:
        print("\nInvalid Input!")
        exit(0)
    print("+-------------------------------------------------------------------------------------+")
    submain(octs)

def oct_hex():
    print("+============[Octal to Hexadecimal]============+")
    inputan = str(input("Masukkan bilangan Oktal tanpa Spacing: "))
    print("+-------------------------------------------------------------------------------------+")
    rev = 0
    chk = 0
    inputanint = int(inputan)

    while inputanint!=0:
        rem = inputanint%10
        if rem>7:
            chk = 1
            break
        rev = rem + (rev*10)
        inputanint = int(inputanint/10)

    if chk == 0:
        inputanint = rev
        binnum = ""

        while inputanint!=0:
            rem = inputanint%10
            if rem==0:
                binnum = binnum + "000"
            elif rem==1:
                binnum = binnum + "001"
            elif rem==2:
                binnum = binnum + "010"
            elif rem==3:
                binnum = binnum + "011"
            elif rem==4:
                binnum = binnum + "100"
            elif rem==5:
                binnum = binnum + "101"
            elif rem==6:
                binnum = binnum + "110"
            elif rem==7:
                binnum = binnum + "111"
            inputanint = int(inputanint/10)

        arr = list(map(( lambda x: ' ' + x + ' '), inputan))
        bintabs = list(map(''.join, zip(*[iter(binnum)]*3)))
        if len(binnum) % 4 == 0:
            binnums = binnum
            akhirs = list(map(''.join, zip(*[iter(binnums)]*4)))
            akhir = " ".join(akhirs)
        elif len(binnum) % 4 == 1:
            binnums = "0" * 3 + binnum
            akhirs = list(map(''.join, zip(*[iter(binnums)]*4)))
            akhir = " ".join(akhirs)
        elif len(binnum) % 4 == 2:
            binnums = "0" * 2 + binnum
            akhirs = list(map(''.join, zip(*[iter(binnums)]*4)))
            akhir = " ".join(akhirs)
        elif len(binnum) % 4 == 3:
            binnums = "0" * 1 + binnum
            akhirs = list(map(''.join, zip(*[iter(binnums)]*4)))
            akhir = " ".join(akhirs)

        print("Kita ubah Oktal menjadi Biner terlebih dahulu")
        table = [arr, bintabs]
        print(tabulate(table, tablefmt='fancy_grid'))
        print("----------------------------------------------------------------------------------------")
        print(f"=> Hasil dari Oktal {inputan} adalah {akhir} Biner")
        print("----------------------------------------------------------------------------------------")
        

    else:
        print("\nInvalid Input!")
        exit(0)
    # ----------
    bnum = int(binnums, 2)
    desimal = 0
    desimal += bnum
    hasil  = ""
    while desimal != 0:
        while desimal % 16 != 0:
            vv = desimal % 16
            desimal = desimal // 16
            hasil += str(hex(int(vv)).replace("0x","").upper())

    hexnum = hasil[::-1]
    hasilAkhir = "".join(hexnum)
    print("Lalu Kita ubah Biner menjadi Heksadesimal")
    table = [akhirs, hexnum]
    print(tabulate(table, tablefmt='fancy_grid'))
    print("----------------------------------------------------------------------------------------")
    print(f"+==> Dan hasil akhir dari {inputan} Oktal adalah :: {hasilAkhir} dalam Heksadesimal")
    print("+-------------------------------------------------------------------------------------+")
    submain(octs)


# DECIMAL
def dec_bin():
    print("+============[Decimal to Binary]============+")
    inputan = float(input("Masukkan bilangan desimal: "))
    print("+-------------------------------------------------------------------------------------+")
    print(f"{inputan}")
    desimal = 0.0
    desimal += inputan
    hasil  = ""
    while desimal != 0.0:
        vv = desimal % 2
        desimal = desimal // 2
        hasil += str(int(vv)).upper()
        print(f"{desimal} sisa {vv}")

    if len(hasil) % 4 != 0:
        xyz = hasil[::-1]
        formula = "0" * (4 - len(hasil) % 4)
        test = formula + xyz
        hassss = list(map(''.join, zip(*[iter(test)]*4)))
        hasilAkhir = " ".join(hassss)

    else:
        hasilAkhir = hasil[::-1]

    print(f"Hasil Konversi dari {inputan} Desimal adalah {hasilAkhir} Binary")
    print("+-------------------------------------------------------------------------------------+")
    submain(decs)

def dec_oct():
    print("+============[Decimal to Octal]============+")
    inputan = float(input("Masukkan bilangan desimal: "))
    print("+-------------------------------------------------------------------------------------+")
    print(f"{inputan}")
    desimal = 0.0
    desimal += inputan
    hasil  = ""
    while desimal != 0.0:
        vv = desimal % 8
        desimal = desimal // 8
        hasil += str(int(vv)).upper()
        print(f"{desimal} sisa {vv}")

    if len(hasil) < 3:
        xyz = hasil[::-1]
        hasilAkhir = "0"*(3 - len(hasil)) + xyz
    else:
        hasilAkhir = hasil[::-1]

    print(f"Hasil Konversi dari {inputan} Desimal adalah {hasilAkhir} Octal")
    print("+-------------------------------------------------------------------------------------+")
    submain(decs)

def dec_hex():
    print("+============[Decimal to Hexadecimal]============+")
    inputan = float(input("Masukkan bilangan desimal: "))
    print("+-------------------------------------------------------------------------------------+")
    print(f"{inputan}")
    desimal = 0.0
    desimal += inputan
    hasil  = ""
    while desimal != 0.0:
        while desimal % 16 != 0.0:
            vv = desimal % 16
            desimal = desimal // 16
            hasil += str(hex(int(vv)).replace("0x","").upper())
            print(f"{desimal} sisa {vv} -> dalam hex :: {hex(int(vv))}")
    print(f"Hasil Konversi dari {inputan} Desimal adalah {hasil[::-1]} Hexa")
    print("+-------------------------------------------------------------------------------------+")
    submain(decs)


# HEXADECIMAL
def hex_dec():
    print("+============[Hexadecimal to Decimal]============+")
    submain(hexs)

def hex_bin():
    print("+============[Hexadecimal to Binary]============+")
    submain(hexs)

def hex_oct():
    print("+============[Hexadecimal to Octal]============+")
    submain(hexs)












if __name__ == "__main__":
    main()
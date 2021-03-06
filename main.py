#!/usr/bin/python
import os, subprocess
from tabulate import tabulate
from termcolor import colored, cprint

version = "       ver.1.1-alpha-release      "

bins = "biner"
octs = "oktal"
decs = "desimal"
hexs = "hexa"

isRunning = 0

def main(isRunning = 0):
    if isRunning == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        subprocess.check_output("python ./updater.py", shell=True)
        isRunning += 1
    
    os.system('cls' if os.name == 'nt' else 'clear')
    cprint("+==================================+", 'red', attrs=['bold'])
    cprint("|        KONVERTER BILANGAN        |", 'red', attrs=['bold'])
    cprint("+==================================+", 'red', attrs=['bold'])
    cprint(f"|{version}|", 'red', attrs=['bold'])
    cprint(f"|           by encrypt0r           |", 'red', attrs=['bold'])
    cprint("+==================================+", 'white', attrs=['bold'])
    cprint("| [1] Biner                        |", 'white', attrs=['bold'])
    cprint("| [2] Oktal                        |", 'white', attrs=['bold'])
    cprint("| [3] Desimal                      |", 'white', attrs=['bold'])
    cprint("| [4] Heksadesimal                 |", 'white', attrs=['bold'])
    cprint("| [0] Keluar                       |", 'white', attrs=['bold'])
    cprint("+==================================+", 'white', attrs=['bold'])
    pilih = int(input("Masukkan pilihan anda =>> "))
    if pilih == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        submain(bins)
    elif pilih == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        submain(octs)
    elif pilih == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        submain(decs)
    elif pilih == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        submain(hexs)
    elif pilih == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        exit(0)
    else:
        print("\nPilihan Tidak Tersedia.!!")
        main(isRunning = 1)

def submain(to):
    if to == bins:
        print("+==================================+")
        print("|          KONVERSI BINER          |")
        print("+==================================+")
        print("| [1] Biner ke Desimal             |")
        print("| [2] Biner ke Oktal               |")
        print("| [3] Biner ke Heksadesimal        |")
        print("|     Pilihan ini Khusus untuk     |")
        print("| [4] bilangan Biner negatif atau  |")
        print("|     dibelakang Koma              |")
        print("| [0] Kembali                      |")
        print("+==================================+")
        pilih = int(input("Masukkan pilihan anda =>> "))
        if pilih == 1:
            bin_dec()
        elif pilih == 2:
            bin_oct()
        elif pilih == 3:
            bin_hex()
        elif pilih == 4:
            print("Untuk Bilangan Negatif. soon")
        elif pilih == 0:
            main(isRunning = 1)
        else:
            print("\nPilihan tidak ada!")
            submain(to)
    elif to == octs:
        print("+==================================+")
        print("|          KONVERSI OKTAL          |")
        print("+==================================+")
        print("| [1] Oktal ke Desimal             |")
        print("| [2] Oktal ke Biner               |")
        print("| [3] Oktal ke Heksadesimal        |")
        print("|     Pilihan ini Khusus untuk     |")
        print("| [4] bilangan Biner negatif atau  |")
        print("|     dibelakang Koma              |")
        print("| [0] Kembali                      |")
        print("+==================================+")
        pilih = int(input("Masukkan pilihan anda =>> "))
        if pilih == 1:
            oct_dec()
        elif pilih == 2:
            oct_bin()
        elif pilih == 3:
            oct_hex()
        elif pilih == 4:
            print("Untuk Bilangan Negatif. soon")
        elif pilih == 0:
            main(isRunning = 1)
        else:
            print("\nPilihan tidak ada!")
            submain(to)
    elif to == decs:
        print("+==================================+")
        print("|         KONVERSI DESIMAL         |")
        print("+==================================+")
        print("| [1] Desimal ke Biner             |")
        print("| [2] Desimal ke Oktal             |")
        print("| [3] Desimal ke Heksadesimal      |")
        print("|     Pilihan ini Khusus untuk     |")
        print("| [4] bilangan Biner negatif atau  |")
        print("|     dibelakang Koma              |")
        print("| [0] Kembali                      |")
        print("+==================================+")
        pilih = int(input("Masukkan pilihan anda =>> "))
        if pilih == 1:
            dec_bin()
        elif pilih == 2:
            dec_oct()
        elif pilih == 3:
            dec_hex()
        elif pilih == 4:
            print("Untuk Bilangan Negatif. soon")
        elif pilih == 0:
            main(isRunning = 1)
        else:
            print("\nPilihan tidak ada!")
            submain(to)
    elif to == hexs:
        print("+==================================+")
        print("|       KONVERSI HEKSADESIMAL      |")
        print("+==================================+")
        print("| [1] Heksadesimal ke Desimal      |")
        print("| [2] Heksadesimal ke Biner        |")
        print("| [3] Heksadesimal ke Oktal        |")
        print("|     Pilihan ini Khusus untuk     |")
        print("| [4] bilangan Biner negatif atau  |")
        print("|     dibelakang Koma              |")
        print("| [0] Kembali                      |")
        print("+==================================+")
        pilih = int(input("Masukkan pilihan anda =>> "))
        if pilih == 1:
            hex_dec()
        elif pilih == 2:
            hex_bin()
        elif pilih == 3:
            hex_oct()
        elif pilih == 4:
            print("Untuk Bilangan Negatif. soon")
        elif pilih == 0:
            main(isRunning = 1)
        else:
            print("\nPilihan tidak ada!")
            submain(to)
    else:
        print("\nPilihan tidak ada!")
        main(isRunning = 1)


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
    # TABLE
    table = [arrr[::-1], way, mult]
    cprint(tabulate(table, tablefmt='fancy_grid'), 'yellow')
    # OUTPUT - GLOBAL COLORS
    inputanWrn = colored(f"{inputan}", 'yellow', attrs=['bold', 'underline'])
    akhirWrn = colored(f"{hasilAkhir}", 'yellow', attrs=['underline'])
    desimalWrn = colored(f"{desimal}", 'yellow', attrs=['bold', 'underline'])
    print(f"\n+==> Hasil dari biner {inputanWrn} adalah {akhirWrn} = {desimalWrn} Desimal")
    print("+-------------------------------------------------------------------------------------+")
    opt = input("LANJUT Konversi Biner ke Desimal? y/N :  ").upper()
    if opt == "Y":
        bin_dec()
    elif opt == "N":
        submain(bins)
    else:
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

        if len(hasil) % 3 == 2:
            fn = hasil[0:2]
            xx = hasil[2:len(hasil)]
            hass = list(map(''.join, zip(*[iter(xx)]*3)))
            finals = fn + " " + " ".join(hass)
        elif len(hasil) % 3 == 1:
            fn = hasil[0:1]
            xx = hasil[1:len(hasil)]
            hass = list(map(''.join, zip(*[iter(xx)]*3)))
            finals = fn + " " + " ".join(hass)
        elif len(hasil) % 3 == 0:
            hass = list(map(''.join, zip(*[iter(hasil)]*3)))
            finals = " ".join(hass)

        table = [[jobss, "biner"], [hasilAkhir, "oktal"]]
        print(tabulate(table, tablefmt='fancy_grid'))
        print(f"+==> Hasil Biner {inputan} dalam Oktal adalah {finals}")

    elif len(inputan) % 3 == 2:
        bint = "0" + inputan
        jobss = list(map(''.join, zip(*[iter(bint)]*3)))
        hasil = ""
        for i in range(0, len(jobss)):
            hasil += oct(int(jobss[i], 2))[2:]
        hasilAkhir = list(map(( lambda x: ' ' + x + ' '), hasil))

        if len(hasil) % 3 == 2:
            fn = hasil[0:2]
            xx = hasil[2:len(hasil)]
            hass = list(map(''.join, zip(*[iter(xx)]*3)))
            finals = fn + " " + " ".join(hass)
        elif len(hasil) % 3 == 1:
            fn = hasil[0:1]
            xx = hasil[1:len(hasil)]
            hass = list(map(''.join, zip(*[iter(xx)]*3)))
            finals = fn + " " + " ".join(hass)
        elif len(hasil) % 3 == 0:
            hass = list(map(''.join, zip(*[iter(hasil)]*3)))
            finals = " ".join(hass)


        table = [[jobss, "biner"], [hasilAkhir, "oktal"]]
        print(tabulate(table, tablefmt='fancy_grid'))
        print(f"+==> Hasil Biner {inputan} dalam Oktal adalah {finals}")

    elif len(inputan) % 3 == 1:
        bint = "00" + inputan
        jobss = list(map(''.join, zip(*[iter(bint)]*3)))
        hasil = ""
        for i in range(0, len(jobss)):
            hasil += oct(int(jobss[i], 2))[2:]
        hasilAkhir = list(map(( lambda x: ' ' + x + ' '), hasil))

        if len(hasil) % 3 == 2:
            fn = hasil[0:2]
            xx = hasil[2:len(hasil)]
            hass = list(map(''.join, zip(*[iter(xx)]*3)))
            finals = fn + " " + " ".join(hass)
        elif len(hasil) % 3 == 1:
            fn = hasil[0:1]
            xx = hasil[1:len(hasil)]
            hass = list(map(''.join, zip(*[iter(xx)]*3)))
            finals = fn + " " + " ".join(hass)
        elif len(hasil) % 3 == 0:
            hass = list(map(''.join, zip(*[iter(hasil)]*3)))
            finals = " ".join(hass)

        table = [[jobss, "biner"], [hasilAkhir, "oktal"]]
        print(tabulate(table, tablefmt='fancy_grid'))
        print(f"+==> Hasil Biner {inputan} dalam Oktal adalah {finals}")

    else:
        print("[!] TYPE ERROR")
        exit(0)
    print("+-------------------------------------------------------------------------------------+")
    opt = input("LANJUT Konversi Biner ke Oktal? y/N :  ").upper()
    if opt == "Y":
        bin_oct()
    elif opt == "N":
        submain(bins)
    else:
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
    opt = input("LANJUT Konversi Biner ke Heksadesimal? y/N :  ").upper()
    if opt == "Y":
        bin_hex()
    elif opt == "N":
        submain(bins)
    else:
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
    opt = input("LANJUT Konversi Oktal ke Desimal? y/N :  ").upper()
    if opt == "Y":
        oct_dec()
    elif opt == "N":
        submain(octs)
    else:
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
    opt = input("LANJUT Konversi Oktal ke Biner? y/N :  ").upper()
    if opt == "Y":
        oct_bin()
    elif opt == "N":
        submain(octs)
    else:
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
    opt = input("LANJUT Konversi Oktal ke Heksadesimal? y/N :  ").upper()
    if opt == "Y":
        oct_hex()
    elif opt == "N":
        submain(octs)
    else:
        submain(octs)


# DECIMAL
def dec_bin():
    print("+============[Decimal to Binary]============+")
    inputan = float(input("Masukkan bilangan desimal: "))
    print("+-------------------------------------------------------------------------------------+")
    print(f"{inputan} dibagi 8")
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

    print(f"hasilnya adalah {hasil[::-1]}")
    print(f"Hasil Konversi dari {inputan} Desimal adalah {hasilAkhir} Binary setelah dilakukan Grouping 4 Bit")
    print("+-------------------------------------------------------------------------------------+")
    opt = input("LANJUT Konversi Desimal ke Biner? y/N :  ").upper()
    if opt == "Y":
        dec_bin()
    elif opt == "N":
        submain(decs)
    else:
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

    rever = hasil[::-1]
    if len(rever) % 3 == 2:
        fn = rever[0:2]
        xx = rever[2:len(rever)]
        hass = list(map(''.join, zip(*[iter(xx)]*3)))
        hasilAkhir = fn + " " + " ".join(hass)
    elif len(rever) % 3 == 1:
        fn = rever[0:1]
        xx = rever[1:len(rever)]
        hass = list(map(''.join, zip(*[iter(xx)]*3)))
        hasilAkhir = fn + " " + " ".join(hass)
    elif len(rever) % 3 == 0:
        hass = list(map(''.join, zip(*[iter(rever)]*3)))
        hasilAkhir = " ".join(hass)

    print(f"Hasil Konversi dari {inputan} Desimal adalah {hasilAkhir} Octal")
    print("+-------------------------------------------------------------------------------------+")
    opt = input("LANJUT Konversi Desimal ke Oktal? y/N :  ").upper()
    if opt == "Y":
        dec_oct()
    elif opt == "N":
        submain(decs)
    else:
        submain(decs)

def dec_hex():
    print("+============[Decimal to Hexadecimal]============+")
    inputan = float(input("Masukkan bilangan desimal: "))
    print("+-------------------------------------------------------------------------------------+")
    print(f"{inputan} dibagi 16")
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
    opt = input("LANJUT Konversi Desimal ke Heksadesimal? y/N :  ").upper()
    if opt == "Y":
        dec_hex()
    elif opt == "N":
        submain(decs)
    else:
        submain(decs)


# HEXADECIMAL
def hex_dec():
    print("+============[Hexadecimal to Decimal]============+")
    inputan = str(input("Masukkan bilangan Heksadesimal tanpa spacing: ")).upper()
    print("+-------------------------------------------------------------------------------------+")
    desimal = 0
    arrr = list(inputan.strip(" "))
    oldstr = arrr
    newstrr = []
    hexalph = {"A": "10", "B":"11", "C":"12", "D":"l3", "E":"14", "F":"15"}

    i = 0
    for strng in oldstr:
        if strng.isdigit():
            newstrr += strng
        else:
            newstr = strng.replace(strng, hexalph[strng])
            newstrr.append(newstr)
        i += 1

    rev = newstrr[::-1]


    mult = []
    way = []
    for i in range(0, len(rev)):
        axx = int(rev[i])
        kalkul = axx*16**i
        desimal += kalkul
        mult.append(f"{kalkul}")
        way.append(f"({newstrr[i]}x16)^{i}")

    hasilAkhir = "+".join(mult)
    # TABLE
    table = [arrr, way, mult]
    cprint(tabulate(table, tablefmt='fancy_grid'), 'yellow')
    # OUTPUT - GLOBAL COLORS
    inputanWrn = colored(f"{inputan}", 'yellow', attrs=['bold', 'underline'])
    akhirWrn = colored(f"{hasilAkhir}", 'yellow', attrs=['underline'])
    desimalWrn = colored(f"{desimal}", 'yellow', attrs=['bold', 'underline'])
    print(f"\n+==> Hasil dari Heksa {inputanWrn} adalah {akhirWrn} = {desimalWrn} Desimal")
    print("+-------------------------------------------------------------------------------------+")
    opt = input("LANJUT Konversi Heksa ke Desimal? y/N :  ").upper()
    if opt == "Y":
        hex_dec()
    elif opt == "N":
        submain(hexs)
    else:
        submain(hexs)

def hex_bin():
    print("+============[Hexadecimal to Binary]============+")
    inputan = str(input("Masukkan bilangan Heksadesimal tanpa spacing: ")).upper()
    print("+-------------------------------------------------------------------------------------+")
    arrr = list(inputan.strip(" "))
    oldstr = arrr
    newstrr = []
    hexalph = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
        }

    i = 0
    for strng in oldstr:
        newstr = strng.replace(strng, hexalph[strng])
        newstrr.append(newstr)
        i += 1

    akhir = " ".join(newstrr)
    # TABLE
    table = [arrr, newstrr]
    cprint(tabulate(table, tablefmt='fancy_grid'), 'yellow')
    # OUTPUT - GLOBAL COLORS
    inputanWrn = colored(f"{inputan}", 'yellow', attrs=['bold', 'underline'])
    desimalWrn = colored(f"{akhir}", 'yellow', attrs=['bold', 'underline'])
    print(f"\n+==> Hasil dari Heksa {inputanWrn} adalah {desimalWrn} Desimal")
    print("+-------------------------------------------------------------------------------------+")
    opt = input("LANJUT Konversi Heksa ke Biner? y/N :  ").upper()
    if opt == "Y":
        hex_bin()
    elif opt == "N":
        submain(hexs)
    else:
        submain(hexs)

def hex_oct():
    print("+============[Hexadecimal to Octal]============+")
    inputan = str(input("Masukkan bilangan Heksadesimal tanpa spacing: ")).upper()
    print("+-------------------------------------------------------------------------------------+")
    arrr = list(inputan.strip(" "))
    oldstr = arrr
    newstrr = []
    hexalph = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
        }

    i = 0
    for strng in oldstr:
        newstr = strng.replace(strng, hexalph[strng])
        newstrr.append(newstr)
        i += 1

    # TABLE
    table = [arrr + ["Heksa"], newstrr + ["Biner"]]
    cprint(tabulate(table, tablefmt='fancy_grid'), 'yellow')

    # bin to oct
    binrs = "".join(newstrr)

    if len(binrs) % 3 == 0:
        jobss = list(map(''.join, zip(*[iter(binrs)]*3)))
        hasil = ""
        for i in range(0, len(jobss)):
            hasil += oct(int(jobss[i], 2))[2:]
        hasilAkhir = list(map(( lambda x: ' ' + x + ' '), hasil))

        if len(hasil) % 3 == 2:
            fn = hasil[0:2]
            xx = hasil[2:len(hasil)]
            hass = list(map(''.join, zip(*[iter(xx)]*3)))
            finals = fn + " " + " ".join(hass)
        elif len(hasil) % 3 == 1:
            fn = hasil[0:1]
            xx = hasil[1:len(hasil)]
            hass = list(map(''.join, zip(*[iter(xx)]*3)))
            finals = fn + " " + " ".join(hass)
        elif len(hasil) % 3 == 0:
            hass = list(map(''.join, zip(*[iter(hasil)]*3)))
            finals = " ".join(hass)

        table = [[jobss, "biner"], [hasilAkhir, "oktal"]]
        print(tabulate(table, tablefmt='fancy_grid'))
        print(f"+==> Hasil Heksa {inputan} dalam Oktal adalah {finals}")

    elif len(binrs) % 3 == 2:
        bint = "0" + binrs
        jobss = list(map(''.join, zip(*[iter(bint)]*3)))
        hasil = ""
        for i in range(0, len(jobss)):
            hasil += oct(int(jobss[i], 2))[2:]
        hasilAkhir = list(map(( lambda x: ' ' + x + ' '), hasil))

        if len(hasil) % 3 == 2:
            fn = hasil[0:2]
            xx = hasil[2:len(hasil)]
            hass = list(map(''.join, zip(*[iter(xx)]*3)))
            finals = fn + " " + " ".join(hass)
        elif len(hasil) % 3 == 1:
            fn = hasil[0:1]
            xx = hasil[1:len(hasil)]
            hass = list(map(''.join, zip(*[iter(xx)]*3)))
            finals = fn + " " + " ".join(hass)
        elif len(hasil) % 3 == 0:
            hass = list(map(''.join, zip(*[iter(hasil)]*3)))
            finals = " ".join(hass)


        table = [[jobss, "biner"], [hasilAkhir, "oktal"]]
        print(tabulate(table, tablefmt='fancy_grid'))
        print(f"+==> Hasil Heksa {inputan} dalam Oktal adalah {finals}")

    elif len(binrs) % 3 == 1:
        bint = "00" + binrs
        jobss = list(map(''.join, zip(*[iter(bint)]*3)))
        hasil = ""
        for i in range(0, len(jobss)):
            hasil += oct(int(jobss[i], 2))[2:]
        hasilAkhir = list(map(( lambda x: ' ' + x + ' '), hasil))

        if len(hasil) % 3 == 2:
            fn = hasil[0:2]
            xx = hasil[2:len(hasil)]
            hass = list(map(''.join, zip(*[iter(xx)]*3)))
            finals = fn + " " + " ".join(hass)
        elif len(hasil) % 3 == 1:
            fn = hasil[0:1]
            xx = hasil[1:len(hasil)]
            hass = list(map(''.join, zip(*[iter(xx)]*3)))
            finals = fn + " " + " ".join(hass)
        elif len(hasil) % 3 == 0:
            hass = list(map(''.join, zip(*[iter(hasil)]*3)))
            finals = " ".join(hass)

        table = [[jobss, "biner"], [hasilAkhir, "oktal"]]
        print(tabulate(table, tablefmt='fancy_grid'))
        print(f"+==> Hasil Heksa {inputan} dalam Oktal adalah {finals}")

    else:
        print("[!] TYPE ERROR")
        exit(0)

    print("+-------------------------------------------------------------------------------------+")
    opt = input("LANJUT Konversi Heksa ke Oktal? y/N :  ").upper()
    if opt == "Y":
        hex_oct()
    elif opt == "N":
        submain(hexs)
    else:
        submain(hexs)

if __name__ == "__main__":
    main(isRunning = 0)




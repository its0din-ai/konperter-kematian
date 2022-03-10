#!/usr/bin/python


# KONVERTER BILANGAN

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
    submain(bins)

def bin_oct():
    print("+============[Binary to Octal]============+")
    inputan = str(input("Masukkan bilangan Biner: "))
    print("+-------------------------------------------------------------------------------------+")
    if len(inputan) % 3 == 0:
        jobss = list(map(''.join, zip(*[iter(inputan)]*3)))
        hasil = ""
        for i in range(0, len(jobss)):
            hasil += oct(int(jobss[i], 2))[2:]
        print(f"Biner {inputan} dalam Oktal adalah {hasil}")
        print(f"*) {jobss}radiks-2 \n=> {list(map(( lambda x: ' ' + x + ' '), hasil))}radiks-8")

    elif len(inputan) % 3 == 2:
        bint = "0" + inputan
        jobss = list(map(''.join, zip(*[iter(bint)]*3)))
        hasil = ""
        for i in range(0, len(jobss)):
            hasil += oct(int(jobss[i], 2))[2:]
        print(f"Biner {inputan} dalam Oktal adalah {hasil}")
        print(f"*) {jobss}radiks-2 \n=> {list(map(( lambda x: ' ' + x + ' '), hasil))}radiks-8")
    elif len(inputan) % 3 == 1:
        bint = "00" + inputan
        jobss = list(map(''.join, zip(*[iter(bint)]*3)))
        hasil = ""
        for i in range(0, len(jobss)):
            hasil += oct(int(jobss[i], 2))[2:]
        print(f"Biner {inputan} dalam Oktal adalah {hasil}")
        print(f"*) {jobss}radiks-2 \n=> {list(map(( lambda x: ' ' + x + ' '), hasil))}radiks-8")
    else:
        print("[!] TYPE ERROR")
        exit(0)

    print("+-------------------------------------------------------------------------------------+")
    submain(bins)

def bin_hex():
    print("+============[Binary to Hexadecimal]============+")
    submain(bins)


# OCTAL
def oct_dec():
    print("+============[Octal to Decimal]============+")
    submain(octs)

def oct_bin():
    print("+============[Octal to Binary]============+")
    submain(octs)

def oct_hex():
    print("+============[Octal to Hexadecimal]============+")
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

    if len(hasil) < 8:
        xyz = hasil[::-1]
        hasilAkhir = "0"*(8 - len(hasil)) + xyz
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
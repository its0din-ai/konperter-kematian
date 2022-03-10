#!/usr/bin/python

from psutil import users
from tabulate import tabulate

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

def bin_dec():
    print("\nKONVERSI BINER KE DESIMAL")
    print("=========================")
    user = input("Biner ke Desimal :: ")
    listbin = user.split('')
    listdec = []
    if len(listbin) % 4 != 0:
        print(listbin)
        


    main()
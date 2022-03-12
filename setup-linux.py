import time
import os
import subprocess


verr = str(subprocess.check_output("python --version", shell=True).decode()).replace('\n', '')
verrP = str(subprocess.check_output("pip --version", shell=True).decode()).replace('\n', '')

# verrs = str(verr.decode("utf-8")).replace('\n', '')
# verrsP = str(verrP.decode("utf-8")).replace('\n', '')

if True:
    print("\n=========================================================================")
    print("Cheking for Update")
    print("========================================================================")
    subprocess.check_output("python updater.py)", shell=True)
    for j in range(1,101):
        time.sleep(.04)
        downloading = "[CHECKING]"
        percentage = f"[{j}%]"
        bar = '|' * j
        color = downloading + bar + percentage
        
        print(color, end="\r")
            
        print("\n", end="\n")


if "Python 3" in verr:
    print("\n=========================================================================")
    print("Python 3 terdeteksi")
    print(verr)
    print("========================================================================")
    time.sleep(.8)
    if "pip (python 3" in verrP:
        print("pip terdeteksi")
        print(verrP)
        print("=========================================================================")
        time.sleep(.8)

        print("Memulai setup")
        subprocess.check_output("pip3 install -r requirements.txt", shell=True)
        for j in range(1,101):
            time.sleep(.02)
            downloading = "[Loading]"
            percentage = f"[{j}%]"
            bar = '|' * j
            color = downloading + bar + percentage
            
            print(color, end="\r")
            
        print("\n", end="\n")

        print("+==========================================================+")
        print("|                     SETUP SELESAI !!                     |")
        print("+----------------------------------------------------------+")
        print("|  Program akan otomatis dibuka untuk pertama kali         |")
        print("|  Untuk selanjutnya, tetap jalankan program dengan        |")
        print("|  mengetikkan perintah python3 main.py                    |")
        print("|                                                          |")
        print("|  Terimakasih telah menggunakan Program Opensource ini    |")
        print("+==========================================================+\n")

        for j in range(1,101):
            time.sleep(.07)
            downloading = "[Preparing]"
            percentage = f"[{j}%]"
            bar = '|' * j
            color = downloading + bar + percentage
            
            print(color, end="\r")
            
        print("\n", end="\n")
        os.system("python ./main.py")
    else:
        print("pip3 Tidak ada, mohon install PIP terlebih dahulu")
        print(verrP)
        print("=========================================================================")
        time.sleep(.8)
        exit(0)
else:
    print("\n=========================================================================")
    print("Python 3 Tidak ada, mohon install PIP terlebih dahulu")
    print(verr)
    print("========================================================================")
    time.sleep(.8)
    exit(0)
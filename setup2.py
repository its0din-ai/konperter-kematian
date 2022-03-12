#!/usr/bin/python
import time, os, subprocess
from alive_progress import alive_bar

verr = str(subprocess.check_output("python --version", shell=True).decode()).replace('\n', '')
verrP = str(subprocess.check_output("pip --version", shell=True).decode()).replace('\n', '')


with alive_bar(100, force_tty=True, title="Checking for Update") as bar:
    subprocess.check_output("git fetch", shell=True)
    subprocess.check_output("git pull", shell=True)
    for i in range(100):
        time.sleep(0.1)
        bar()

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
        with alive_bar(100, force_tty=True, title="Setup in Progress") as bar:
            for i in range(100):
                time.sleep(0.1)
                bar()

        print("+==========================================================+")
        print("|                     SETUP SELESAI !!                     |")
        print("+----------------------------------------------------------+")
        print("|  Program akan otomatis dibuka untuk pertama kali         |")
        print("|  Untuk selanjutnya, tetap jalankan program dengan        |")
        print("|  mengetikkan perintah python3 main.py                    |")
        print("|                                                          |")
        print("|  Terimakasih telah menggunakan Program Opensource ini    |")
        print("+==========================================================+\n")

        with alive_bar(100, force_tty=True, title="Preparing Program") as bar:
            for i in range(100):
                time.sleep(0.1)
                bar()
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
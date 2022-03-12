#!/usr/bin/python
import time, os, subprocess
from alive_progress import alive_bar

verr = str(subprocess.check_output("python --version", shell=True).decode()).replace('\n', '')
verrP = str(subprocess.check_output("pip --version", shell=True).decode()).replace('\n', '')
verrG = str(subprocess.check_output("git --version", shell=True).decode()).replace('\n', '')
sistem = os.name


print("Checking for Update")
with alive_bar(100, force_tty=True) as bar:
    subprocess.check_output("git fetch", shell=True)
    subprocess.check_output("git pull", shell=True)
    for i in range(100):
        time.sleep(0.1)
        bar()

print(sistem)

if sistem == "nt":
    if "git version" in verrG:
        print("\n=========================================================================")
        print("GIT Terdeteksi")
        print(verrG)
        print("========================================================================")
        time.sleep(.8)
        if "Python 3" in verr:
            print("Python 3 Terdeteksi")
            print(verr)
            print("========================================================================")
            time.sleep(.8)
            if "pip (python 3" in verrP:
                print("pip Terdeteksi")
                print(verrP)
                print("=========================================================================")
                time.sleep(.8)

                subprocess.check_output("pip3 install -r requirements.txt", shell=True)
                print("Setup in Progress")
                with alive_bar(100, force_tty=True) as bar:
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

                print("Preparing Program")
                with alive_bar(100, force_tty=True) as bar:
                    for i in range(100):
                        time.sleep(0.1)
                        bar()
                os.system("python ./main.py")
            else:
                print("pip3 tidak Terdeteksi, silahkan kunjungi https://pip.pypa.io/en/stable/installation/ untuk Tutorial Installasi PIP")
                print(verrP)
                print("=========================================================================")
                time.sleep(.8)
                exit(0)
        else:
            print("\n=========================================================================")
            print("Python 3 tidak Terdeteksi, silahkan kunjungi https://www.petanikode.com/python-windows/ untuk Tutorial Installasi Python")
            print(verr)
            print("========================================================================")
            time.sleep(.8)
            exit(0)
    else:
        print("\n=========================================================================")
        print("GIT tidak Terdeteksi, silahkan kunjungi https://www.petanikode.com/git-install/ untuk Tutorial Installasi GIT")
        print("========================================================================")
else:
    if "git version" in verrG:
        print("\n=========================================================================")
        print("GIT Terdeteksi")
        print(verrG)
        print("========================================================================")
        time.sleep(.8)
        if "Python 3" in verr:
            print("Python 3 Terdeteksi")
            print(verr)
            print("========================================================================")
            time.sleep(.8)
            if "pip (python 3" in verrP:
                print("pip Terdeteksi")
                print(verrP)
                print("=========================================================================")
                time.sleep(.8)

                subprocess.check_output("pip3 install -r requirements.txt", shell=True)
                print("Setup in Progress")
                with alive_bar(100, force_tty=True) as bar:
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

                print("Preparing Program")
                with alive_bar(100, force_tty=True) as bar:
                    for i in range(100):
                        time.sleep(0.1)
                        bar()
                os.system("python ./main.py")
            else:
                print("PIP3 Tidak Terdeteksi, mencoba menginstal PIP3...")
                print(verrP)
                print("=========================================================================")
                time.sleep(.8)
                exit(0)
        else:
            print("\n=========================================================================")
            print("Python3 Tidak Terdeteksi, mencoba menginstall Python3...")
            print(verr)
            print("========================================================================")
            time.sleep(.8)
            exit(0)
    else:
        print("\n=========================================================================")
        print("GIT tidak Terdeteksi, mencoba menginstall GIT...")
        print("========================================================================")






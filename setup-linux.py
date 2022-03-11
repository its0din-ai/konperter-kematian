import time
import os
import subprocess


verr = subprocess.check_output("python --version", shell=True).decode()
verrP = subprocess.check_output("pip --version", shell=True).decode()


if "Python 3" in verr:
    print("Python 3 terdeteksi")
    print(verr)
    time.sleep(.8)
    if "pip (python 3" in verrP:
        print("pip terdeteksi")
        print(verrP)
        time.sleep(.8)
        print("Memulai setup")
        os.system("pip3 install -r requirements.txt")

        time.sleep(2)
        print("Selesai")

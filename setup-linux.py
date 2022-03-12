import subprocess
import os

subprocess.check_output("pip3 install alive_progress", shell=True)
os.system("python ./updater.py")
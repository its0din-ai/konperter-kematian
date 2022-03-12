#!/usr/bin/python
import subprocess, os

subprocess.check_output("pip3 install alive_progress", shell=True)
os.system("python ./setup2.py")
import os
import subprocess

subprocess.check_output("git fetch", shell=True)
subprocess.check_output("git pull", shell=True)
## Termcolor Library: ANSII Color formatting for output in terminal.
 
# Import Libraries
from termcolor import colored
 
print("warning")
print("Done")
 
### Text colors:
 
warning = colored("warning", "red")
done = colored("done", "green")
 
print(f"[{warning}] Virus in running")
print(f"[{done}] Virus killed")
 
### Text highlights:
warning = colored("[warning]", "red", "on_grey")
done = colored("[done]", "green", "on_grey")
 
print(f"{warning} Virus in running")
print()
print(f"{done} Virus killed")
 
### Attributes
warning = colored("[warning]", "red", "on_grey", attrs=['reverse'])
done = colored("[done]", "green")
 
print(f"{warning} Virus in running", end = "\n")
 
print(f"{done} Virus killed", end="\n")
 
done = colored("[done]", "green", attrs=['bold'])
print(f"{done} Virus killed")
 
done = colored("[done]", "green", attrs=['underline'])
print(f"{done} Virus killed")
 
done = colored("[done]", "green", attrs=['reverse'])
print(f"{done} Virus killed")
 
 
######### Downloading Bar
import time
 
for j in range(1,101):
    time.sleep(.02)
     
    downloading = colored("Collecting Data", 'yellow', 'on_grey', attrs=['reverse'])
    percentage = colored(f"[{j}%]", 'blue')
    bar = colored('|' * j, "green")
    color = downloading + percentage + bar
     
    print(color, end="\r")
     
print("\n", end="\n")
 
for j in range(1,101):
    time.sleep(.2)
     
    downloading = colored("Downloading", 'red', 'on_grey', attrs=['reverse'])
    percentage = colored(f"[{j}%]", 'blue')
    bar = colored('|' * j, "green")
    color = downloading + percentage + bar
     
    print(color, end="\r")
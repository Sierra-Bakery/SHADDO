import sys
import time
import random
class bcolors:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
def Loadscreen():
    print(f"{bcolors.YELLOW}Initiating SHADDO.exe{bcolors.END}")
    time.sleep(0.9)
    for i in range(101):
        eqlsgn = f"{bcolors.PURPLE}={bcolors.END}"
        sys.stdout.write('\r')
        sys.stdout.write("[%-10s] %d%%" % (eqlsgn*i, 1*i))
        sys.stdout.flush()
        time.sleep((random.randint(1,100)*0.001))
    print(f"{bcolors.GREEN}\n< SHADDO.exe Initiated Sucessfully >{bcolors.END}")
    time.sleep(2)

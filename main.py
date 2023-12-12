#SHADDO.bat remake for Python
#Original SHADDO.bat remake in python. SHADDO is a tool that will contain multiple ethical hacking tools.
#This will mimmic some or all types of tools on kali or other systems.
#This tool will contain cool visuals and functionality.
#Aimed at bringing a simplified platform for beginners at ethical hacking - penetration testing.
import Graphics
import os
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
# EXAMPLE COLORED PRINTABLE >>> print(f"{bcolors.FAIL}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
#Start of the program, this gives a cool startup graphical
os.system('mode con: cols=120 lines=5')
Graphics.Loadscreen()
#makeshift start asking for account username and password
os.system('mode con: cols=120 lines=20')
username = str(input(f"{bcolors.BLUE}Username >>> {bcolors.END}"))
password = str(input(f"{bcolors.CYAN}Password >>> {bcolors.END}"))
# # Check with server if correct # #
while username != "Sierra" or password != "LightBeforeDawn": #Will be changed later
    print("Loading...")
    waittime = random.randint(1,3)
    time.sleep(waittime)
    print(f"{bcolors.RED}{bcolors.BOLD}ERROR: INCORRECT CREDENTIALS{bcolors.END}")
    print(f"{bcolors.YELLOW}     Please Try Again{bcolors.END}")
    input(f"{bcolors.YELLOW}Press ENTER To Continue...{bcolors.END}")
    os.system('mode con: cols=120 lines=20')
    username = str(input(f"{bcolors.BLUE}Username >>> {bcolors.END}"))
    password = str(input(f"{bcolors.CYAN}Password >>> {bcolors.END}"))
print(f"{bcolors.PURPLE}AUTHENTICATION SUCESSFULL{bcolors.END}")
time.sleep(2)
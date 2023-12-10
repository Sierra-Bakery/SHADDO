import sys
import time
import random
def initiatescreen():
    print("< Initiating SHADDO.exe >")
    time.sleep(0.9)
    for i in range(101):
        sys.stdout.write('\r')
        sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
        sys.stdout.flush()
        time.sleep((random.randint(1,100)*0.001))
    print("\n< SHADDO.exe Initiated Sucessfully >")

e = initiatescreen()
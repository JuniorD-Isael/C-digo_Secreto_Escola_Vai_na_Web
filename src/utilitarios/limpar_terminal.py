from time import sleep
import os
def clear():
    sleep(2.5)
    os.system('cls' if os.name == 'nt' else 'clear')
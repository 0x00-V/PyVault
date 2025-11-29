from os import system
import sys
from .cli import mainMenu

try:
    mainMenu()
except KeyboardInterrupt as e:
    system("clear||cls")
    print("Goodbye.")
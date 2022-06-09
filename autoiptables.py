import os
from colorama import Fore
import platform
import time

################################################################################################

plt = platform.system()

menuList = ["Add", "Clear"]
ModuleChoice = 0

################################################################################################

Banner = Fore.RED + """
                _         _____ _____ _______    _     _           
     /\        | |       |_   _|  __ \__   __|  | |   | |          
    /  \  _   _| |_ ___    | | | |__) | | | __ _| |__ | | ___  ___ 
   / /\ \| | | | __/ _ \   | | |  ___/  | |/ _` | '_ \| |/ _ \/ __|
  / ____ \ |_| | || (_) | _| |_| |      | | (_| | |_) | |  __/\__ \\
 /_/    \_\__,_|\__\___/ |_____|_|      |_|\__,_|_.__/|_|\___||___/
                     ______                                        
                    |______|

                        [/ Dev By GameBak \]
"""

################################################################################################

def ModuleMenu():
    nombre = 0

    for module in menuList:
        nombre += 1
        print(Fore.LIGHTRED_EX + "[" + str(nombre) + "] " + module)

    print(' ')

def Reset():
    time.sleep(0.8)

    if plt == "Windows":
        os.system("cls")
    elif plt == "Linux":
        os.system("clear")
    elif plt == "Darwin":
        os.system("clear")

    print(Banner)
    ModuleMenu()

def readExec(file):
    rules = open('./config/' + file + '.txt', 'r+')

    for l in rules.readlines():
        if (str(l).strip() != ""):
            os.system(l.split('\n')[0])

def Main(ModuleChoice):
    while(True):
        QuestionMenu = input(Fore.RED + "Select your Module : " + Fore.RESET)
        print("")

        if(QuestionMenu.isnumeric()):
            if(0 < int(QuestionMenu) <= len(menuList)):
                ModuleChoice += int(QuestionMenu) + 1
                break
            else:
                print(Fore.LIGHTRED_EX + "[!] You must enter a number corresponding to a module." + Fore.RESET)
                Reset()
        else:
            print(Fore.LIGHTRED_EX + "[!] You must enter a number corresponding to a module." + Fore.RESET)
            Reset()

    if(ModuleChoice != 1):
        ModuleChoice = ModuleChoice-1 

    if menuList[ModuleChoice-1] == "Add":
        readExec("rules")

    elif menuList[ModuleChoice-1] == "Clear":
        readExec("clear")

################################################################################################

Reset()
Main(ModuleChoice)

################################################################################################

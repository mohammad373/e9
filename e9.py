# e9

import os
import sys
import time
import socket
import datetime
import requests
from colorama import Fore

def __target__():
    os.system("clear")
    print(Fore.YELLOW + """
                    ///////////////////
                    //////////////////
                    /////////////////
                    ////////////////
                    ///////////////
                    //////////////
                    /////////////
                    ////////////
                    ///////////
                    //////////
                    /////////
                    ////////
                    ///////
                    //////
                    /////
                    ////
                    ///
                    //
                    /""")
   
    target = input(Fore.RED + "\n[" + Fore.BLUE + "!" + Fore.RED + "]" + Fore.BLUE + " ~ " + Fore.YELLOW + "Pleass Enter Your Address Target" + Fore.GREEN + " ==>  ")
    if  target == "" or None:
        try:
            time.sleep(1)
            print(Fore.RED + "[!] ~ Error : Your Target Is None Or Not Found ;(")
            time.sleep(0.4)
            sys.exit()
        except:
            pass
    if not "http" in target or not "https" in target:
       target = "http://" + target
    mn = socket.gethostbyname(target)
    r = requests.get(target)
    coun = 1
    time = datetime.datetime.now()
    while True:
        coun = 1
        if r.status_code == 404 or r.status_code == 500:
            print(Fore.BLUE + "[ " , Fore.RED + coun , Fore.BLUE + " ]" + Fore.RED + " ~ " + Fore.RED + target + Fore.GREEN + " ==>  " , Fore.RED + mn , Fore.YELLOW + time)
            coun += 1
        if r.status_code == 200:
            print(Fore.BLUE + "[ " , Fore.GREEEN +  coun , Fore.BLUE + " ]" + Fore.GREEEN + " ~ " + Fore.GREEEN + target + Fore.RED + " ==> " ,Fore.GREEN + mn , Fore.YELLOW + time)
            coun += 1
__target__()

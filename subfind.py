#!/usr/bin/env python3
import requests
import os
import sys
import re
from multiprocessing import Pool
from colorama import Fore, init

# Color
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
white = Fore.WHITE
cyan = Fore.LIGHTCYAN_EX
blue = Fore.LIGHTBLUE_EX
yellow = Fore.LIGHTYELLOW_EX

init(autoreset=True)
s = requests.Session()

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    __banner__ = f"""{red}
    ⣴⣶⣤⡤⠦⣤⣀⣤⠆     ⣈⣭⣭⣿⣶⣿⣦⣼⣆        
    ⠉⠻⢿⣿⠿⣿⣿⣶⣦⠤ ⡠⢾⣿⣿⡿⠋⠉⠉⠻⣿⣿⡛⣦      
          ⠈   ⠈⢿⣿⣟⠦⣾⣿⣿⣷     ⠻⠿⢿⣿⣧⣄    
       ⣸⣿⣿⢧ ⢻⠻⣿⣿⣷⣄⣀ ⠢⣀⡀    ⠈⠙⠿    
   ⢀      ⢠⣿⣿⣿⠈  ⠡⠌⣻⣿⣿⣿⣿⣿⣿⣿⣛⣳⣤⣀⣀  
   ⢠⣧⣶⣥⡤⢄ ⣸⣿⣿⠘  ⢀⣴⣿⣿⡿⠛⣿⣿⣧⠈⢿⠿⠟⠛⠻⠿    {cyan}---[ {white}MASS Subdomain Finder {red}]---
{red}  ⣰⣿⣿⠛⠻⣿⣿⡦⢹⣿⣷   ⢊⣿⣿⡏  ⢸⣿⣿⡇ ⢀⣠⣄⣾           {cyan}[ {white}Created By Drian {red}]
{red} ⣠⣿⠿⠛ ⢀⣿⣿⣷⠘⢿⣿⣦⡀ ⢸⢿⣿⣿⣄ ⣸⣿⣿⡇⣪⣿⡿⠿⣿⣷⡄ 
  ⠙⠃   ⣼⣿⡟⠌ ⠈⠻⣿⣿⣿⣷⣿⣿⣿⣿⡟ ⠫⢿⣿⡆   ⠁
  ⢻⣿⣿⣄   ⠈⠻⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⡟ ⠫⢿⣿⡆   ⠁
  ⠻⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⣀⣤⣾⡿⠃    """
    print(__banner__ + "\n")

def SubdomainFinder(domain):
    global s
    try:
        domain = domain.strip("\n\r")
        req = s.get(f"https://rapiddns.io/subdomain/{domain}?full=1#result").text
        all_domain = re.findall(r"</th>\n<td>(.*?)</td>", req)
        
        if len(all_domain) != 0:
            sys.stdout.write(f"\n{white}---> {blue}{domain} {white}[ {green}{len(all_domain)} Domain {white}]")
            with open("../subdomain.txt", "a") as subdomain_file:
                for x in all_domain:
                    x = x.replace("ns1.", "").replace("ns2.", "").replace("www.", "").replace("cpanel.", "").replace("autodiscover.", "").replace("whm.", "").replace("cpcontacts.", "").replace("webdisk.", "").replace("cpcalendars.", "")
                    if x not in open("../subdomain.txt", "r").read():
                        subdomain_file.write(x + "\n")
        else:
            sys.stdout.write(f"\n{white}---> {blue}{domain} {white}[ {yellow}BAD! {white}]")
    except:
        sys.stdout.write(f"\n{white}---> {blue}{domain} {white}[ {yellow}BAD! {white}]")

if __name__=="__main__":
    banner()
    
    # Menggunakan os.path.dirname(__file__) untuk mendapatkan direktori di mana skrip ini berjalan
    script_directory = os.path.dirname(os.path.realpath(__file__))
    list_domain = open(os.path.join(script_directory, "..", input(f"{cyan}[{yellow}#{cyan}] {white}Domain List : ")), "r").readlines()
    Thread = input(f"{cyan}[{yellow}#{cyan}] {white}Thread : ")
    pool = Pool(int(Thread))
    pool.map(SubdomainFinder, list_domain)
    pool.close()
    pool.join()
    sys.stdout.write(f"\n{white}---> DONE!")
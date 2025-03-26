import os
import re
import requests
import time

blue = '\033[0;34'
cyan = '\033[0;36m'
green = '\033[0;34m'
okegreen = '\033[92m'
lightgreen = '\033[1;32m'
white = '\033[1;37m'
red = '\033[1;31m'
yellow = '\033[1;33m'

def angka(save):
    while True:
        curr = requests.get("https://website.informer.com/lists/").text
        domains = re.findall(r'"/(.*?)" >', curr)
        b = len(domains)
        if b > 0:
            with open(save, 'a') as file:
                file.write("\n".join(domains) + "\n")
            b = sum(1 for _ in open(save))
            print(f"\033[42;1m -- \033[0m {okegreen}[+] Found {b} Total : {b}")
        else:
            print(f"\033[41;1m -- \033[0m {red} [-] Error Ngentod")
        time.sleep(5)

def banner():
    print(f"{okegreen}<<<<<>>>>>")
    print(f"{cyan}       Grabber by Drian")
    print(f"{cyan}   Auto Grab Domain Per Sec")
    print(f"{okegreen}<<<<<>>>>>")
    save = input("Save in => ")
    save = f"../{save}"
    return save

if __name__ == "__main__":
    os.system('clear')
    save = banner()
    angka(save)
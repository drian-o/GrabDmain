#!/usr/bin/env python3
# Created by Chris

import os
import re
import requests

blue = '\033[0;34m'
cyan = '\033[0;36m'
green = '\033[0;34m'
okegreen = '\033[92m'
lightgreen = '\033[1;32m'
white = '\033[1;37m'
red = '\033[1;31m'
yellow = '\033[1;33m'

def greb():
    url = f"https://www.evimitasi.com/key/{huruf}?page={pagee}"
    response = requests.get(url).text
    domains = re.findall(r'<a href="/www.(.*?)"', response)
    if domains:
        tod = len(domains)
        with open('../ress.txt', 'a') as file:
            file.write("\n".join(domains) + "\n")
        todd = sum(1 for _ in open('../ress.txt'))
        print(f"{okegreen}[{red}OK!{okegreen}]{cyan} Found {tod} Domain > Page : {pagee} > Total Di .txt : {todd}")
    else:
        print(f"{okegreen}[{red}-{okegreen}]${red} Error Woy!!")

def banner():
    print(f"{okegreen}<<<<<>>>>>")
    print(f"{cyan}       Grabber by Drian")
    print(f"{cyan}    Grabber Domain by A-Z 0-9")
    print(f"{okegreen}<<<<<>>>>>")
    print()
    print(f"{cyan}Masukkan ABCDEFGHIJKLMNOPQRSTUVWXYZ012345678")
    print(f"{cyan}Contoh: Huruf: => A")
    print(f"{cyan}Note: Harus Huruf Gede!")
    print(white)
    global huruf, page, pagenya
    huruf = input("Huruf: => ")
    page = int(input("Page: "))
    pagenya = int(input("Mau Page Berapa: "))

if __name__ == "__main__":
    os.system('clear')
    banner()
    for pagee in range(page, pagenya + 1):
        greb()

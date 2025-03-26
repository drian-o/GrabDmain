#!/usr/bin/env python3
# Created by Chris

import os
import re
import requests

blue = '\033[0;34m'
cyan = '\033[0;36m'
green = '\033[0;32m'
okegreen = '\033[92m'
lightgreen = '\033[1;32m'
white = '\033[1;37m'
red = '\033[1;31m'
yellow = '\033[1;33m'

def greb():
    apinya = requests.get(f"https://www.iapolo.com/google/map{pagee}.xml").text
    domains = re.findall(r'<loc>(.*?)</loc>', apinya)
    if domains:
        tod = len(domains)
        cleaned_domains = [domain.replace("https://www.iapolo.com/", "") for domain in domains]
        with open('../grab3.txt', 'a') as file:
            file.write("\n".join(cleaned_domains) + "\n")
        todd = sum(1 for _ in open('../grab3.txt'))
        print(f"{okegreen}[{red}OK!{okegreen}]{cyan} Found {tod} Domain > Page : {pagee} > Total Di .txt : {todd}")
    else:
        print(f"{okegreen}[{red}-{okegreen}]{red} Error Woy!!")

def banner():
    print(f"{okegreen}<<<<<>>>>>")
    print(f"{cyan}       Grabber by Drian")
    print(f"{cyan}      Priv Domain Grabber")
    print(f"{okegreen}<<<<<>>>>>")
    global page, pagenya
    page = int(input("Halaman: "))
    pagenya = int(input("Mau Sampai Halaman (Max 22522): "))

if __name__ == "__main__":
    os.system('clear')
    banner()
    for pagee in range(page, pagenya + 1):
        greb()
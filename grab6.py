#!/usr/bin/env python3
# Created by Chris

import os
import re
import requests

blue = '\033[0;34'
cyan = '\033[0;36m'
green = '\033[0;34m'
okegreen = '\033[92m'
lightgreen = '\033[1;32m'
white = '\033[1;37m'
red = '\033[1;31m'
yellow = '\033[1;33m'

def grab():
    url = f"https://rankchart.org/sitemap/{pagee}.xml"
    response = requests.get(url).text
    domains = re.findall(r'<loc>https://rankchart.org/site/(.*?)</loc>', response)
    if domains:
        tod = len(domains)
        cleaned_domains = [domain.replace("https://rankchart.org/site/", "") for domain in domains]
        with open('../ressbypage.txt', 'a') as file:
            file.write("\n".join(cleaned_domains) + "\n")
        todd = sum(1 for _ in open('../ressbypage.txt'))
        print(f"{okegreen}[{red}OK!{okegreen}]{cyan} Found {tod} Domain > Page : {pagee} > Total Di .txt : {todd}")
    else:
        print(f"{okegreen}[{red}-{okegreen}]${red} Error Woy!!")

def banner():
    print()
    print(f"{okegreen}<<<<<>>>>>")
    print(f"{cyan}       Grabber by Drian")
    print(f"{cyan}      Priv Domain Grabber")
    print(f"{okegreen}<<<<<>>>>>")
    print()
    global page, pagenya
    page = int(input("Page: "))
    pagenya = int(input("To Page (Max 10001): "))

if __name__ == "__main__":
    os.system('clear')
    banner()
    for pagee in range(page, pagenya + 1):
        grab()
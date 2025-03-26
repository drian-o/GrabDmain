import requests
import os
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

init(autoreset=True)
success_color = Fore.GREEN
failure_color = Fore.RED
warning_color = Fore.YELLOW
reset = Style.RESET_ALL

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.93 Safari/537.36"
}

os.system('cls' if os.name == 'nt' else 'clear')

banner = '''
██████╗ ███████╗██╗   ██╗██╗██████╗ 
██╔══██╗██╔════╝██║   ██║██║██╔══██╗
██████╔╝█████╗  ██║   ██║██║██████╔╝
██╔══██╗██╔══╝  ╚██╗ ██╔╝██║██╔═══╝ 
██║  ██║███████╗ ╚████╔╝ ██║██║     
╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚═╝╚═╝     
                                    
                                                                                             
Mass Reverse IP
Coded By Drian
'''
print(success_color + banner + reset)
list_site = input("Give list: ")
# Menambahkan path "../" ke list_site
list_site = "../" + list_site

# Memastikan path yang diberikan dalam bentuk absolut
if not os.path.isabs(list_site):
    list_site = os.path.abspath(os.path.join(os.getcwd(), list_site))

# Membaca daftar situs dari file
with open(list_site, 'r') as file:
    sites = file.read().splitlines()

unique_sites = set()
unique_ips = set()

for site in sites:
    url = f"https://rapiddns.io/sameip/{site}?full=1#result"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"{failure_color}Gagal melakukan request untuk {site}")
        continue

    soup = BeautifulSoup(response.text, 'html.parser')
    table_rows = soup.find('tbody').find_all('tr')

    website_count = 0
    ip_count = 0

    for row in table_rows:
        website = row.find_all('td')[0].text
        ip = row.find_all('td')[1].text

        unwanted_words = ['webmail.', 'cpanel.', 'www.', 'webdisk.', 'mail.', 'cpcontacts.', 'cpcalendars.', 'autodiscover.']
        for word in unwanted_words:
            website = website.replace(word, '')

        if website not in unique_sites:
            website_count += 1
            unique_sites.add(website)
            with open('../domain.txt', 'a') as site_file:
                site_file.write(website + '\n')

        if ip not in unique_ips:
            ip_count += 1
            unique_ips.add(ip)
            with open('../ip.txt', 'a') as ip_file:
                ip_file.write(ip + '\n')

    print(f"{site} {failure_color}site {success_color}{website_count} {failure_color}ip {success_color}{ip_count}")

print(f"{warning_color}Pemrosesan selesai.")

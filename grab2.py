import requests
from bs4 import BeautifulSoup

def scrape_and_save(domain_text, max_records):
    # URL dasar yang akan digunakan
    base_url = "https://domains.tntcode.com/?domain_name_box=%0D%0A&domain_name_box_2={}&whois_status_box=&maximum_records_box={}&maximum_characters_box=&availability_box=any&can_contain_letters_box=true&can_contain_numbers_box=true&can_contain_dashes_box=true&sort=&order="

    url = base_url.format(domain_text, max_records)

    response = requests.get(url)

    if response.status_code == 200:
        # Parsing halaman web menggunakan BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        textarea = soup.find('textarea', {'style': 'display:block; width:calc(100% - 2em); margin-top:1em; padding:0.5em;', 'rows': '20'})

        if textarea:
            web_content = textarea.text.strip()

            with open('../keyword.txt', 'w', encoding='utf-8') as file:
                file.write(web_content)

            print(f"Hasil scraping disimpan dalam hasil.txt")
        else:
            print("Tag <textarea> tidak ditemukan.")
    else:
        print(f"Gagal mengakses URL: {url}")

input_text = input("keyword: ")
max_records = input("Jumlah domain: ")

scrape_and_save(input_text, max_records)

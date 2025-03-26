import os
import requests
import time

yellow = '\033[1;33m'
red = '\033[1;31m'
clear = '\033[0m'

print(yellow + "[==============================]")
print(yellow + "   " + yellow + "Priv8 Domain Grabber")
print(yellow + "   " + yellow + "Version  : 4.0")
print(yellow + "   " + yellow + "Drian")
print(yellow + "[==============================]")

domain = input("Input Domains: ")
response = requests.get("https://tranco-list.eu/download/65GX/10000000000000000000000000000000000")
results = [line.split(",")[1] for line in response.text.splitlines() if line.endswith("." + domain)]

parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
result_file_path = os.path.join(parent_directory, f"{domain}.txt")

with open(result_file_path, "w") as file:
    for result in results:
        file.write(result + "\n")

print("Grabbing...")
time.sleep(3)

with open(result_file_path, "r") as file:
    for line in file:
        print(line.strip())

print(clear)
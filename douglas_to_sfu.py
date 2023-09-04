from bs4 import BeautifulSoup
import requests
import re
import sys
import time

html_text = requests.get(
    f"https://www.douglascollege.ca/course/{sys.argv[1].lower()}-{sys.argv[2]}"
).text
soup = BeautifulSoup(html_text, "lxml")
transfers = soup.find("div", class_="transfers")

for transfer in transfers:
    if "SFU" in transfer.text:
        equivalent = re.search("(SFU \w\w\w?\w? \d\d\d\w?)", transfer.text)
        print(equivalent[0])

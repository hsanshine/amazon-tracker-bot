# amazon price tracker
# 2021-11-13
# kyamanywa Hamza

import requests
from bs4 import BeautifulSoup
import smtplib

item_url = 'https://www.amazon.com/Carhartt-Midweight-Sleeve-Sweatshirt-Regular/dp/B002G9UD8C/ref=sr_1_2?keywords=hoodies+for+men+winter&qid=1636803926&sr=8-2'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Accept-Langauge': 'en-US,en;q=0.9',

}
response = requests.get(item_url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)

price_tag = soup.select_one(".a-price > .a-offscreen")

hoodie_price = price_tag.getText().split('$')[1]

print(hoodie_price)

desired_price = 25


if hoodie_price <= desired_price:
    print('you can now by the hoodie bro!')
    print(f'link : {item_url}')

# testing request exceptions
#
# response = requests.get('https://httpbin.org/status/200')
#
# try:
#     response.raise_for_status()
#
# except requests.exceptions.HTTPError:
#     print("error error error")
#
# print(response)
#
#
#
# try:
#     requests.get('https://dadgagkdfjaodjfsfdfsfldfs.com')  # url does not exist
#     response.raise_for_status()
# except requests.exceptions.ConnectionError:
#     print('connection error')
#
# print(response)
#
#
# # try to time out a request
# try:
#     r = requests.get('https://facebook.com', timeout=0.0001)
#     print(r)
# except requests.exceptions.Timeout:
#     print('time out!!!')

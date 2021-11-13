# amazon price tracker
# 2021-11-13
# Kyamanywa Hamza
# must provide headers, desired price and item url

import os
import scrapper
import mail

# gmail login information
gmail_user = os.getenv('MY_GMAIL')
gmail_password = os.getenv('MY_GMAIL_PASSWORD')

desired_price = 25
item_url = 'https://www.amazon.com/Carhartt-Midweight-Sleeve-Sweatshirt-Regular/dp/B002G9UD8C/ref=sr_1_2?keywords=hoodies+for+men+winter&qid=1636803926&sr=8-2'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Accept-Langauge': 'en-US,en;q=0.9',
}

sender = 'hamzamycode@gmail.com'
receivers = ['sanshinehamza@gmail.com', 'untilhamza@gmail.com']

response = scrapper.send_request(item_url, header)
soup = scrapper.scrap(response)
# print(soup.title)

price_tag = soup.select_one(".a-price > .a-offscreen")

hoodie_price = price_tag.getText().split('$')[1]

# print(hoodie_price)


if float(hoodie_price) <= desired_price:
    subject = 'Buy item from Amazon'
    receivers = ['untilhamza@gmail.com', 'sanshinehamza@gmail.com']
    content = f' This is mail from you bot. \n You can now by the hoodie from {item_url} for ${hoodie_price}'
    mail_server = mail.Mail(gmail_user, gmail_password)
    mail_server.send(receivers, subject, content)

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

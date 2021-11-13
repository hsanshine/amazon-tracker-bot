# amazon price tracker
# 2021-11-13
# kyamanywa Hamza

import os
import scrapper
import mail

# gmail login information
gmail_user = os.getenv('MY_GMAIL')
gmail_password = os.getenv('MY_GMAIL_PASSWORD')

item_url = 'https://www.amazon.com/Carhartt-Midweight-Sleeve-Sweatshirt-Regular/dp/B002G9UD8C/ref=sr_1_2?keywords=hoodies+for+men+winter&qid=1636803926&sr=8-2'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Accept-Langauge': 'en-US,en;q=0.9',
}

sender = 'hamzamycode@gmail.com'
receivers = ['sanshinehamza@gmail.com', 'untilhamza@gmail.com']



subject = 'SMTP e-mail test'
receivers = ['untilhamza@gmail.com', 'sanshinehamza@gmail.com']
content = ''' This is a test email message. '''

response = scrapper.send_request(item_url, header)
soup = scrapper.scrap(response)


mail_server = mail.Mail()
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

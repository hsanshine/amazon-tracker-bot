import requests
from bs4 import BeautifulSoup


def send_request(scrap_url, scrap_url_header):
    try:
        response = requests.get(scrap_url, headers=scrap_url_header)
        return response
    except requests.exceptions.ConnectionError:
        print('connection error!')


def scrap(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup



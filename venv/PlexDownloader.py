import requests
from bs4 import BeautifulSoup
import json
import subprocess

def get_url():
    url = "https://plex.tv/api/downloads/1.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    site_json = json.loads(soup.text)
    readit = json.dumps(site_json, indent=4)
    testing = {}
    i = 0
    for urld in site_json['computer']['Linux']['releases']:
        testing[i] = urld
        i += 1
    dict_second = {}
    dict_second = testing[1]
    return dict_second['url']
yeet = get_url()
print(yeet)


def wget_url(address):





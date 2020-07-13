import requests
from bs4 import BeautifulSoup
import json
import subprocess


def get_url():
    #I don't have the slightest idea of what I'm doing with dictionaries
    #To start, we're going to get the copy of the json file that has the url for the installer we care about
    #after that we're going to drill down into the dictionary to get the url and return it
    #unfortunately I don't know what I'm doing so we need 2 dictionaries, the first one imports a relatively large amount
    #of the file, but my solution to getting the url required a second dictionary to get the URL in a form where I could
    #get it successfully. After that we return the URL. There's no way this code is optimal.

    #Get the json page we need using beautiful soup
    #Set it up for loading via json.loads
    url = "https://plex.tv/api/downloads/1.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    site_json = json.loads(soup.text)
    #load the first dictionary
    json_Dictionary_Raw = {}
    index = 0
    for section in site_json['computer']['Linux']['releases']:
        json_Dictionary_Raw[i] = section
        index += 1

    #At this point there's 6 lines in dict_First. We need the second line to get loaded into another dictionary
    #That way we can grab the URL key from that line
    json_Dictionary_Trimmed = {}
    json_Dictionary_Trimmed = json_Dictionary_Raw[1]
    return json_Dictionary_Trimmed['url']
address = get_url()
def wget_url(address):





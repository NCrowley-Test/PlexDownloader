import requests
from bs4 import BeautifulSoup
import json
import subprocess
import config
import os
import time
start_time = time.time()

def get_url():
    # I don't have the slightest idea of what I'm doing with dictionaries
    # To start, we're going to get the copy of the json file that has the url for the installer we care about
    # after that we're going to drill down into the dictionary to get the url and return it
    # unfortunately I don't know what I'm doing so we need 2 dictionaries, the first one imports a relatively large amount
    # of the file, but my solution to getting the url required a second dictionary to get the URL in a form where I could
    # get it successfully. After that we return the URL. There's no way this code is optimal.

    # Get the json page we need using beautiful soup
    # Set it up for loading via json.loads
    url = "https://plex.tv/api/downloads/1.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    site_json = json.loads(soup.text)
    # load the first dictionary
    json_Dictionary_Raw = {}
    index = 0
    for section in site_json['computer']['Linux']['releases']:
        json_Dictionary_Raw[index] = section
        index += 1

    # At this point there's 6 lines in dict_First. We need the second line to get loaded into another dictionary
    # That way we can grab the URL key from that line
    json_Dictionary_Trimmed = {}
    json_Dictionary_Trimmed = json_Dictionary_Raw[1]
    return json_Dictionary_Trimmed['url']

# All this does is grab the file from the known address
def wget_url(address):
    subprocess.run(["wget",address])


# Function to see if there's an updated file to download
def check_If_New_Url(address):
    soup = BeautifulSoup(page.content, 'html.parser')
    site_json = json.loads(soup.text)
    # load the first dictionary
    json_Dictionary_Raw = {}
    index = 0
    for section in site_json['computer']['Linux']['releases']:
        json_Dictionary_Raw[index] = section
        index += 1

    # At this point there's 6 lines in dict_First. We need the second line to get loaded into another dictionary
    # That way we can grab the URL key from that line
    json_Dictionary_Trimmed = {}
    json_Dictionary_Trimmed = json_Dictionary_Raw[1]
    return json_Dictionary_Trimmed['url']

    # Function to see if there's an updated file to download


def check_If_New_Url(address):
    # Open a text file with the most recent version that's been downloaded
    checkfile = open("currenturl.txt")
    # If it's the same as the old version, return true
    if address == checkfile.read():
        checkfile.close()
        print("Worked!")
        return True
    # Otherwise, overwrite the old address and return false so we know to continue
    else:
        checkfile.close()
        checkfile = open("currenturl.txt", "w")
        checkfile.write(address)
        checkfile.close()
        return False


def get_Installer_Name(address):
    # Strip out the last bit of the address that contains the filename, then return
    seperator = "/debian/"
    return address.partition(seperator)[2]


def dpkg_Install_File(installer):
    subprocess.run(["dpkg", "-i", installer])
    subprocess.run(["rm", installer])

address = get_url()
installer = get_Installer_Name(address)
if check_If_New_Url(address) == True:
    # There isn't a new address, so no new installer. Program can exit
    print("--- %s seconds ---" % (time.time() - start_time))
    exit(1)

else:
    # There's a new address, so a new installer.
    wget_url(address)
    dpkg_Install_File(installer)
    print("--- %s seconds ---" % (time.time() - start_time))
    exit(2)
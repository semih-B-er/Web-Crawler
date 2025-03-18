import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin



url = "https://news.ycombinator.com/"
found_Links =[]
def make_reques(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text , "html.parser")
    return soup
def crwl(url):
    links = make_reques(url)
    for link in links.find_all('a'):
        foundLink = link.get('href')
        if foundLink:
            foundLink = urljoin(url, foundLink)
            if "#" in foundLink:
                foundLink = foundLink.split("#")[0]
            if url in foundLink and foundLink not in found_Links:
                found_Links.append(foundLink)
                print(foundLink)
                #recursive
                crwl(foundLink)

crwl(url)


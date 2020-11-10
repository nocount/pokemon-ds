# Scraping images for computer vision work

import os

from urllib.request import urlopen, Request, URLopener
from bs4 import BeautifulSoup


def scrape_pokemon_image(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')

    images = soup.find_all('img')
    image_link = images[0].get('src')

    print("[INFO] downloading {}".format(image_link))
    name = str(image_link.split('/')[-1])
    opener = URLopener()
    opener.addheader('User-Agent', 'Mozilla/5.0')
    opener.retrieve(image_link, os.path.join('data/images/', name))

    print(image_link)


def scrape_pokemon_data(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'html.parser')

    index = 0
    for p in soup.find_all('span', class_='infocard-lg-data'):
        entity = p.find('a', class_='ent-name').get('href')
        link = 'https://pokemondb.net' + entity

        scrape_pokemon_image(link)

        # index += 1
        # if index == 10:
        #     break


    def

if __name__ == '__main__':
    scrape_pokemon_data('https://pokemondb.net/pokedex/national')
    print('Praise the Sun')

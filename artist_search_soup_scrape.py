'''
this program will ask user for artist/band name and return the lyrics
webaddress for the desired artist/musician while also retrieving the
htlm soup from the artist landing page
'''
import requests
import time
import numpy as np
from bs4 import BeautifulSoup


def search_lyricsdotcom(artist):
    '''
    creates link for the lyrics
    '''
    path = 'https://www.lyrics.com/lyrics/' + artist
    return path


def get_landing_soup(landingpage, artist_underscore):
    '''
    retrieves the text from the website in a beautiful soup
    '''
    resp = requests.get(landingpage)
    soup = BeautifulSoup(resp.text, features="lxml")
    time.sleep(np.random.uniform(0.4, 1.3))
    with open(f'./data/html/{artist_underscore}_landing_page.html', 'w') as f:
        f.write(str(soup))
    return soup


def get_artist_link(soup_overview):
    '''
    retrieves the artist link
    '''
    link = soup_overview.find(class_="tal fx")
    link = link.a['href']
    link = 'https://www.lyrics.com/' + str(link)
    return link

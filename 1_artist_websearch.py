'''
this program will ask user for artist/band name and return the lyrics
webaddress for the desired artist/musician
'''
import requests
import time
import numpy as np
from bs4 import BeautifulSoup


def search_lyricsdotcom(artist):
    path = 'https://www.lyrics.com/lyrics/' + artist
    return path


def get_soup(link):
    '''
    retrieves the text from artist search in a beautiful soup
    '''
    resp = requests.get(link)
    soup = BeautifulSoup(resp.text, features="lxml")
    time.sleep(np.random.uniform(0.4, 1.3))
    return soup


def get_artist_link(soup_overview):
    '''
    retrieves the artist link
    '''
    link = soup_overview.find(class_ = "tal fx")
    link = link.a['href']
    link = 'https://www.lyrics.com/' + str(link)
    print(link)
    return link


name = input('Enter desired band of artist name: ')
path = search_lyricsdotcom(name)
soup = get_soup(path)
get_artist_link(soup)

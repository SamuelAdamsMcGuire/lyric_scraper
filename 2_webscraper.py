#using the web address for the desired artist the user can then using the command line
#enter the webaddress and through this program the lyrics will be scraped. 

import requests
import time
import sys
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

def get_soup(landingpage):
    '''
    retrieves the text from the website in a beautiful soup
    '''
    resp = requests.get(landingpage)
    soup = BeautifulSoup(resp.text, features="lxml")
    time.sleep(np.random.uniform(0.4, 1.3))
    return soup

def get_artist(soup_overview):
    '''
    retrieves artist name from the soup
    '''
    return soup_overview.find(class_ = "artist").text

def get_links(soup_overview):
    '''
    retrieves the song links
    '''
    links = soup_overview.find_all(class_ = "tal qx")
    links = [link.a['href'] for link in links]
    links = ['https://www.lyrics.com' + str(link) for link in links]
    return links

def get_lyrics(link):
    '''
    scraps the lyrics
    '''
    resp = requests.get(link)
    soup = BeautifulSoup(resp.text, features="lxml")
    lyrics = soup.find(class_='lyric-body').text
    time.sleep(np.random.uniform(0.4, 1.3))
    return lyrics

args = sys.argv
artistpage = sys.argv[1]

soup = get_soup(artistpage)
artist = get_artist(soup)
links = get_links(soup)


lyric_dictionary = {'artist':[], 'lyrics':[]}

try:
    for i in tqdm(range(len(links))):
        lyric_dictionary['artist'].append(artist)
        lyric = get_lyrics(links[i])
        lyric_dictionary['lyrics'].append(lyric)
except ValueError:
        pass
except AttributeError:
        pass

lyric_df = pd.DataFrame(lyric_dictionary, columns=['artist', 'lyrics'])
lyric_df.to_csv('lyrics_' + artist + '.csv', sep='\t')

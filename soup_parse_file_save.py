'''
using the web address for the desired artist the user can then using the
command line enter the webaddress and through this program the lyrics
will be scraped.
'''

import requests
import time
import sys
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm


def get_artist(soup_overview):
    '''
    retrieves artist name from the soup
    '''
    return soup_overview.find(class_="artist").text


def get_links(soup_overview):
    '''
    retrieves the song links
    '''
    link_soup = soup_overview.find_all(class_="tal qx")
    link_href = [link.a['href'] for link in link_soup]
    links = ['https://www.lyrics.com' + str(link) for link in link_href]
    return links


def get_song_title(soup_overview):
    '''
    retrieves songs titles
    '''
    link_soup = soup_overview.find_all(class_="tal qx")
    titles = [link.a.text for link in link_soup]
    return titles


def get_lyrics(link, artist):
    '''
    scraps the lyrics
    '''
    resp = requests.get(link)
    soup = BeautifulSoup(resp.text, features="lxml")
    lyrics = soup.find(class_='lyric-body').text
    time.sleep(np.random.uniform(0.4, 1.3))
    with open(f'./data/html/{artist}_song_page.html', 'w') as f:
        f.write(str(soup))
    return lyrics


def save_songs(links, title, artist):
    lyric_dictionary = {'artist': [], 'title': [], 'lyrics': []}

    try:
        for i in tqdm(range(len(links))):
            lyric_dictionary['artist'].append(artist)
            title = title  # get_song_title(soup_overview)
            lyric_dictionary['title'].append(title[i])
            lyric = get_lyrics(links[i], artist.replace(' ', '_'))
            lyric_dictionary['lyrics'].append(lyric)
    except ValueError:
        pass
    except AttributeError:
        pass

    artist_underscore = artist.replace(' ', '_')
    lyric_df = pd.DataFrame(
        lyric_dictionary, columns=[
            'artist', 'title', 'lyrics'])
    lyric_df.drop_duplicates(subset=['title'], inplace=True)
    lyric_df.to_csv(f'./data/lyrics/lyrics_{artist_underscore}.csv', sep='\t')
    print(f'Dataframe for {artist} has been made!')

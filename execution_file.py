'''
Execution file for the entire program. Allows users to download new artists or test the trained model on it's knowledge of the artist's lyrics
'''

import pickle
import spacy
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from token_maker import custom_tokenizer
from artist_search_soup_scrape import search_lyricsdotcom, get_artist_link, get_landing_soup
from soup_parse_file_save import get_lyrics, get_links, get_artist, save_songs, get_song_title
from lyric_compiler import lyric_compiler
from model_bow_generator import prepare_data, preprocessing_data, train_save_model

df = pd.read_csv('data/compiled_lyrics/df_total.csv')
artists = df['artist'].unique().tolist()

print('Welcome to the 8 ball lyric scraper and lyric predictor!')
print(f"Our current database has {', '.join(artists[0:-1])} and {artists[-1]} on file.")
ques_1 = input('You are welcome to scrape another artist, however please keep in mind this will take some time.\nWould you like to proceed to predictions(1) or scrape an additional artist(2) (enter 1 or 2)? ')
   
if ques_1 == '2':
    ques_2 = input('Which artist would you like to scrape?')
    artist_underscore = ques_2.replace(' ', '_')
    path = search_lyricsdotcom(ques_2)
    soup_path = get_landing_soup(path, artist_underscore)
    ques_3 = input(f'Is this the correct link: {get_artist_link(soup_path)} (y or n)?')
    if ques_3 == 'y':
        print('This will take a moment')
        artistpage = get_artist_link(soup_path)
        soup_links = get_landing_soup(artistpage, artist_underscore)
        artist = get_artist(soup_links)
        title = get_song_title(soup_links)
        links = get_links(soup_links)
        save_songs(links, title, artist)
        file_directory = '/home/samuel/git_projects/lyric_scraper/data/lyrics/'
        lyric_compiler(file_directory, artist)
        corpus_train, corpus_test, y_train, y_test = prepare_data('/home/samuel/git_projects/lyric_scraper/data/compiled_lyrics/df_total.csv')
        bow, X_train, X_test = preprocessing_data(corpus_train, corpus_test)
        print('Now to train you new model so we can add the new artist! Radical!')
        train_save_model(LogisticRegression(class_weight='balanced'), X_train, y_train)
        with open('models/bow.p', 'rb') as f:
            bow = pickle.load(f)
        with open('models/model.p', 'rb') as f:
            m = pickle.load(f)
        while True:
            print('So let\'s get to some predictions dude!')
            keywords = input('Enter some lyrics or push return to exit: ')
            artist_pred = m.predict(bow.transform([keywords]))[0]
            artist_prob = round(m.predict_proba(bow.transform([keywords])).max(), 2)*100

            if keywords == '':
                print('Thanks for hangin! Come again!')
                break
            else:
                print(f'The magic 8 ball says the artist is: {artist_pred} with a confidence of {artist_prob}%.')
elif ques_1 == '1':
    print('Then lets get to the prediction fun!')
    
    with open('models/bow.p', 'rb') as f:
        bow = pickle.load(f)

    with open('models/model.p', 'rb') as f:
        m = pickle.load(f)

    while True:
        keywords = input('Enter some lyrics or push return to exit: ')
        artist_pred = m.predict(bow.transform([keywords]))[0]
        artist_prob = round(m.predict_proba(bow.transform([keywords])).max(), 2)*100
        #might use the below variables in the future to give a more verbose output
        #classes = m.classes_
        #class_percents = np.round(m.predict_proba(bow.transform([keywords])), 2)*100

        if keywords == '':
            print('Thanks for hangin! Come again!')
            break
        else:
            print(f'The magic 8 ball says the artist is: {artist_pred} with a  confidence of {artist_prob}%.')

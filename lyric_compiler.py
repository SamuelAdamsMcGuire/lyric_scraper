'''this program will iterate through all the dataframes containing the scraped
lyrics then combine them all into one dataframe, save the dataframe to be used
to train a model for predictions.
'''

import os
import sys
import pandas as pd


def lyric_compiler(file_directory, artist):
    '''
    this function iterate through .csv files
    and compiles them into one dataframe
    '''
    df_total = pd.DataFrame(columns=['artist', 'title', 'lyrics'])

    for filename in os.listdir(file_directory):
        df = pd.read_csv(file_directory+filename, index_col=0, error_bad_lines=False, sep='\t')
        df_total = df_total.append(df)

    df_total.to_csv('./data/compiled_lyrics/df_total.csv', index=False)
    print(f'The available songs from {artist} have been scraped and added to our database')

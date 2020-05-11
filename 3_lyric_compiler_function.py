'''this program will iterate through all the dataframes containing the scraped
lyrics then combine them all into one dataframe to be used develop a model for
out predictions compiler works, but when the file df_total already exist in the
file directory then an error will return need to fix this
'''

import os
import sys
import pandas as pd


def local_lyric_compiler(file_directory):
    '''
    this function iterate through .csv files
    and compiles them into one dataframe
    '''
    df_total = pd.DataFrame(columns=['artist', 'lyrics'])

    for filename in os.listdir(file_directory):
        df = pd.read_csv('data/lyrics/'+filename, index_col=0, error_bad_lines=False, sep='\t')
        df_total = df_total.append(df)

    df_total.to_csv('data/compiled_lyrics/df_total.csv', index=False)


args = sys.argv
directory = sys.argv[1]

local_lyric_compiler(directory)

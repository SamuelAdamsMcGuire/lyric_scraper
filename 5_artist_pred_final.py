'''
Here the models are used to make predictions on which artist wrote/would have
written the lyrics that are entered by the user.
'''
import pickle
import spacy
import sys
import pandas as pd


nlp = spacy.load("en_core_web_sm", disable=["parser", "textcat", "ner"])
#lyrics = pd.read_csv('lyrics/df_total.csv', error_bad_lines=False)


def custom_tokenizer(text):
    tokens = []
    for t in nlp(text):
        if not(len(t) < 2 or t.is_stop or t.like_num or
               t.is_punct or t.is_oov or not t.is_alpha):
            tokens.append(t.lemma_)
    return tokens


with open('models/bow.p', 'rb') as f:
    bow = pickle.load(f)

with open('models/model.p', 'rb') as f:
    m = pickle.load(f)

while True:
    keywords = input('Enter some lyrics between single quotation marks or break to exit: ')
    aritist_pred = m.predict(bow.transform([keywords]))

    if keywords == 'break':
        break
    else:
        print('The magic 8 ball says the artist is: ' + aritist_pred[0])

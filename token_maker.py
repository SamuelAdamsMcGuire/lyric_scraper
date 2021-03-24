'''custom tokenizer to remove and lemmatize the data'''

import spacy

nlp = spacy.load("en_core_web_sm", disable=["parser", "textcat", "ner"])


def custom_tokenizer(text):
    '''
    used to filter out unwanted words, punctuation, and so on
    '''
    tokens = []
    for t in nlp(text):
        if not(len(t) < 2 or t.is_stop or t.like_num or
               t.is_punct or not t.is_alpha):
            tokens.append(t.lemma_)
    return tokens

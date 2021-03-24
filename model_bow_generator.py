'''
Preprocesses data, trains model and saves trained model
'''
import pickle
import pandas as pd
from bs4 import BeautifulSoup
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn import metrics
from tqdm import tqdm
from token_maker import custom_tokenizer


def prepare_data(data_path):
    '''
    data is read in and split for use in model training
    '''
    df_total = pd.read_csv(data_path)
    corpus = df_total['lyrics']
    y = df_total['artist']
    corpus_train, corpus_test, y_train, y_test = train_test_split(
        corpus, y, test_size=0.4, train_size=0.6)
    return(corpus_train, corpus_test, y_train, y_test)


def preprocessing_data(corpus_train, corpus_test):
    '''
    bag of words vectorization is used to make the features for our model
    '''
    bow = CountVectorizer(tokenizer=custom_tokenizer,
                          ngram_range=(1, 1),
                          min_df=0.01,
                          max_df=0.99)
    X_train = bow.fit_transform(corpus_train)
    X_test = bow.transform(corpus_test)
    with open('models/bow.p', 'wb') as f:
        pickle.dump(bow, f)
    print('Your preprocessing model has been save for use in training your model! Party on Wayne')
    return(bow, X_train, X_test)


def train_save_model(model_w_hparams, X_train, y_train):
    '''
    data transformed useing TFiDF and then model is trained and saved
    '''
    m = Pipeline([
        ('Tfidf', TfidfTransformer()),
        ('model', model_w_hparams)])
    m.fit(X_train, y_train)
    with open('models/model.p', 'wb') as f:
        pickle.dump(m, f)
    print('Your model has been trained with the new data and saved for use. Excellent!')
    return m

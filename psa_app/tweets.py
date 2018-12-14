#!/usr/bin/env python
# coding: utf-8

# In[77]:


import nltk
nltk.download('stopwords')
nltk.download('wordnet')
import random
import pandas as pd
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string


# In[78]:


import sqlite3 ,csv
conn = sqlite3.connect('db_sentiment_v2.sqlite3')
print("Opened.")
cur = conn.cursor()


# In[79]:


#test database
cur = conn.execute("SELECT tweet_text from psa_tweet LIMIT 5")
result = cur.fetchall()

for x in result:
  print(x)


# In[80]:


#create a dataframe with all tweets 
df = pd.read_sql_query("SELECT tweet_text from psa_tweet;", conn)
df


# In[81]:


#save alltweets to a text file
df.to_csv('tweets.txt', index=False, sep=' ', header=None)


# In[82]:


#text cleaning
import spacy
spacy.load('en')
from spacy.lang.en import English
parser = English()
def tokenize(text):
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens


# In[83]:


import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma
    
from nltk.stem.wordnet import WordNetLemmatizer
def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)


# In[84]:


#filter stopwords
nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))


# In[85]:


#prepare text for topic modeling
def prepare_text_for_lda(text):
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens


# In[86]:


text_data = []
with open('tweets.txt') as f:
    for line in f:
        tokens = prepare_text_for_lda(line)
        if random.random() > .99:
            print(tokens)
            text_data.append(tokens)


# In[87]:


#LDA WITH GENSIM
from gensim import corpora
dictionary = corpora.Dictionary(text_data)
corpus = [dictionary.doc2bow(text) for text in text_data]
Lda = gensim.models.ldamodel.LdaModel
ldamodel = Lda(corpus, num_topics=10, id2word = dictionary, passes=30)


# In[88]:


#print 10 topics
topics = ldamodel.print_topics(num_topics=10, num_words=4)
for topic in topics:
    print(topic)


# In[ ]:





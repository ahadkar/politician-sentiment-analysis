# Created by Aditya Hadkar

from .models import Politician
from .models import Tweet
from .models import Stats
from .models import Topics
from .models import TweetTopic

import time
import csv

import spacy
from spacy.lang.en import English
spacy.load('en')
parser = English()

import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('wordnet')

nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))

import random
import gensim

from gensim import corpora

import pickle


def analyze_stats():

    positive_tweet_count = 0
    negative_tweet_count = 0
    neutral_tweet_count = 0

    most_positive_tweet = ""
    most_positive_tweet_id = 0
    most_positive_tweet_score = 0.0

    most_negative_tweet_score = -0.05
    most_negative_tweet = ""
    most_negative_tweet_id = 0

    start_time = time.time()

    for tweet in Tweet.objects.all().iterator(2000):

        sentiment_polarity = ""

        if float(tweet.sentiment_score) >= 0.05:
            positive_tweet_count += 1
            sentiment_polarity = "positive"

            if float(tweet.sentiment_score) > most_positive_tweet_score:
                most_positive_tweet_score = tweet.sentiment_score
                most_positive_tweet_id = tweet.tweet_id
                most_positive_tweet = tweet.tweet_text

        elif -0.05 < float(tweet.sentiment_score) < 0.05:
                neutral_tweet_count += 1
                sentiment_polarity = "neutral"

        elif float(tweet.sentiment_score) <= -0.05:
            negative_tweet_count += 1
            sentiment_polarity = "negative"

            if float(tweet.sentiment_score) < most_negative_tweet_score:
                most_negative_tweet_score = tweet.sentiment_score
                most_negative_tweet_id = tweet.tweet_id
                most_negative_tweet = tweet.tweet_text

        tweet.sentiment_polarity = sentiment_polarity

        # print(tweet.sentiment_polarity)

    stat = Stats.objects.create()
    stat.most_positive_tweet = most_positive_tweet
    stat.most_positive_tweet_id = most_positive_tweet_id
    stat.positive_tweet_count = positive_tweet_count
    stat.most_negative_tweet = most_negative_tweet
    stat.most_negative_tweet_id = most_negative_tweet_id
    stat.negative_tweet_count = negative_tweet_count
    stat.neutral_tweet_count = neutral_tweet_count

    stat.save()

    print(most_positive_tweet, most_positive_tweet_id, most_positive_tweet_score)
    print(most_negative_tweet, most_negative_tweet_id, most_negative_tweet_score)
    print("Elapsed: {} seconds".format(round(time.time() - start_time, 4)))


def analyze_topics():

    start_time = time.time()

    text_data = []

    count = 0

    for tweet in Tweet.objects.all().iterator(2500):

        tokens = prepare_text_for_lda(tweet.tweet_text)

        count += 1

        print("Processing Row: ", count)

        if random.random() > .99:
            print(tokens)
            text_data.append(tokens)

    print("Finished creating tokens...")
    print("Elapsed: {} seconds".format(round(time.time() - start_time, 4)))

    print("Creating corpus...")

    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]

    print("Loading pickle...")

    pickle.dump(corpus, open('corpus.pkl', 'wb'))
    dictionary.save('dictionary.gensim')

    print("Creating Model...")
    start_time = time.time()

    num_topics = 5

    lda_model = gensim.models.ldamodel.LdaModel(corpus, num_topics=num_topics,
                                                id2word=dictionary,
                                                passes=15,
                                                chunksize=10000)

    lda_model.save('model5.gensim')

    topics = lda_model.print_topics(num_words=4)

    print("Finished creating model.")
    print("Elapsed: {} seconds".format(round(time.time() - start_time, 4)))

    print("Generating topics...")
    start_time = time.time()

    if Topics.objects.count() > 0:
        Topics.objects.all().delete()

    count = 0

    for topic in topics:

        print(topic)

        psa_topic = Topics.objects.create()
        psa_topic.topics = topic[1]
        psa_topic.topic_id = topic[0]

        psa_topic.save()

        count += 1

    print("Finished creating tokens.")
    print("Elapsed: {} seconds".format(round(time.time() - start_time, 4)))

    print("Generating topics for tweets...")

    count = 0

    if TweetTopic.objects.count() > 0:
        TweetTopic.objects.all().delete()

    # all_tweet_topics = list.append(["topic_id", "tweet_id", "user_id", "topic_coverage"])

    for tweet in Tweet.objects.all().iterator(2500):

        print("Processing Row: ", count)
        count += 1

        if isinstance(tweet.tweet_id, str):
            continue
        else:

            new_doc = prepare_text_for_lda(tweet.tweet_text)
            new_doc_bow = dictionary.doc2bow(new_doc)

            extracted_topics = lda_model.get_document_topics(new_doc_bow)

            print(extracted_topics)

            for distribution in extracted_topics:
                tweet_topic = TweetTopic.objects.create()

                tweet_topic.tweet_id = int(tweet.tweet_id)
                tweet_topic.user_id = int(tweet.user_id)

                tweet_topic.topic_id = int(distribution[0])
                tweet_topic.topic_coverage = float(distribution[1])

                tweet_topic.save()

                # all_tweet_topics.append([str(tweet_topic.topic_id),
                #                          str(tweet_topic.tweet_id),
                #                          str(tweet_topic.user_id),
                #                          str(tweet_topic.topic_coverage)])

    # Alternate approach
    # print("Writing to file.")
    #
    # with open('topics.csv', 'w', newline='') as file:
    #     wr = csv.writer(file, quoting=csv.QUOTE_ALL)
    #     wr.writerows(all_tweet_topics)

    # TweetTopic.objects.bulk_create(all_tweet_topics)

    print("Finished creating model.")
    print("Elapsed: {} seconds".format(round(time.time() - start_time, 4)))


def tokenize(text):
    lda_tokens = []
    tokens = parser(text)

    # Ignore - lda_tokens.append('URL')
    # Ignore - lda_tokens.append('SCREEN_NAME')

    for token in tokens:
        if token.orth_.isspace() or token.like_url or token.orth_.startswith('@'):
            continue
        else:
            lda_tokens.append(token.lower_)

    return lda_tokens


def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma


def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)


def prepare_text_for_lda(text):
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens


import gc


def queryset_iterator(queryset, chunksize=1000):

    # Iterate over a Django Queryset ordered by the primary key
    #
    # This method loads a maximum of chunk size (default: 1000) rows in it's
    # memory at the same time while django normally would load all rows in it's
    # memory. Using the iterator() method only causes it to not preload all the
    # classes.
    #
    # Note that the implementation of the iterator does not support ordered query sets.

    pk = 0
    last_pk = queryset.order_by('-pk')[0].pk
    queryset = queryset.order_by('pk')
    while pk < last_pk:
        for row in queryset.filter(pk__gt=pk)[:chunksize]:
            pk = row.pk
            yield row
        gc.collect()


def clean_up_tweet_topics():

    if TweetTopic.objects.count() > 0:
        TweetTopic.objects.all().delete()

    if Topics.objects.count() > 0:
        Topics.objects.all().delete()


if __name__ == '__main__':
    analyze_topics()

'''
Perform sentiment analysis on tweets.
Use bag-of-words presentation.
Pre-processing includes cleaning the tweets, tokenizing and stemming the tweets.
Use VADER to do sentiment analysis.
Leverage the compound score to classify tweets into different sentiment polarities.
'''
import re
import sqlite3
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def clean_tweet (tweet):
    # remove stock market tickers like $GE
    tweet = re.sub(r'\$\w*', '', tweet)

    # remove old style retweet text "RT"
    tweet = re.sub(r'^RT[\s]+', '', tweet)

    # remove URLs
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)

    # remove the hash # sign from the word
    tweet = re.sub(r'#', '', tweet)

    return tweet

def process_tweet(tweet):
    stopwords_english = stopwords.words('english')

    # tokenize tweets
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet)

    # remove stop words and stem the word
    tweet_clean = ''
    for word in tweet_tokens:
        if word not in stopwords_english:
            stem_word = WordNetLemmatizer().lemmatize(word)
            tweet_clean = tweet_clean + ' ' + stem_word

    return tweet_clean

def get_score(tweet):
    # get scores using VADER
    analyser = SentimentIntensityAnalyzer()
    scores = analyser.polarity_scores(tweet)

    # retrieve the compound score
    score = scores.get('compound')

    return score

def get_polarity(score):
    # clarify scores into different polarity
    if score >= 0.05:
        polarity = 'positive'
    elif score <= -0.05:
        polarity = 'negative'
    else:
        polarity = 'neutral'

    return polarity

def retrieve_tweets():
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()

    # retrieve all the tweets in from the database
    cursor.execute('''SELECT id, tweet_text FROM psa_tweet''')
    all_tweets = cursor.fetchall()
    db.close()

    return all_tweets

def update_sentiment(id, score, polarity):
    # update the score of a single tweet into the database
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    cursor.execute('''UPDATE psa_tweet SET sentiment_score = ?, sentiment_polarity = ? WHERE id = ?''', (score,polarity,id))

    db.commit()
    db.close()

def main():
    # retrieve the tweets
    all_tweets = retrieve_tweets()

    # for each tweet, clean and process it, then get the sentiment info and update the database
    for row in all_tweets:
        id = row[0]
        tweet = row[1]

        tweet_cleaned = clean_tweet(tweet)
        tweet_processed = process_tweet(tweet_cleaned)
        score = get_score(tweet_processed)
        polarity = get_polarity(score)

        update_sentiment(id, score, polarity)

if __name__ == "__main__":
    main()




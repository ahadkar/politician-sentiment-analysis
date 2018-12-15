# Created by Aditya Hadkar

from .models import Politician
from .models import Tweet
from .models import Stats

import time


def calculate():

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


if __name__ == '__main__':
    calculate()

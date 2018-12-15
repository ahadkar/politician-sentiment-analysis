# Created by Aditya Hadkar
# psa/views.py

from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Politician
from .models import Tweet
from .models import Stats

from psa import tweet_analyzer

# Create your views here.

tweet_sort_order = ''


class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    html = "about.html"
    template_name = html


def politician_list(request):

    all_politicians = Politician.objects.order_by('screen_name')

    stat = Stats.objects.first()
    stat.total_tweet_count = 1048575

    page = request.GET.get('page', 1)

    paginator = Paginator(all_politicians, 30)

    try:
        politicians = paginator.page(page)
    except PageNotAnInteger:
        politicians = paginator.page(1)
    except EmptyPage:
        politicians = paginator.page(paginator.num_pages)

    global tweet_sort_order

    tweet_sort_order = 'created_at'

    context = {
        'pol_list': politicians,
        'stat': stat,
        'sort_order': tweet_sort_order,
    }

    # tweet_analyzer.calculate()

    return render(request, 'index.html', context)


def pol_tweets(request):

    screen_name = request.GET.get('screen_name')

    politician = Politician.objects.get(screen_name=screen_name)

    global tweet_sort_order

    tweet_sort_order = request.GET.get('sort_order')

    if len(tweet_sort_order) == 0:
        tweet_sort_order = 'created_at'

    all_tweets = Tweet.objects.filter(user_id=politician.twitter_id).order_by(tweet_sort_order)

    stat = Stats.objects.create()

    most_positive_tweet_score = 0.0
    most_positive_tweet_id = 0

    most_negative_tweet_score = -0.05
    most_negative_tweet_id = 0

    for tweet in all_tweets.iterator():

        stat.total_tweet_count += 1

        if tweet.polarity() == "Positive":
            stat.positive_tweet_count += 1

            if float(tweet.sentiment_score) > most_positive_tweet_score:
                most_positive_tweet_score = float(tweet.sentiment_score)
                most_positive_tweet_id = tweet.tweet_id

        elif tweet.polarity() == "Negative":
            stat.negative_tweet_count += 1

        elif tweet.polarity() == "Neutral":
            stat.neutral_tweet_count += 1

            if float(tweet.sentiment_score) < most_negative_tweet_score:
                most_negative_tweet_score = tweet.sentiment_score
                most_negative_tweet_id = tweet.tweet_id

    positive_tweet = all_tweets.filter(tweet_id=most_positive_tweet_id)
    negative_tweet = all_tweets.filter(tweet_id=most_negative_tweet_id)

    page = request.GET.get('page', 1)

    paginator = Paginator(all_tweets, 75)

    try:
        tweets = paginator.page(page)
    except PageNotAnInteger:
        tweets = paginator.page(1)
    except EmptyPage:
        tweets = paginator.page(paginator.num_pages)

    context = {
        'testData': 'Hello: ' + screen_name,
        'politician': politician,
        'tweets': tweets,
        'positive_tweet': positive_tweet,
        'negative_tweet': negative_tweet,
        'stat': stat,
        'sort_order': tweet_sort_order
    }

    return render(request, 'tweets.html', context)

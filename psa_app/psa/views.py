# Created by Aditya Hadkar
# psa/views.py

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404
from .models import Politician
from .models import Tweet

# Create your views here.


class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    html = "about.html"
    template_name = html


def politician_list(request):

    pol_list = Politician.objects.order_by('latest_following_count')

    context = {
        "pol_list": pol_list,
    }

    return render(request, 'index.html', context)


def politician_tweet_list(request, twitter_id):

    try:
        tweet_list = Tweet.objects.get(twitter_id)
    except Tweet.DoesNotExist:
        raise Http404("Tweets don't exist for this user.")

    context = {'politician_tweet_list': tweet_list}

    '''
    Follow from here:
    https://docs.djangoproject.com/en/2.1/intro/tutorial03/
    '''

    return render(request, 'tweets/index.html', context)

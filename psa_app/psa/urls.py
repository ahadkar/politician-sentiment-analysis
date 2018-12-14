# Created by Aditya Hadkar
# psa/urls.py

from psa import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^', views.politician_list, name='politician_list'),
    url('<bigint:twitter_id/>', views.politician_list, name='politician_tweet_list'),
]

# Created by Aditya Hadkar
# psa/urls.py

from django.conf.urls import url,include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'tweets', views.pol_tweets, name='tweets'),
    url(r'^', views.politician_list, name='politician_list'),
]

#path('<str:screen_name>/', views.pol_tweets, name='tweets'),
#url(r'^screen_name=(?P<screen_name>\d+)/$', views.pol_tweets, name='tweets'),

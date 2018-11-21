# Created by Aditya Hadkar
# psa/urls.py

from django.conf.urls import url, include
from psa import views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
	url(r'^about/$', views.AboutPageView.as_view()),
]
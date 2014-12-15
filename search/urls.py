from django.conf.urls import patterns, include, url
from search.views import index, search

urlpatterns = patterns('',
 	url(r'^$', index),
 	url(r'^key/$', search, name="search_key"),
)

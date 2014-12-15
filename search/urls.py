from django.conf.urls import patterns, include, url
from search.views import index, SearchAjaxView

urlpatterns = patterns('',
 	url(r'^$', index),
 	url(r'^key/$', SearchAjaxView.as_view(), name="search_key"),
)

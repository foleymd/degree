from django.conf.urls import *
from django.conf import settings

urlpatterns = patterns('degree.minors.links.views',
    url(r'^$', 'index', name='index_link'),  # if nothing, go to function 'inbox' (not sure about braces, inbox_link is a shorthand link
    )

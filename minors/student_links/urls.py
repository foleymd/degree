from django.conf.urls import *
from degree.minors.student_links.views import index
from django.conf import settings

urlpatterns = [
    url(r'^$', index, name='student_links_index'),
]

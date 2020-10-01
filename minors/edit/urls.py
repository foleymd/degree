from django.conf.urls import *
from django.conf import settings

urlpatterns = patterns('degree.minors.edit.views',
    url(r'^(?P<stat_ty_schl_fos_seq>[A-Za-z0-9 ]*)$', 'edit', name='edit_link'),  # if nothing, go to function 'inbox' (not sure about braces, inbox_link is a shorthand link
    )

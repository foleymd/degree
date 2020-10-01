from django.conf.urls import patterns, url

urlpatterns = patterns('degree.minors.log.views',
    url(r'^(?P<eid>\w{3,8})/$', 'logs_by_eid', name='logs_by_eid'),
    url(r'$', 'search', name='search'),
)

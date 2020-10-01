from django.conf.urls import include, patterns, url

# from degree.minors.manage_student.views import *

urlpatterns = patterns('degree.minors.manage_student.views',
    url(r'^student_credential/(?P<doc_nbr>\d{1,10})/$', 'student_credential', name='credential_by_doc_nbr'),
    url(r'^student_credential/$', 'student_credential', name="student_credential"),
    url(r'^search_by_eid/$', 'search_by_eid', name="search_by_eid"),
    url(r'^search_by_code/$', 'search_by_code', name="search_by_code"),
    url(r'^late_add_inbox/$', 'late_add_inbox', name="late_add_inbox"),
    url(r'^reports/$', 'reports', name="reports"),
    url(r'$', 'search_by_eid', name='search'),

)

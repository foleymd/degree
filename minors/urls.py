import django.conf.urls

urlpatterns = django.conf.urls.patterns('',
    (r'^apps/degree/minors/edit/', django.conf.urls.include('degree.minors.edit.urls')),
    (r'^apps/degree/minors/', django.conf.urls.include('degree.minors.inventory.urls')),
    (r'^apps/degree/minors/manage_student/', django.conf.urls.include('degree.minors.manage_student.urls')),
    (r'^apps/degree/minors/log/', django.conf.urls.include('degree.minors.log.urls')),
    (r'^apps/degree/minors/links/', django.conf.urls.include('degree.minors.links.urls')),
    (r'^apps/degree/minors/student_links/nlogon/', django.conf.urls.include('degree.minors.student_links.urls')),
                                        )

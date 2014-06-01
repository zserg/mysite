from django.conf.urls import patterns, url

from ruseng import views

urlpatterns = patterns('ruseng.views',
        (r'^.*$','ruseng'),
                      )
urlpatterns += patterns('',
        (r'^accounts/login/', 'django.contrib.auth.views.login', 
         {'template_name': 'notes/login.html'}),
                       )


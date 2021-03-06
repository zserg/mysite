from django.conf.urls import patterns, url

from server import views

urlpatterns = patterns('server.views',
        (r'^status$','status'),
        (r'^status_(.+)$','status_by_name'),
                      )
urlpatterns += patterns('',
        (r'^accounts/login/', 'django.contrib.auth.views.login', 
         {'template_name': 'notes/login.html'}),
                       )


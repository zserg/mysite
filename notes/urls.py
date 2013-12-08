from django.conf.urls import patterns, url

from notes import views

urlpatterns = patterns('notes.views',
        (r'^(?P<file_name>.+\.txt)$', 'post'), 
        (r"", "main"),
                      )
urlpatterns += patterns('',
        (r'^accounts/login/', 'django.contrib.auth.views.login', 
         {'template_name': 'notes/login.html'}),
                       )


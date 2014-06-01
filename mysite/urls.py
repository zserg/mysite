from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
     url(r'^blog/', include('blog.urls')),
     url(r'^notes/', include('notes.urls')),
     url(r'^server/', include('server.urls')),
     url(r'^ruseng/', include('ruseng.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
        (r'^accounts/login/', 'django.contrib.auth.views.login', 
         {'template_name': 'notes/login.html'}),
                       )


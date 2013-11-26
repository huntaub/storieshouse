from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
# ... the rest of your URLconf goes here ...
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'storieshouse.views.home', name='home'),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/?logged_out=true'}),
    url(r'^change_password/$', 'django.contrib.auth.views.password_change', {'post_change_redirect': '/account/'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/', include('podcast.urls')),
    url(r'^', include('house.urls')),
)

urlpatterns += staticfiles_urlpatterns()
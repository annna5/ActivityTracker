from django.conf.urls import patterns, include, url
from django.contrib import admin
import apptest.urls
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'l6.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^zaj7/', include(apptest.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

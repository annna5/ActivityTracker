from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.competition_list, name='competition_list'),
    url(r'^events_from_date/(?P<lower>\w+)', views.events_from_date, name='events_from_date'),
    url(r'^calendar$', views.calendar, name='calendar'),
    url(r'^statistics', views.statistics, name='statistics'),
    # url(r'^sport/templates/sport/my_calendar.html$', views.calendar, name='my_calendar'),
    url(r'^comp/(?P<pk>[0-9]+)/$', views.comp_detail, name='comp_detail'),
    url(r'^comp_list_for_dist/(?P<dist>[0-9]+\.[0-9]+)/$', views.comp_list_for_dist, name='comp_list_for_dist'),
    url(r'^comp/new/$', views.competition_new, name='competition_new'),
    url(r'^comp/(?P<pk>[0-9]+)/edit/$', views.comp_edit, name='comp_edit'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/register/complete/$', views.registration_complete, name='registration_complete'),
    url(r'^comp/(?P<pk>[0-9]+)/remove/$', views.comp_remove, name='comp_remove'),

]

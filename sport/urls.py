from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.competition_list, name='competition_list'),
    url(r'^upcoming_events$', views.upcoming_events, name='upcoming_events'),
    url(r'^old_events$', views.old_events, name='old_events'),
    url(r'^calendar$', views.calendar, name='calendar'),
    url(r'^statistics', views.statistics, name='statistics'),
    # url(r'^sport/templates/sport/my_calendar.html$', views.calendar, name='my_calendar'),
    url(r'^comp/(?P<pk>[0-9]+)/$', views.comp_detail, name='comp_detail'),
    url(r'^comp/new/$', views.competition_new, name='competition_new'),
    url(r'^comp/(?P<pk>[0-9]+)/edit/$', views.comp_edit, name='comp_edit'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/register/complete/$', views.registration_complete, name='registration_complete'),
    url(r'^comp/(?P<pk>[0-9]+)/remove/$', views.comp_remove, name='comp_remove'),

]

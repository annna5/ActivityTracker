from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.competition_list, name='competition_list'),
    url(r'^comp/(?P<pk>[0-9]+)/$', views.comp_detail, name='comp_detail'),
    url(r'^comp/new/$', views.competition_new, name='competition_new'),
]

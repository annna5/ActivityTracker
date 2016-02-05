from django.conf.urls import *
from apptest.views import *

urlpatterns = patterns('',
    (r'^testowanie$', create),
    (r'^testowaniemany', createmany),
    (r'^journale', wyszukaj)
)

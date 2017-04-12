from django.conf.urls import url
from simpleapi.views import *

urlpatterns = [
    url(r'^trends/$', all_trens),
    url(r'^trends/(?P<id>[0-9]+)$', given_trend),
]

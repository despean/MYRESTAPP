from django.conf.urls import url
from simpleapi.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^trends/$', all_trens),
    url(r'^trends/(?P<id>[0-9]+)$', given_trend),
]

urlpatterns = format_suffix_patterns(urlpatterns)
from django.conf.urls import url
from estavos.clubs.views import ClubDetail, ClubList


urlpatterns = [
    url(r'^$', ClubList.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ClubDetail.as_view(), name='detail'),
]

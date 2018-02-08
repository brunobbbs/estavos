from django.conf.urls import url
from estavos.clubs.views import ClubList


urlpatterns = [
    url(r'^$', ClubList.as_view(), name='list'),
]

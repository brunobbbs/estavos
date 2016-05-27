from django.conf.urls import url
from estavos.tournaments.views import TournamentListView, TournamentDetail

urlpatterns = [
    url(r'^$', TournamentListView.as_view(), name='list'),
    url(r'(?P<pk>\d+)/$', TournamentDetail.as_view(), name='detail'),
]

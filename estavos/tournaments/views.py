from django.views.generic import ListView, DetailView
from estavos.tournaments.models import Tournament


class TournamentListView(ListView):
    model = Tournament
    queryset = Tournament.objects.all().filter(active=True)
    
    def get_context_data(self, **kwargs):
        kwargs = super(TournamentListView, self).get_context_data(**kwargs)
        inactive_tournaments = Tournament.objects.all().filter(active=False)
        kwargs['inactive_tournaments'] = inactive_tournaments
        return kwargs


class TournamentDetail(DetailView):
    model = Tournament
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TournamentConfig(AppConfig):
    name = 'estavos.tournaments'
    verbose_name = _('Torneios')

    def ready(self):
        import estavos.tournaments.signals  # noqa

from django.views.generic import ListView
from estavos.activities.models import Activity
from braces.views import LoginRequiredMixin


class ActivityListView(LoginRequiredMixin, ListView):
    model = Activity
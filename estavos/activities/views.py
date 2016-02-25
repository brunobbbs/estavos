from django.views.generic import ListView
from estavos.activities.models import Activity


class ActivityListView(ListView):
    model = Activity
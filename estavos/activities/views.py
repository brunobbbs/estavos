from django.views.generic import ListView
from estavos.activities.models import Activity
from braces.views import LoginRequiredMixin


class ActivityListView(LoginRequiredMixin, ListView):
    model = Activity

    def get_queryset(self):
        qs = super(ActivityListView, self).get_queryset()
        user = self.request.user
        if user.is_authenticated() and not user.is_superuser:
            qs = qs.filter(partner=user)
        return qs
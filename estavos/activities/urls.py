from django.conf.urls import url
from estavos.activities.views import ActivityListView


urlpatterns = [
    url(r'^$', ActivityListView.as_view(), name='list'),
]

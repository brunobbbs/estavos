from django.conf.urls import url
from estavos.courses.views import Home, Inscription

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^inscricao/$', Inscription.as_view(), name='inscription'),
]

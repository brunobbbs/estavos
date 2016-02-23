from django.conf.urls import url
from estavos.courses.views import Home, PreInscription, InscriptionView, CoursesListView

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'inscricao/$', CoursesListView.as_view(), name='list'),
    url(r'inscricao/(?P<course_id>\d+)/$', InscriptionView.as_view(), name='inscription'),
    url(r'inscricao/concluido/(?P<pk>\d+)/$', PreInscription.as_view(), name='preinscription'),
]

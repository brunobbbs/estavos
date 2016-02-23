from django.conf.urls import url
from estavos.courses.views import Home, InscriptionDetail, InscriptionView, CoursesListView

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'inscricao/$', CoursesListView.as_view(), name='list'),
    url(r'inscricao/(?P<course_id>\d+)/$', InscriptionView.as_view(), name='inscription'),
    url(r'inscricao/concluido/(?P<slug>\w+)/$', InscriptionDetail.as_view(), name='inscription_detail'),
]

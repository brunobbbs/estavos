from django.conf.urls import url
from estavos.courses.views import Home, InscriptionDetail, InscriptionCreate, CoursesListView

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'inscricao/$', CoursesListView.as_view(), name='list'),
    url(r'inscricao/(?P<course_id>\d+)/$', InscriptionCreate.as_view(), name='inscription'),
    url(r'inscricao/detalhes/(?P<slug>\w+)/$', InscriptionDetail.as_view(), name='inscription_detail'),
]
